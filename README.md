# Kernel Applied Filter Project

![Versão do Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Licença](https://img.shields.io/badge/license-MIT-green.svg)
![Status do Projeto](https://img.shields.io/badge/status-ativo-brightgreen)

Uma aplicação de linha de comando (CLI) poderosa e interativa para aplicar filtros de imagem em tempo real usando a técnica de convolução de kernels.

---

### Demonstração Geral

![Demonstração do App](https://i.imgur.com/TuZlqQP.gif)

## 📚 Sobre o Projeto

Este projeto permite a manipulação de imagens digitais através de **kernels de convolução**. Um kernel é uma pequena matriz que desliza sobre a imagem, modificando o valor de cada pixel com base em seus vizinhos. Esse processo é a base para dezenas de efeitos, desde um simples desfoque (blur) até a complexa detecção de bordas.

A aplicação foi construída com uma arquitetura modular, separando a lógica de negócios, a interface do usuário e o gerenciamento de arquivos, tornando-a fácil de manter e estender com novos filtros.

## ✨ Funcionalidades Principais

-   **Interface de Linha de Comando Interativa**: Um menu simples e intuitivo para uma experiência de usuário fluida.
-   **Ampla Gama de Filtros**: Coleção de filtros pré-definidos para suavização, nitidez, detecção de bordas e efeitos estilísticos.
-   **Controle de Intensidade**: Aplique qualquer filtro múltiplas vezes para intensificar o efeito desejado.
-   **Visualização em Tempo Real**: A imagem processada é exibida instantaneamente após a aplicação do filtro.
-   **Arquitetura Extensível**: Adicionar novos filtros é tão simples quanto definir uma nova matriz de kernel no arquivo `Kernels.py`.

## 🎨 Showcase de Filtros

Veja alguns dos efeitos que você pode aplicar com este programa.

| Filtro | Demonstração |
| :--- | :---: |
| **Motion Blur** | ![Filtro Motion Blur](https://i.imgur.com/jGq2z5A.gif) <br> *(Simula o efeito de movimento na imagem.)* |
| **Relevo (Emboss)** | ![Filtro de Relevo](https://i.imgur.com/pOz8YxT.gif) <br> *(Cria um efeito de entalhe ou relevo na imagem.)* |
| **Bordas (Sobel Y)** | ![Filtro Sobel](https://i.imgur.com/KcygPjM.gif) <br> *(Detecta e realça as bordas horizontais.)* |

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem principal do projeto.
-   **OpenCV**: Utilizado para a operação de convolução (`cv2.filter2D`), garantindo máxima performance.
-   **Pillow (PIL)**: Para abrir, converter e salvar os formatos de imagem.
-   **NumPy**: Para a criação e manipulação eficiente das matrizes (imagens e kernels).

## 🚀 Como Executar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

#### **1. Pré-requisitos**
-   Python 3.8 ou superior.

#### **2. Instalação**

```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/kernel-applied-filter-project.git](https://github.com/seu-usuario/kernel-applied-filter-project.git)
cd kernel-applied-filter-project

# Crie e ative um ambiente virtual
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
