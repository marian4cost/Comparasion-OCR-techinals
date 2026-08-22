import pytesseract
from PIL import Image
import time
import os

# ---------------------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------------------
FOLDER_PATH = "images"  # Substitua pelo caminho da sua pasta
OUTPUT_FILE = "resultados_placas_tesseract.txt"
EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# ---------------------------------------------------------
# 1) VERIFICAR SE A PASTA EXISTE
# ---------------------------------------------------------
if not os.path.exists(FOLDER_PATH):
    print(f"❌ ERRO: A pasta '{FOLDER_PATH}' não foi encontrada.")
    exit()

# Listar todas as imagens da pasta
imagens = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(EXTENSOES_VALIDAS)]

if not imagens:
    print(f"⚠️ Nenhuma imagem válida encontrada em '{FOLDER_PATH}'.")
    exit()

print("🔄 Rodando Tesseract OCR na pasta...")

# ---------------------------------------------------------
# 2) PROCESSAR IMAGENS E SALVAR NO ARQUIVO .TXT
# ---------------------------------------------------------
inicio_total = time.time()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS TESSERACT OCR - BATCH PLACAS =====\n\n")

    for idx, nome_arquivo in enumerate(imagens, 1):
        caminho_imagem = os.path.join(FOLDER_PATH, nome_arquivo)
        
        try:
            img = Image.open(caminho_imagem)
            
            inicio_img = time.time()
            # Leitura do texto (usando lang='por' para acentuação e caracteres do PT-BR)
            texto_extraido = pytesseract.image_to_string(img, lang="por")
            tempo_img = time.time() - inicio_img

            # Limpa espaços extras e quebras de linha
            texto_limpo = " ".join(texto_extraido.split())
            leitura_completa = texto_limpo if texto_limpo else "[Nenhum texto detectado]"

            # Escreve os resultados no .txt
            f.write(f"[{idx}] Imagem: {nome_arquivo}\n")
            f.write(f"⏱ Tempo: {tempo_img:.3f}s\n")
            f.write(f"📄 Leitura: {leitura_completa}\n")
            f.write("-" * 40 + "\n")

            print(f"✅ [{idx}/{len(imagens)}] Processado: {nome_arquivo} em {tempo_img:.3f}s")

        except Exception as e:
            print(f"❌ Erro ao processar a imagem {nome_arquivo}: {e}")

tempo_total = time.time() - inicio_total

# ---------------------------------------------------------
# 3) FINALIZAÇÃO
# ---------------------------------------------------------
print()
print(f"⏱ Tempo total de execução (Tesseract): {tempo_total:.3f} segundos")
print(f"📁 Todos os resultados foram salvos em: {OUTPUT_FILE}")
print("🟩 Tesseract Finalizado com sucesso!")