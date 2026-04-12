# Animal Disease AI Chatbot

This project is an **AI chatbot module** from the main system:
https://github.com/pratik-singh-03/Animal-Disease-Detection-System

It can also be used **independently** to provide basic information about animal diseases.

---

## Features

* AI-based responses using OpenRouter API
* Structured answers (Definition, Causes, Symptoms, Prevention, Treatment)
* Simple web-based chat interface
* Lightweight and easy to run

---

## Tech Stack

* Flask (Python)
* HTML, Inline CSS, JavaScript
* OpenRouter API (LLMs)

---

## Setup

```bash
pip install flask requests
python app.py
```

Open: http://127.0.0.1:5000/

---

## API Key Setup

Before running the project, add your own OpenRouter API key in `app.py`:

```python
API_KEY = "YOUR_API_KEY"
```

Replace `"YOUR_API_KEY"` with your actual OpenRouter API key.

---

## Note

This chatbot provides general guidance only. Always consult a veterinarian.

---

## Author

Pratik Singh
