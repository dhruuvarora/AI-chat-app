# AI Chat App

A simple AI-powered chatbot backend built with **FastAPI** and **Groq API**. This project demonstrates how to build a REST API that accepts user prompts, sends them to a Large Language Model (LLM), and returns AI-generated responses.

---

## Features

* FastAPI backend
* Groq API integration
* RESTful API endpoints
* Environment variable support using `.env`
* Request validation using Pydantic
* Interactive Swagger UI
* Easy to extend for future AI applications

---

## Tech Stack

* Python
* FastAPI
* Groq API
* Pydantic
* Python Dotenv
* Uvicorn

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhruuvarora/AI-chat-app.git
cd AI-chat-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` File

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET /

Returns the status of the API.

#### Response

```json
{
  "message": "Hello, World!"
}
```

---

### POST /chat

Sends a prompt to the AI model and returns an AI-generated response.

#### Request

```json
{
  "message": "Explain FastAPI."
}
```

#### Response

```json
{
  "response": "FastAPI is a modern Python web framework..."
}
```

---

## Project Structure

```text
AI-chat-app/
│
├── app/
│   └── main.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── test.py
```

---

## Future Improvements

* Add conversation history
* Support streaming responses
* Add authentication and authorization
* Dockerize the application
* Integrate a React frontend
* Support multiple AI models
* Store chat history in a database

---

## Author

**Dhruv Arora**

GitHub: https://github.com/dhruuvarora
