import pytesseract
from PIL import Image
import time
import os
from collections import Counter

# ---------------------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------------------

IMAGE_PATH = "pagSherlook.jpeg"
OUTPUT_FILE = "tesseract_resultados.txt"

# ---------------------------------------------------------
# 1) VERIFICAÇÃO DO CAMINHO
# ---------------------------------------------------------
if not os.path.exists(IMAGE_PATH):
    print(f"❌ ERRO: O arquivo não foi encontrado:\n{IMAGE_PATH}")
    exit()

# ---------------------------------------------------------
# 2) ABRIR IMAGEM
# ---------------------------------------------------------
try:
    img = Image.open(IMAGE_PATH)
except Exception as e:
    print(f"❌ Erro ao abrir imagem: {e}")
    exit()

print("🔄 Rodando Tesseract OCR...")

# ---------------------------------------------------------
# 3) MEDIR TEMPO
# ---------------------------------------------------------
inicio = time.time()

# Leitura do texto
texto_extraido = pytesseract.image_to_string(img)

fim = time.time()
tempo_execucao = fim - inicio

# ---------------------------------------------------------
# 4) CONTAGEM DE PALAVRAS
# ---------------------------------------------------------
palavras = texto_extraido.split()
contador = Counter(palavras)

# ---------------------------------------------------------
# 5) SALVAR RESULTADOS EM ARQUIVO
# ---------------------------------------------------------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS TESSERACT OCR =====\n\n")
    f.write(f"Tempo de execução: {tempo_execucao:.3f} segundos\n\n")
    f.write("Palavras detectadas:\n")

    for palavra, freq in contador.items():
        f.write(f"{palavra}: {freq}\n")

print()
print(f"⏱ Tempo de execução (Tesseract): {tempo_execucao:.3f} segundos")
print(f"📁 Arquivo salvo em: {OUTPUT_FILE}")
print("🟩 Tesseract Finalizado com sucesso!")