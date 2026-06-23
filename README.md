# 🐍🤖 PyBot – AI-Powered Python Learning Assistant




\

## 📖 Overview

PyBot is an intelligent educational chatbot designed to help students learn Python Programming and Artificial Intelligence through interactive conversations.

The chatbot acts as a virtual tutor that explains programming concepts, provides code examples, answers technical questions, and helps beginners build a strong foundation in Python and AI.

This project was developed as a Graduation Project to demonstrate the integration of Artificial Intelligence with modern web technologies for educational purposes.

---

## 🎯 Objectives

* Make Python learning easier for beginners.
* Simplify Artificial Intelligence concepts.
* Provide interactive learning experiences.
* Offer instant educational support.
* Encourage self-learning and practice.

---

## ✨ Features

### 🐍 Python Learning

* Variables & Data Types
* Operators
* Conditional Statements
* Loops
* Functions
* Lists & Dictionaries
* Object-Oriented Programming (OOP)
* Error Handling
* File Handling

### 🤖 Artificial Intelligence Learning

* AI Fundamentals
* Machine Learning Basics
* Deep Learning Concepts
* Neural Networks
* Data Science Introduction
* AI Applications

### 💬 Interactive Chatbot

* Real-time conversation
* Educational responses
* Beginner-friendly explanations
* Python code examples
* Practice exercises
* Learning tips

### 🎨 User Interface

* Modern Dark Theme
* Responsive Design
* Mobile Friendly
* Syntax Highlighting
* Interactive Suggestions

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Frontend (HTML/CSS/JavaScript)
 │
 ▼
Flask Backend
 │
 ▼
Groq API
 │
 ▼
Llama 3 Model
 │
 ▼
Educational Response
```

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### AI

* Groq API
* Llama 3.3 70B / Llama 3.1

### Libraries

* Flask
* Groq
* Marked.js
* Highlight.js

---

## 📂 Project Structure

```text
PyBot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/PyBot.git
cd PyBot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_API_KEY_HERE
```

### 6. Run Application

```bash
python app.py
```

### 7. Open Browser

```text
http://127.0.0.1:5000
```

---

## 🚀 Example Usage

### User Question

```text
What is a Python function?
```

### PyBot Response

```text
📚 Explanation:
A function is a reusable block of code that performs a specific task.

💻 Example:

def greet():
    print("Hello!")

greet()

📝 Practice Question:
Create a function that prints your name.

✅ Tip:
Functions help organize and reuse code.
```

---

## 🔮 Future Enhancements

* User Authentication
* Learning Progress Tracking
* Quiz & Assessment Module
* Voice Interaction
* Arabic Voice Support
* Personalized Learning Paths
* Database Integration
* Dashboard Analytics
* PDF Notes Generator

---

## 👨‍💻 Authors

**Mazen and Karam zayan**

Computer Science Department

Helwan National University

Graduation Project – 2026

---

## 📜 License

This project was developed for educational and academic purposes.

this project was created by Mazen and Karam zayan
