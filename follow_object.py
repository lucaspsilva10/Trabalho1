import cv2
import numpy as np
import time
import random

def iniciar_jogo():
    # Configurações iniciais para captura de vídeo
    cap = cv2.VideoCapture(0)
    center_area_size = 100  # Tamanho do quadrado central

    # Função para exibir contagem regressiva e indicar área central
    def contagem_regressiva(frame, numero):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(numero), (int(frame.shape[1] / 2 - 30), int(frame.shape[0] / 2)), font, 2, (0, 0, 255), 3)
        cv2.rectangle(frame,
                      (int(frame.shape[1] / 2 - center_area_size // 2), int(frame.shape[0] / 2 - center_area_size // 2)),
                      (int(frame.shape[1] / 2 + center_area_size // 2), int(frame.shape[0] / 2 + center_area_size // 2)),
                      (255, 0, 0), 2)

    # Temporizador para contagem regressiva
    start_time = time.time()
    countdown_time = 5  # segundos de contagem regressiva
    mean_color = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        elapsed_time = time.time() - start_time
        remaining_time = countdown_time - int(elapsed_time)
        contagem_regressiva(frame, remaining_time)
        cv2.imshow('Siga o Objeto - Preparação', frame)

        if remaining_time == 1 and mean_color is None:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
            center_area = hsv[center_y - center_area_size // 2:center_y + center_area_size // 2,
                              center_x - center_area_size // 2:center_x + center_area_size // 2]
            mean_color = cv2.mean(center_area)[:3]
            print("Cor capturada!")

        if elapsed_time >= countdown_time:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return False

    # Define a faixa de cor do objeto com base na cor média detectada
    if mean_color is not None:
        hue = int(mean_color[0])
        saturation = int(mean_color[1])
        value = int(mean_color[2])
        lower_color = np.array([hue - 10, max(50, saturation - 40), max(50, value - 40)])
        upper_color = np.array([hue + 10, min(255, saturation + 40), min(255, value + 40)])
    else:
        print("Erro: Não foi possível detectar a cor.")
        cap.release()
        cv2.destroyAllWindows()
        return False

    detected_object_center = None
    num_circles = 5
    current_circle = 0
    circle_position = None
    circle_start_time = None
    game_over = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))

            if detected_object_center is None and abs(center[0] - frame.shape[1] // 2) < 30 and abs(center[1] - frame.shape[0] // 2) < 30:
                detected_object_center = center
                print("Objeto inicial detectado no centro.")

            if radius > 10:
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        if game_over:
            cv2.putText(frame, "Game Over", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.putText(frame, "Pressione 'q' para sair", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, "'p' para reiniciar", (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Siga o Objeto', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return False
            elif key == ord('p'):
                cap.release()
                cv2.destroyAllWindows()
                return True
            continue

        if current_circle < num_circles:
            if circle_position is None:
                circle_position = (random.randint(100, frame.shape[1] - 100), random.randint(100, frame.shape[0] - 100))
                circle_start_time = time.time()

            cv2.circle(frame, circle_position, 20, (255, 0, 0), -1)
            elapsed_circle_time = time.time() - circle_start_time

            # Exibir a quantidade de alvos acertados
            cv2.putText(frame, f"Alvos acertados: {current_circle}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if elapsed_circle_time > 3:
                game_over = True
            else:
                distance = np.linalg.norm(np.array(center) - np.array(circle_position))
                if distance < 25:
                    current_circle += 1
                    circle_position = None
                    print(f"Alvo {current_circle} alcançado!")

        else:
            cv2.putText(frame, "Parabens!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Pressione 'q' para sair", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Siga o Objeto', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False

# Loop principal para reiniciar o jogo
while True:
    if not iniciar_jogo():
        break
