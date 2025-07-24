from model.llama_config import load_model

llama_model = None  # No se carga aún

prompt_base = """
<|system|>Eres Gurú, un asistente de Inteligencia Artificial de Excelencia Operativa en BBVA. 
Tu propósito es ayudar a los usuarios con eficiencia, cordialidad y precisión. 
Siempre brindas respuestas útiles, claras y breves sobre temas de operaciones. Eres amable y profesional."""

def ask_guru(user_input, history=""):
    global llama_model
    if llama_model is None:
        llama_model = load_model()  # Solo se carga al primer uso real

    conversation = prompt_base + history
    conversation += f"\n<|user|>\n{user_input}\n<|assistant|>\n"
    response = llama_model(conversation, max_tokens=300)
    answer = response["choices"][0]["text"].strip()
    return answer, conversation + answer
