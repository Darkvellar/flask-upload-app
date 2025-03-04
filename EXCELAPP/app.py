from flask import Flask, request, jsonify
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para permitir requisições do frontend

    UPLOAD_FOLDER = "uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    @app.route("/", methods=["GET"])
    def home():
        return "Servidor Flask rodando!"

    @app.route("/upload", methods=["POST"])
    def upload_file():
        if "file" not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "Nenhum arquivo selecionado"}), 400

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        return jsonify({"message": f"Arquivo '{file.filename}' enviado!", "file_path": file_path}), 200

    return app  # Importante: Retorna a instância do app

# Configuração correta para rodar no Codespaces
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5501)
