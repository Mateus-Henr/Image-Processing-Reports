import cv2
import numpy as np

def segmentacao_mascaras(video_path, cor_time_lower, cor_time_upper):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    cor_time_lower = np.array(cor_time_lower, dtype=np.uint8)
    cor_time_upper = np.array(cor_time_upper, dtype=np.uint8)
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('mascaras_time.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height), isColor=False)
    
    while cap.isOpened():
        ret, frame = cap.read()
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(frame_hsv, cor_time_lower, cor_time_upper)
        kernel = np.ones((5,5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        out.write(mask)
        
        cv2.imshow('Frame', mask)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

cor_time_lower = (70, 85, 80)
cor_time_upper = (120, 255, 255)
segmentacao_mascaras('jogoCruzeiro.mp4', cor_time_lower, cor_time_upper)

def segmentacao_jogadores(video_path, cor_time_lower, cor_time_upper):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    cor_time_lower = np.array(cor_time_lower, dtype=np.uint8)
    cor_time_upper = np.array(cor_time_upper, dtype=np.uint8)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter('jogadores.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height), isColor=True)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_hsv, cor_time_lower, cor_time_upper)
        
        kernel = np.ones((5,5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        result = cv2.bitwise_and(frame, frame, mask=mask)
        out.write(result)
        
        cv2.imshow('Frame', result)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

segmentacao_jogadores('jogoCruzeiro.mp4', cor_time_lower, cor_time_upper)
