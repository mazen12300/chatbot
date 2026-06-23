from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_reply(user_message):
    msg = user_message.lower()

    if "hello" in msg or "hi" in msg or "ازيك" in msg or "السلام" in msg:
        return "Hi! أنا PyBot 🤖 أقدر أساعدك تتعلم Python و AI خطوة بخطوة."

    elif "python" in msg or "بايثون" in msg:
        return """Python is a simple programming language used in AI, websites, apps, and data analysis.

Example:
```python
print("Hello, Python!")
```"""

    elif "variable" in msg or "متغير" in msg:
        return """A variable is used to store data.

Example:
```python
name = "Ahmed"
age = 20
print(name)
```"""

    elif "loop" in msg or "for" in msg or "لوب" in msg:
        return """A loop repeats code many times.

Example:
```python
for i in range(5):
    print(i)
```"""

    elif "function" in msg or "دالة" in msg:
        return """A function is a block of code that runs when you call it.

Example:
```python
def say_hello():
    print("Hello!")

say_hello()
```"""

    elif "ai" in msg or "artificial intelligence" in msg or "ذكاء" in msg:
        return "AI means making computers learn and make decisions like humans. Example: chatbots, face recognition, and self-driving cars."

    elif "machine learning" in msg or "ml" in msg:
        return "Machine Learning is a part of AI where computers learn from data instead of being programmed step by step."

    elif "neural network" in msg or "شبكة عصبية" in msg:
        return "A neural network is an AI model inspired by the human brain. It learns patterns from data."

    else:
        return """I can help you learn Python and AI 🐍🤖

Ask me about:
- Python
- variables
- loops
- functions
- AI
- machine learning
- neural networks"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])

    user_message = messages[-1]["content"]
    reply = get_bot_reply(user_message)

    return jsonify({
        'reply': reply,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True)