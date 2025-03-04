from flask import Flask, request, jsonify
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for frontend requests

    # Create the uploads folder if it doesn't exist
    UPLOAD_FOLDER = "uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    @app.route("/", methods=["GET"])
    def home():
        return "Servidor Flask rodando!"

    @app.route("/upload", methods=["GET", "POST"])
    def upload_file():
        if request.method == "GET":
            return "Upload endpoint ativo! Use POST para enviar arquivos."
        
        if "file" not in request.files:
            return jsonify({"error": "Nenhum arquivo foi enviado"}), 400
        
        file = request.files["file"]
        
        if file.filename == "":
            return jsonify({"error": "Nenhum arquivo selecionado"}), 400

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        return jsonify({
            "message": f"Arquivo '{file.filename}' enviado com sucesso!",
            "file_path": file_path
        }), 200

    return app  # Return the app instance

# ✅ Call create_app() before running Flask
if __name__ == "__main__":
    app = create_app()  # Fix: Create the Flask app
    app.run(debug=True, host="0.0.0.0", port=5501)
