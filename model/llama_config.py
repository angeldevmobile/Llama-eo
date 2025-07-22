from llama_cpp import Llama
import os

def load_model():
    model_path = os.getenv("MODEL_PATH", "model/Llama-3.2-1B-Instruct-Q5_K_M.gguf")
    model_path = os.path.abspath(model_path)
    print(f"Intentando cargar modelo desde: {model_path}")
    return Llama(model_path=model_path, n_ctx=4096, verbose=True)