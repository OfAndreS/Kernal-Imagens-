# conda activate KernelAppliedFilterProject

from businessLogic import fileManager as fm
from businessLogic import mathOperations as mo
from businessLogic import Kernels as k

import numpy as np

def processesImage(intensidade, myKernel, myImage, typeOfFilter):
    if myImage is None:
        print("| ❌ ) - Nenhuma imagem carregada para processar.")
        return

    matriz_processada = mo.convertImageToMatrizBRB(myImage)
        
    print(f"|  aplicando o filtro {typeOfFilter} {intensidade} vez(es)...")

    for _ in range(intensidade):
        matriz_processada = mo.applieConvolution(matriz_processada, myKernel)
            
    finalImage = mo.convertImageToRGB(matriz_processada)
    mo.saveImage(finalImage, typeOfFilter)


def printHeader():
    print("\n\n| * * * * * * * * * * * * * * * * * *\n\n")
    
    
def printChoiceMenu():
    print("\n| * Filtros de Suavização  *  *  *  ")
    print("| 01 ) - Blur (Box)")
    print("| 02 ) - Blur Gaussiano")
    print("| 03 ) - Motion Blur")
    print("\n| * Filtros de Nitidez e Relevo  *  *  *  ")
    print("| 04 ) - Nitidez (Sharpen)")
    print("| 05 ) - Nitidez Intensa")
    print("| 06 ) - Relevo (Emboss)")
    print("\n| * Filtros de Detecção de Bordas  *  *  *  ")
    print("| 07 ) - Bordas (Laplaciano)")
    print("| 08 ) - Bordas Verticais (Sobel X)")
    print("| 09 ) - Bordas Horizontais (Sobel Y)")
    print("\n| * Opções do Programa  *  *  *  ")
    print("| 00 ) - Carregar Nova Imagem")
    print("| Sair")


def firstMenu(myImage):

    while True:
        printChoiceMenu()
        userInput = input("\n| Escolha uma opção: ")

        if userInput.lower() == 'sair':
            print("| Saindo do programa.")
            break

        if not userInput:
            print("| ❌ ) - Entrada inválida. Por favor, escolha uma opção.")
            continue 
        
        myKernel = None
        typeOfFilter = ""
        
        myInput = userInput.zfill(2)

        match myInput:
            case '01':
                myKernel = k.typesKernels.KernelsSuavizaçãoBlur()
                typeOfFilter = "Blur"
            case '02':
                myKernel = k.typesKernels.kernelGaussianoblur()
                typeOfFilter = "BlurGaussiano"
            case '03':
                myKernel = k.typesKernels.kernelMotionBlur()
                typeOfFilter = "MotionBlur"
            case '04':
                myKernel = k.typesKernels.KernelNitidezSharpen()
                typeOfFilter = "NitidezSharpen"
            case '05':
                myKernel = k.typesKernels.kernelSharpenIntenso()
                typeOfFilter = "NitidezIntensa"
            case '06':
                myKernel = k.typesKernels.kernelRelevo()
                typeOfFilter = "Relevo"
            case '07':
                myKernel = k.typesKernels.KernelsDeteccaoBordasLaplaciano()
                typeOfFilter = "BordasLaplaciano"
            case '08':
                myKernel = k.typesKernels.kernelSobelX()
                typeOfFilter = "BordasVerticais_SobelX"
            case '09':
                myKernel = k.typesKernels.kernelSobelY()
                typeOfFilter = "BordasHorizontais_SobelY"
            case '00':
                new_image_path = fm.selectFileWithFileManager()
                if new_image_path:
                    myImage = new_image_path
                    print("| ✅ Nova imagem carregada.")
                else:
                    print("| Nenhuma nova imagem selecionada.")
                continue
            case _: 
                print(f"| ❌ ) - Opção '{userInput}' não reconhecida. Tente novamente.")
                continue
        
        try:
            intensidade_input = input("| Digite a intensidade do efeito (pressione Enter para 1): ")
            if intensidade_input == "":
                intensidade = 1
            else:
                intensidade = int(intensidade_input)
        except ValueError:
            print("| ❌ ) - Intensidade inválida. Usando 1 como padrão.")
            intensidade = 1
            
        processesImage(intensidade, myKernel, myImage, typeOfFilter)

if __name__ == "__main__":
    caminho_imagem = fm.selectFileWithFileManager()
    if caminho_imagem:
        firstMenu(caminho_imagem)
    else:
        print("| Programa encerrado pois nenhuma imagem foi selecionada.")