from PIL import Image # Pillow 
import numpy as np
import cv2            # opencv-python  
import os


def convertImageToMatrizBRB(imagePath):
    imagePill = Image.open(imagePath)
    originalMatriz = np.array(imagePill)
    originalBrbMatriz = cv2.cvtColor(originalMatriz, cv2.COLOR_RGB2BGR)
    
    return originalBrbMatriz

def applieConvolution(matriz_imagem, kernel):
    """
    Aplica um efeito de blur usando um kernel explícito e a função de
    convolução do OpenCV (cv2.filter2D).
    NOTA: Esta função é o método padrão e é EXTREMAMENTE RÁPIDA.
    """
    # cv2.filter2D é a função de convolução.
    # O argumento -1 no ddepth diz ao OpenCV para usar a mesma profundidade
    # de bits da imagem original.
    
    matriz_saida = cv2.filter2D(src=matriz_imagem, ddepth=-1, kernel=kernel)
    return matriz_saida

def convertImageToRGB(matriz_blur_bgr):
    matriz_blur_rgb = cv2.cvtColor(matriz_blur_bgr, cv2.COLOR_BGR2RGB) 
    imagem_blur_pil = Image.fromarray(matriz_blur_rgb)
    
    return imagem_blur_pil

def saveImage(imagem_blur_pil, typeOfFilter): 
    output_dir = os.path.join("..", "output") 

    os.makedirs(output_dir, exist_ok=True)

    id = str(round(np.random.rand() * 1000000))
    file_name = f"img_{typeOfFilter}_{id}.png"
    
    full_path = os.path.join(output_dir, file_name)

    print(f"\n\n| 💾 Salvando imagem em: {full_path}")
    imagem_blur_pil.save(full_path)
    imagem_blur_pil.show() 