from flask import Blueprint, request, jsonify
from app.services.llama_service import ask_guru
from app.services.ocr_service import extract_text_from_image, extract_text_from_pdf
from config import API_KEY
from werkzeug.utils import secure_filename
import os

guru_routes = Blueprint('guru_routes', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def require_api_key(f):
  def decorated(*args, **kwargs):
    api_key = request.headers.get('x-api-key')
    if api_key not in API_KEY:
      return jsonify({"error": "Unauthorized: API Key missing or invalid"}), 401
    return f(*args, **kwargs)
  decorated.__name__ = f.__name__
  return decorated

@guru_routes.route('/ask', methods=['POST'])
@require_api_key
def ask():
  data = request.json
  question = data.get("question", "")
  history = data.get("history", "")
  answer, updated_history = ask_guru(question, history)

  clean_answer = answer.replace("\\n", "\n").replace('\\"', '"').strip()
  clean_history = updated_history.replace("\\n", "\n").replace('\\"', '"').strip()

  return jsonify({"answer": clean_answer, "history": clean_history})

@guru_routes.route('/ocr', methods=['POST'])
@require_api_key
def ocr():
  if 'file' not in request.files:
    return jsonify({"error": "No file part in the request"}), 400
  
  file = request.files['file']
  filename = secure_filename(file.filename)
  ext = filename.rsplit('.', 1)[1].lower()
  
  if ext not in ALLOWED_EXTENSIONS:
    return jsonify({"error": "File type not allowed"}), 400
  
  filepath = os.path.join('temp', filename)
  os.makedirs('temp', exist_ok=True)
  file.save(filepath)
  
  try:
    if ext == 'pdf':
      text = extract_text_from_pdf(filepath)
    else:
      text = extract_text_from_image(filepath)
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  finally:
    os.remove(filepath)
    
  return jsonify({"text": text})