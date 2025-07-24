from llama_cpp import Llama
import os
import requests

def load_model():
    model_url = os.getenv("MODEL_URL")
    local_path = "model/Llama-3.2-1B-Instruct-Q5_K_M.gguf"
    os.makedirs("model", exist_ok=True)

    # Descarga el modelo solo si no existe localmente
    if not os.path.exists(local_path):
        print(f"Descargando modelo desde {model_url}...")
        response = requests.get(model_url, stream=True)
        with open(local_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("✅ Descarga completa")

    print(f"🔍 Intentando cargar modelo desde: {os.path.abspath(local_path)}")
    return Llama(model_path=local_path, n_ctx=4096, verbose=True)
