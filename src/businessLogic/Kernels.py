import numpy as np

class typesKernels():
    
    def KernelNitidezSharpen():
        KernelNitidezSharpen = np.array([[0, -1, 0], 
                                         [-1, 5, -1], 
                                         [0, -1, 0]])
        return KernelNitidezSharpen
    
    def KernelsDeteccaoBordasLaplaciano():
        KernelsDeteccaoBordasLaplaciano = np.array([[0, 1, 0],
                                                    [1, -4, 1],
                                                    [0, 1, 0]])
        return KernelsDeteccaoBordasLaplaciano

    def KernelsSuavizaçãoBlur():
        KernelsSuavizaçãoBlur = np.array([[1/9, 1/9, 1/9],
                                          [1/9, 1/9, 1/9],
                                          [1/9, 1/9, 1/9]])
        return KernelsSuavizaçãoBlur
    
    def kernelGaussianoblur():
        kernelGaussianoblur = np.array([[1/16, 2/16, 1/16],
                                        [2/16, 4/16, 2/16],
                                        [1/16, 2/16, 1/16]])
        return kernelGaussianoblur
    
    def kernelRelevo():
        kernelRelevo = np.array([[-2, -1, 0],
                                  [-1, 1, 1],
                                  [0, 1, 2]])
        return kernelRelevo
    

    def kernelSharpenIntenso():
        kernelSharpenIntenso = np.array([[-1, -1, -1],
                                         [-1,  9, -1],
                                         [-1, -1, -1]])
        return kernelSharpenIntenso

    def kernelSobelX():
        kernelSobelX = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]])
        return kernelSobelX

    def kernelSobelY():
        kernelSobelY = np.array([[-1, -2, -1],
                                 [ 0,  0,  0],
                                 [ 1,  2,  1]])
        return kernelSobelY

    def kernelMotionBlur():
        kernelMotionBlur = np.zeros((9, 9))
        kernelMotionBlur[4, :] = np.ones(9) # Linha central com 1s
        kernelMotionBlur = kernelMotionBlur / 9 # Normaliza a soma
        return kernelMotionBlur

    def kernelIdentidade():
        kernelIdentidade = np.array([[0, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 0]])
        return kernelIdentidade