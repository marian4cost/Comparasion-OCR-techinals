# 🔍 Comparative OCR: EasyOCR vs. Tesseract OCR in Python

> **Análise comparativa prática entre Tesseract OCR e EasyOCR para reconhecimento óptico de caracteres (OCR).**

Este repositório apresenta uma análise comparativa entre dois dos motores de OCR mais utilizados na comunidade de Visão Computacional em Python: **Tesseract OCR** e **EasyOCR**.

O projeto avalia o desempenho de ambas as ferramentas em **dois cenários distintos**:

| Cenário                | Descrição                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------- |
| 📖 **Página de Livro** | Extração de texto de um documento estruturado, avaliando acurácia e tempo de processamento.             |
| 🚗 **Lote de Imagens** | Leitura sequencial de imagens armazenadas em um diretório, com os resultados salvos em arquivos `.txt`. |

---

## 🛠️ Tecnologias Utilizadas

* 🐍 **Python 3.12**
* 🔤 **Pytesseract** — Wrapper Python para o Tesseract OCR
* 🤖 **EasyOCR** — Framework de OCR baseado em PyTorch
* 🖼️ **Pillow (PIL)** — Processamento e manipulação de imagens

---

## 💻 Instalação e Pré-requisitos

### 1. Clonar o Repositório

```bash
git clone https://github.com/marian4cost/Comparasion-OCR-techinals
cd Comparasion-OCR-techinals
```

### 2. Criar e Ativar o Ambiente Virtual

#### 🐧 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar o Tesseract OCR

O **Tesseract OCR** é o mecanismo utilizado pelo `pytesseract` para realizar o reconhecimento dos caracteres.

#### 🐧 Ubuntu / Debian

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por -y
```

#### 🪟 Windows

Faça o download do instalador do Tesseract através do projeto **Tesseract at UB Mannheim** e, após a instalação, adicione o caminho do executável ao `PATH` do sistema.

---

### 4. Instalar as Bibliotecas Python

Com o ambiente virtual ativado:

```bash
pip install pytesseract Pillow easyocr
```

---

## 📁 Estrutura do Repositório

```text
Comparasion-OCR-techinals/
│
├── 📂 readingPlate/
        ├── 📂 images/
           └── Imagens utilizadas nos testes em lote
        ├── 🐍 readingPlate/tesseractocr.py
            └── Processamento em lote utilizando Tesseract
        ├── 🐍 readingPlate/easyocr.py
            └── Processamento em lote utilizando EasyOCR
├── 🖼️ pagSherlook.jpeg
│   └── Imagem utilizada no teste individual
│
├── 🐍 tesseract.py
│   └── Leitura de página utilizando Tesseract
│
├── 🐍 easyocr.py
│   └── Leitura de página utilizando EasyOCR
│
├── 📄 .gitignore
│   └── Arquivos ignorados pelo Git
│
└── 📖 README.md
    └── Documentação do projeto
```

---

## 🚀 Como Executar

### 📖 1. Leitura de Página Individual

Para realizar o reconhecimento de uma página de livro ou documento estruturado:

#### Tesseract OCR

```bash
python tesseract.py
```

#### EasyOCR

```bash
python easyocr.py
```

---

### 🚗 2. Processamento em Lote

Para processar sequencialmente as imagens presentes no diretório de testes:

#### Tesseract OCR

```bash
python readingPlate/tesseractocr.py
```

#### EasyOCR

```bash
python readingPlate/easyocr.py
```

Os resultados do processamento são armazenados em arquivos `.txt`, permitindo uma análise posterior das saídas produzidas por cada ferramenta.

---

# 📊 Benchmark

Os experimentos foram realizados considerando principalmente **tempo de processamento, consumo de recursos e capacidade de reconhecimento em diferentes tipos de imagens**.

## ⚡ Principais Descobertas

### 🔤 Tesseract OCR

O **Tesseract OCR** apresentou excelente desempenho em documentos estruturados, como páginas de livros.

**Principais características observadas:**

* ⚡ Processamento significativamente mais rápido;
* 💾 Baixo consumo de memória RAM;
* 📖 Excelente desempenho em textos estruturados;
* ⏱️ Tempo aproximado de **0,8 s por imagem** no cenário avaliado.

> **Resumo:** quando a imagem possui texto bem estruturado, boa iluminação e pouca interferência visual, o Tesseract apresenta uma excelente relação entre velocidade e qualidade.

---

### 🤖 EasyOCR

O **EasyOCR** apresentou maior potencial para situações em que o texto está inserido em imagens mais complexas.

**Principais características observadas:**

* 🧠 Utiliza redes neurais para o reconhecimento;
* 🚗 Mais adequado para cenários de *Scene Text*, como placas e textos presentes em objetos;
* 🌗 Possui maior robustez diante de variações de iluminação e ruídos;
* ⏱️ Apresentou tempo aproximado de **6,8 s por imagem em CPU** no cenário avaliado;
* 💻 Possui maior custo computacional em comparação ao Tesseract.

> **Resumo:** embora seja mais pesado e lento em CPU, o EasyOCR é uma alternativa interessante para imagens menos estruturadas e cenários de Visão Computacional.

---

## ⚖️ Comparação Rápida

| Característica               | 🔤 Tesseract |   🤖 EasyOCR   |
| ---------------------------- | :----------: | :------------: |
| Texto estruturado            |     ⭐⭐⭐⭐⭐    |      ⭐⭐⭐⭐      |
| Scene Text                   |      ⭐⭐⭐     |      ⭐⭐⭐⭐⭐     |
| Placas veiculares            |      ⭐⭐⭐     |      ⭐⭐⭐⭐⭐     |
| Velocidade                   | ⚡ Muito alta |    🐢 Menor    |
| Consumo de memória           |   🟢 Baixo   |    🟠 Maior    |
| Redes neurais                |       ❌      |        ✅       |
| Execução em CPU              | 🟢 Excelente | 🟠 Mais pesada |
| Robustez a imagens complexas |  🟠 Moderada |     🟢 Alta    |
| Facilidade de instalação     |    🟢 Alta   |     🟢 Alta    |

---

## 🎯 Conclusão

A comparação demonstra que **não existe necessariamente um único motor de OCR ideal para todos os cenários**.

A escolha depende principalmente das características das imagens que serão processadas.

### 📖 Para documentos estruturados

**Tesseract OCR** tende a ser a melhor escolha quando o objetivo é:

* processar grandes quantidades de documentos;
* obter alta velocidade;
* utilizar poucos recursos computacionais;
* trabalhar com textos bem estruturados.

### 🚗 Para imagens complexas

**EasyOCR** tende a ser mais interessante quando o objetivo envolve:

* placas veiculares;
* textos presentes em objetos;
* diferentes condições de iluminação;
* imagens com ruído;
* fontes e posições variadas;
* cenários de *Scene Text*.

---

## 📌 Resumo

```text
                    COMPARATIVE OCR
                          │
             ┌────────────┴────────────┐
             │                         │
       TESSERACT OCR              EASYOCR
             │                         │
      ┌──────┴──────┐           ┌──────┴──────┐
      │             │           │             │
  Documentos     Velocidade   Placas       Scene Text
  estruturados      ⚡          🚗             👁️
      │             │           │             │
      └─────────────┘           └─────────────┘
             │                         │
          Leve e                     Mais
           rápido                  robusto
```

---

## 👩‍💻 Autora

**Mariana da Costa Lisboa**

Projeto desenvolvido para estudos e experimentação em **Visão Computacional, OCR e Processamento de Imagens com Python**.

---

## 📄 Licença

Este projeto está disponível para fins **educacionais e experimentais**.
