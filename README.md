# PyBot 🐍🤖
### Chatbot لتعليم Python و AI — مشروع التخرج

---

## خطوات التشغيل

### 1. ثبّت المكتبات
```bash
pip install flask anthropic
```

### 2. ضع الـ API Key
افتح ملف `app.py` وغيّر هذا السطر:
```python
client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")
```
إلى:
```python
client = anthropic.Anthropic(api_key="sk-ant-...")  # مفتاحك هنا
```

### 3. شغّل البرنامج
```bash
python app.py
```

### 4. افتح المتصفح
اذهب إلى: `http://localhost:5000`

---

## هيكل المشروع
```
chatbot/
├── app.py              # الـ Backend (Flask + Claude API)
├── requirements.txt    # المكتبات المطلوبة
├── README.md           # هذا الملف
└── templates/
    └── index.html      # واجهة الشات بوت
```

---

## المميزات
- ✅ يتعلم Python من الأساسيات للمتقدم
- ✅ يشرح مفاهيم AI و Machine Learning
- ✅ يدعم العربية والإنجليزية
- ✅ يعرض الكود بشكل منسق مع Syntax Highlighting
- ✅ يتذكر سياق المحادثة
- ✅ تصميم احترافي وسهل الاستخدام
