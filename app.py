from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from question_generator import generate_questions

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    file = request.files["resume"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_text(filepath)
        questions = generate_questions(resume_text)

        return render_template("result.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)