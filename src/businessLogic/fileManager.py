import tkinter as tk
from tkinter import filedialog


def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()

    caminho_do_arquivo = filedialog.askopenfilename()
    
    return caminho_do_arquivo

def selectFileWithFileManager():
    print("| Iniciando o seletor de arquivos...")
    
    arquivo_selecionado = selecionar_arquivo()

    if arquivo_selecionado:
        print(f"\n| ✅ Arquivo selecionado com sucesso!")
        print(f"| O caminho do arquivo é: {arquivo_selecionado}")
        return arquivo_selecionado  

    else:
        print("\n| ❌ Nenhuma seleção foi feita. O programa foi encerrado.")
        return None 