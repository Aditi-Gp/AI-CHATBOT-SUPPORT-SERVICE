# AI Chatbot Support Service

An AI-powered chatbot support system built using **Python, Flask, and Cohere API** that enables users to interact with a chatbot through a frontend interface and receive intelligent responses in real time.

## Features
- Real-time chatbot interaction
- Backend built with Flask
- Cohere LLM integration for response generation
- REST API for frontend-backend communication
- CORS enabled for cross-origin requests
- Error handling for failed requests
- Lightweight frontend hosting using Python HTTP server

---

## Tech Stack
- **Backend:** Python, Flask
- **AI Model:** Cohere API (`command-xlarge`)
- **Frontend:** HTML/CSS/JavaScript
- **Libraries Used:**
  - Flask
  - Flask-CORS
  - Cohere
  - Matplotlib

---

## Project Structure
```bash
chatbot_project/
│
├── server.py          # Flask backend server
├── index.html         # Frontend chatbot UI
├── static/            # CSS/JS files (if applicable)
├── templates/         # HTML templates (if applicable)
├── requirements.txt   # Python dependencies
└── README.md
````



## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-CHATBOT-SUPPORT-SERVICE.git
cd chatbot_project
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
```

#### For Windows:

```bash
venv\Scripts\activate
```

#### For Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Replace the Cohere API key in `server.py`:

```python
cohere_api_key = "YOUR_API_KEY"
```

**Recommended:** Store API keys using environment variables instead of hardcoding them.

Example:

```bash
export COHERE_API_KEY=your_key
```

---

## Running the Project

### Terminal 1: Start Flask Backend

```bash
cd chatbot_project
venv\Scripts\activate
python server.py
```

Backend runs on:

```bash
http://localhost:8000
```

---

### Terminal 2: Start Frontend Server

```bash
cd chatbot_project
venv\Scripts\activate
python -m http.server 8080
```

Frontend runs on:

```bash
http://localhost:8080
```

---

## API Endpoints

### Home Route

```http
GET /
```

Returns:

```json
Welcome to the chatbot server!
```

---

### Chat Route

```http
POST /chat
```

#### Request Body

```json
{
  "message": "Hello chatbot"
}
```

#### Response

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## Workflow

1. User enters a message on frontend UI
2. Frontend sends request to Flask backend
3. Backend processes request
4. Cohere model generates response
5. Response is returned to frontend

---

## Future Improvements

* Add user authentication
* Store conversation history
* Deploy on cloud platforms
* Integrate advanced LLMs
* Add multilingual support
* Improve frontend UI

---

## Learning Outcomes

This project helped in understanding:

* API development with Flask
* LLM integration
* Frontend-backend communication
* Error handling
* AI application deployment basics

---

## License

This project is for educational and learning purposes.

```
```
