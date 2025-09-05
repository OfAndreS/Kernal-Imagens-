# Kernel Applied Filter Project

![Versão do Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Licença](https://img.shields.io/badge/license-MIT-green.svg)
![Status do Projeto](https://img.shields.io/badge/status-ativo-brightgreen)

Uma aplicação de linha de comando (CLI) poderosa e interativa para aplicar filtros de imagem em tempo real usando a técnica de convolução de kernels.

---

### Demonstração Geral

<img width="1387" height="522" alt="image" src="https://github.com/user-attachments/assets/7cc59eb5-8707-43c0-a5d0-75bc497627fc" />


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
| **Motion Blur** | <img width="1152" height="646" alt="image" src="https://github.com/user-attachments/assets/c2533871-2b74-460f-ada8-dcb504f68c01" />*(Simula o efeito de movimento na imagem.)* |
| **Relevo (Emboss)** | <img width="1153" height="647" alt="image" src="https://github.com/user-attachments/assets/3f8ff45d-9b01-4249-a874-ff22a71baf20" />*(Cria um efeito de entalhe ou relevo na imagem.)* |
| **Bordas (Sobel Y)** | <img width="1150" height="647" alt="image" src="https://github.com/user-attachments/assets/3b6a719d-87d5-40f7-94f8-5f12d07292dc" />*(Detecta e realça as bordas horizontais.)* |

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem principal do projeto.
-   **OpenCV**: Utilizado para a operação de convolução (`cv2.filter2D`), garantindo máxima performance.
-   **Pillow (PIL)**: Para abrir, converter e salvar os formatos de imagem.
-   **NumPy**: Para a criação e manipulação eficiente das matrizes (imagens e kernels).

## 🚀 Como Executar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

#### **1. Pré-requisitos**
-   Python 3.12 ou superior.

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
