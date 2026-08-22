import easyocr
import time
import os

# ---------------------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------------------
FOLDER_PATH = "images"  # Substitua pelo caminho da sua pasta
OUTPUT_FILE = "resultados_placas_easyocr.txt"
EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# ---------------------------------------------------------
# 1) INICIALIZAR O READER DO EASYOCR
# ---------------------------------------------------------
# Mantenha gpu=False se não tiver CUDA configurado no Linux
reader = easyocr.Reader(['pt'], gpu=False)

print("🔄 Iniciando o processamento da pasta...")

# ---------------------------------------------------------
# 2) VERIFICAR SE A PASTA EXISTE
# ---------------------------------------------------------
if not os.path.exists(FOLDER_PATH):
    print(f"❌ ERRO: A pasta '{FOLDER_PATH}' não foi encontrada.")
    exit()

# Listar todas as imagens da pasta
imagens = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(EXTENSOES_VALIDAS)]

if not imagens:
    print(f"⚠️ Nenhuma imagem válida encontrada em '{FOLDER_PATH}'.")
    exit()

# ---------------------------------------------------------
# 3) PROCESSAR IMAGENS E SALVAR NO ARQUIVO .TXT
# ---------------------------------------------------------
inicio_total = time.time()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("===== RESULTADOS EASYOCR - BATCH PLACAS =====\n\n")

    for idx, nome_arquivo in enumerate(imagens, 1):
        caminho_imagem = os.path.join(FOLDER_PATH, nome_arquivo)
        
        inicio_img = time.time()
        # Leitura do texto presente na imagem
        texto_detectado = reader.readtext(caminho_imagem, detail=0)
        tempo_img = time.time() - inicio_img

        # Junta todas as linhas/blocos detectados em uma única string
        leitura_completa = " ".join(texto_detectado) if texto_detectado else "[Nenhum texto detectado]"

        # Escreve os resultados no .txt
        f.write(f"[{idx}] Imagem: {nome_arquivo}\n")
        f.write(f"⏱ Tempo: {tempo_img:.3f}s\n")
        f.write(f"📄 Leitura: {leitura_completa}\n")
        f.write("-" * 40 + "\n")

        print(f"✅ [{idx}/{len(imagens)}] Processado: {nome_arquivo} em {tempo_img:.3f}s")

tempo_total = time.time() - inicio_total

# ---------------------------------------------------------
# 4) FINALIZAÇÃO
# ---------------------------------------------------------
print()
print(f"⏱ Tempo total de execução: {tempo_total:.3f} segundos")
print(f"📁 Todos os resultados foram salvos em: {OUTPUT_FILE}")
print("🟦 Processamento finalizado com sucesso!")
