# Kernel Applied Filter

Este é um projeto simples em Python que utiliza uma interface de linha de comando (CLI) para aplicar diversos filtros de imagem baseados em kernels de convolução. O usuário pode carregar uma imagem, escolher um filtro, definir a intensidade do efeito e salvar o resultado.

## Funcionalidades

  - **Carregamento de Imagem**: Seleciona um arquivo de imagem do sistema através de uma janela de diálogo.
  - **Interface Interativa**: Um menu no terminal permite ao usuário escolher os filtros e opções.
  - **Variedade de Filtros**: Inclui uma coleção de kernels para diferentes efeitos, como suavização, nitidez, detecção de bordas e estilização.
  - **Controle de Intensidade**: Permite aplicar o mesmo filtro múltiplas vezes para intensificar o efeito.
  - **Salvamento Automático**: As imagens processadas são salvas automaticamente na pasta `/output` com um nome descritivo.

## Filtros Disponíveis

O projeto conta com os seguintes filtros implementados:

#### Suavização (Blur)

  - Blur (Box)
  - Blur Gaussiano
  - Motion Blur (Desfoque de Movimento)

#### Nitidez e Relevo

  - Nitidez (Sharpen)
  - Nitidez Intensa
  - Relevo (Emboss)

#### Detecção de Bordas

  - Bordas (Laplaciano)
  - Bordas Verticais (Sobel X)
  - Bordas Horizontais (Sobel Y)

## Estrutura do Projeto

```
.
├── output/              # Pasta onde as imagens processadas são salvas
├── src/
│   ├── businessLogic/
│   │   ├── Kernels.py           # Define todos os kernels de convolução
│   │   ├── mathOperations.py    # Funções de processamento de imagem (convolução, etc.)
│   │   └── fileManager.py       # Gerencia a seleção de arquivos
│   └── app.py               # Script principal que executa a aplicação
└── requirements.txt     # Lista de dependências do projeto
```

## Como Executar

**1. Pré-requisitos:**

  - Python 3.x instalado.

**2. Clone este repositório (opcional):**

```bash
git clone <url-do-seu-repositorio>
cd KernelAppliedFilterProject
```

**3. Crie um ambiente virtual:**

```bash
python -m venv venv
```

  - No Windows:

<!-- end list -->

```bash
.\venv\Scripts\activate
```

  - No macOS/Linux:

<!-- end list -->

```bash
source venv/bin/activate
```

**4. Instale as dependências:**
Certifique-se de que o arquivo `requirements.txt` exista com o seguinte conteúdo:

```
numpy
Pillow
opencv-python
```

Em seguida, instale as bibliotecas com o comando:

```bash
pip install -r requirements.txt
```

**5. Execute a aplicação:**

```bash
python src/app.py
```

Uma janela de seleção de arquivo será aberta. Após selecionar uma imagem, o menu de filtros aparecerá no seu terminal.

## Dependências

  - **Pillow**: Para manipulação de imagens (abrir, salvar).
  - **NumPy**: Para a criação e manipulação das matrizes (kernels e imagens).
  - **OpenCV-Python**: Para a operação de convolução (`cv2.filter2D`) e conversão de cores, que é extremamente rápida e eficiente.
