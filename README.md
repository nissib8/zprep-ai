# 🚀 ZPrep AI

An AI-powered interview preparation platform that generates personalized interview questions from uploaded resumes using **Google Gemini API**.

## 📌 Overview

ZPrep AI helps students and job seekers prepare for interviews by analyzing their resumes and generating tailored:

* HR Interview Questions
* Technical Interview Questions
* Project-Based Questions

Built with **Flask**, **Python**, and **Google Gemini API**, the platform provides a simple and intuitive interface for personalized interview preparation.

---

## ✨ Features

* 📄 Upload Resume (PDF)
* 🤖 AI-generated interview questions
* 👨‍💼 HR Questions
* 💻 Technical Questions
* 📚 Project-related Questions
* 🎨 Responsive and aesthetic UI
* 🔐 Secure API key management with `.env`

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### AI

* Google Gemini API

### PDF Processing

* PyPDF2

### Environment Management

* python-dotenv

---

## 📂 Project Structure

```text
zprep-ai/
│
├── app.py
├── question_generator.py
├── resume_parser.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── uploads/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/nissib8/zprep-ai.git
cd zprep-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🚀 Future Enhancements

* 🎤 AI Mock Interview Mode
* ⭐ Answer Evaluation and Scoring
* 📊 Performance Dashboard
* 📄 PDF Report Generation
* 💾 Question History
* 🧠 DSA and Behavioral Interview Modes
* 🎙️ Voice-Based Interviews
* 🌐 Streamlit Version

---

## 👩‍💻 Author

**Nissi Mylabathula**

Final Year B.Tech CSE Student

---

⭐ If you found this project useful, consider giving it a star!
