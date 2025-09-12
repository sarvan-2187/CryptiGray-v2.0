from flask import Flask, render_template, request, jsonify, send_from_directory
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static", template_folder="templates")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt-page")
def encrypt_page():
    return render_template("encrypt.html")

@app.route("/decrypt-page")
def decrypt_page():
    return render_template("decrypt.html")

@app.route("/pdf-page")
def pdf_page():
    return render_template("pdf-encrypt.html")

@app.route("/encrypt", methods=["POST"])
def encrypt_pdf():
    if "pdf" not in request.files:
        return jsonify({"error": "No PDF file uploaded"}), 400
    file = request.files["pdf"]
    password = request.form.get("password")
    if not password:
        return jsonify({"error": "Password is required"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    reader = PdfReader(filepath)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    out_filename = f"encrypted_{filename}"
    out_path = os.path.join(UPLOAD_FOLDER, out_filename)

    with open(out_path, "wb") as f:
        writer.write(f)

    return jsonify({"outputUrl": f"/download/{out_filename}"})

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
