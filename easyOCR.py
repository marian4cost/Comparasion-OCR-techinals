import easyocr
import time
import os
from collections import Counter

# ------------------------------
# CONFIGURAÇÕES
# ------------------------------
IMAGE_PATH = "pagSherlook.jpeg"
OUTPUT_FILE = "easyocr_resultados.txt"

# ------------------------------
# VERIFICAÇÃO DO CAMINHO
# ------------------------------
if not os.path.exists(IMAGE_PATH):
    print(f"❌ ERRO: O arquivo não foi encontrado:\n{IMAGE_PATH}")
    exit()

# ------------------------------
# 1) INICIALIZAR EASYOCR
# ------------------------------
reader = easyocr.Reader(['en'], gpu=False)

print("🔄 Rodando EasyOCR...")

# ------------------------------
# 2) MEDIR TEMPO
# ------------------------------
inicio = time.time()

# Lê texto da imagem
results = reader.readtext(IMAGE_PATH, detail=0)

fim = time.time()
tempo_execucao = fim - inicio

# ------------------------------
# 3) CONTAGEM DE PALAVRAS
# ------------------------------
texto_completo = " ".join(results)
palavras = texto_completo.split()
contador = Counter(palavras)

# ------------------------------
# 4) SALVAR EM ARQUIVO
# ------------------------------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS EASYOCR =====\n\n")
    f.write(f"Tempo de execução: {tempo_execucao:.3f} segundos\n\n")
    f.write("Palavras detectadas:\n")
    for palavra, freq in contador.items():
        f.write(f"{palavra}: {freq}\n")

print()
print(f"⏱ Tempo de execução (EasyOCR): {tempo_execucao:.3f} segundos")
print(f"📁 Arquivo salvo em: {OUTPUT_FILE}")
print("🟦 EasyOCR Finalizado com sucesso!")
