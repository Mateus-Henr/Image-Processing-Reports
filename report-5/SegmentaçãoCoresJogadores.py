import cv2
import numpy as np

# Função para segmentação das máscaras
def segmentacao_mascaras(video_path, cor_time_azul_lower, cor_time_azul_upper, espaco_cor='HSV'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    # Configuração das cores para o time azul (exemplo com HSV)
    cor_time_azul_lower = np.array(cor_time_azul_lower, dtype=np.uint8)
    cor_time_azul_upper = np.array(cor_time_azul_upper, dtype=np.uint8)
    
    # Configuração para salvar o vídeo
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('mascaras_time_azul.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height), isColor=False)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Conversão para o espaço de cor desejado (exemplo com HSV)
        if espaco_cor == 'HSV':
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        elif espaco_cor == 'GRAY':
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            frame_hsv = frame  # se nenhum espaço específico for necessário
        
        # Segmentação por cor para identificar o time azul
        mask_time_azul = cv2.inRange(frame_hsv, cor_time_azul_lower, cor_time_azul_upper)
        
        # Aplicação de filtros morfológicos para melhorar a segmentação
        kernel = np.ones((5,5), np.uint8)
        mask_time_azul = cv2.morphologyEx(mask_time_azul, cv2.MORPH_OPEN, kernel)
        mask_time_azul = cv2.morphologyEx(mask_time_azul, cv2.MORPH_CLOSE, kernel)
        
        # Gravação do vídeo de máscaras
        out.write(mask_time_azul)
        
        cv2.imshow('Frame', mask_time_azul)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Exemplo de uso
cor_time_azul_lower = (70, 85, 80)   # Valores de cor em HSV
cor_time_azul_upper = (120, 255, 255)
segmentacao_mascaras('jogoCruzeiro.mp4', cor_time_azul_lower, cor_time_azul_upper, espaco_cor='HSV')

# Função para segmentação dos jogadores do time azul
def segmentacao_jogadores_time_azul(video_path, cor_time_azul_lower, cor_time_azul_upper, espaco_cor='HSV'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    # Configuração das cores para o time azul (exemplo com HSV)
    cor_time_azul_lower = np.array(cor_time_azul_lower, dtype=np.uint8)
    cor_time_azul_upper = np.array(cor_time_azul_upper, dtype=np.uint8)
    
    # Configuração para salvar o vídeo
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('jogadores_time_azul.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height), isColor=True)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Conversão para o espaço de cor desejado (exemplo com HSV)
        if espaco_cor == 'HSV':
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        elif espaco_cor == 'GRAY':
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            frame_hsv = frame  # se nenhum espaço específico for necessário
        
        # Segmentação por cor para identificar o time azul
        mask_time_azul = cv2.inRange(frame_hsv, cor_time_azul_lower, cor_time_azul_upper)
        
        # Aplicação de filtros morfológicos para melhorar a segmentação
        kernel = np.ones((5,5), np.uint8)
        mask_time_azul = cv2.morphologyEx(mask_time_azul, cv2.MORPH_OPEN, kernel)
        mask_time_azul = cv2.morphologyEx(mask_time_azul, cv2.MORPH_CLOSE, kernel)
        
        # Aplicação da máscara para extrair os jogadores do time azul
        result = cv2.bitwise_and(frame, frame, mask=mask_time_azul)
        
        # Gravação do vídeo dos jogadores do time azul
        out.write(result)
        
        cv2.imshow('Frame', result)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

segmentacao_jogadores_time_azul('jogoCruzeiro.mp4', cor_time_azul_lower, cor_time_azul_upper, espaco_cor='HSV')
