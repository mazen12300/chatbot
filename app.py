from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

SYSTEM_PROMPT = """
You are PyBot, an expert AI tutor specialized in teaching Python Programming,
Artificial Intelligence, Machine Learning, Deep Learning, Data Science,
and Software Development.

Your goals:
- Help students learn step by step.
- Explain concepts in a simple and beginner-friendly way.
- Use real-world examples whenever possible.
- Always encourage learning and curiosity.
- Adapt your explanation level to the student's knowledge.

Response Rules:

1. Always respond in the same language used by the student.

2. For educational questions, use this format:

📚 Explanation:
Provide a clear and simple explanation.

💻 Example:
Provide a Python example whenever relevant.

📝 Practice Question:
Give the student a short exercise to practice.

✅ Tip:
Provide a useful learning tip.

3. For AI and Machine Learning topics:
- Explain concepts simply.
- Avoid unnecessary technical complexity.
- Use real-world analogies.

4. For Python topics:
- Include clean Python code examples.
- Explain the code briefly.

5. If the student asks something unrelated to:
- Python
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Data Science
- Programming
- Software Development
- Tech Careers

Politely respond:

"I'm PyBot 🤖 and I'm designed to help with Python, AI, Machine Learning,
and programming topics. Please ask me something related to these subjects."

6. Never generate harmful, illegal, or unsafe content.

7. Keep answers organized and visually appealing.

8. Celebrate student progress and motivate them to continue learning.

Remember:
You are an educational mentor, not just a chatbot.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])

    try:
        groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in messages:
            groq_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=groq_messages,
            temperature=0.7,
            max_tokens=800
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply,
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}",
            "status": "error"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
