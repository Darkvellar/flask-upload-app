@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nome de arquivo inválido"}), 400

    # Salva o arquivo na pasta uploads
    upload_path = os.path.join("uploads", file.filename)
    file.save(upload_path)

    return jsonify({"message": f"Arquivo {file.filename} enviado com sucesso!"}), 200

