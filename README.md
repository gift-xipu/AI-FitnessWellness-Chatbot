# **AI-Powered Fitness and Wellness Chatbot** 🏋️‍♂️🧘‍♀️🥗  

This project is designed to provide **personalized fitness, wellness, and recipe recommendations** using AI-driven chatbots.  

The application is built with **Python, FastAPI, LangChain, and OpenAI GPT-3.5**.

---

## **📌 Table of Contents**
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation & Setup](#installation--setup)  
4. [Usage](#usage)  
5. [API Endpoints](#api-endpoints)  
6. [Environment Variables](#environment-variables)  
7. [Testing](#testing)  
8. [Project Structure](#project-structure)  
9. [Dependencies](#dependencies)  
10. [License](#license)  

---

## **📖 Project Overview**  

This AI-powered chatbot provides **customized responses** in three key areas:  

✔️ **Fitness Chatbot** – Generates workout plans, nutrition tips, and motivational support based on user fitness goals (e.g., weight loss, muscle gain).  

✔️ **Mindfulness Chatbot** – Offers guidance on relaxation techniques, stress management, and sleep improvement.  

✔️ **Recipe Generator** – Creates **AI-generated** recipes based on user-inputted ingredients, dietary preferences, and meal types.  

---

## **✨ Features**  

✅ **AI-Driven Responses** – Uses **OpenAI GPT-3.5** for intelligent, personalized recommendations.  

✅ **Fast & Scalable API** – Built with **FastAPI**, ensuring speed and efficiency.  

✅ **Modular & Extensible** – Well-structured project with clearly defined services.  

✅ **Swagger UI Documentation** – Easily explore API endpoints using **Swagger UI**.  

---

## **🛠 Installation & Setup**  

### **Prerequisites**  
Before starting, ensure you have:  
🔹 **Python 3.8+** installed  
🔹 An **OpenAI API Key**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/ai_fitness_app.git
cd ai_fitness_app
```

### **2️⃣ Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**  
Create a `.env` file in the root directory and add the following:  
```plaintext
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-3.5-turbo
TEMPERATURE=0.7
MAX_TOKENS=150
```

### **5️⃣ Start the Application**  
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will now be accessible at:  
🔹 `http://127.0.0.1:8000`  

---

## **🚀 Usage**  

Once the server is running, you can interact with the chatbot via API requests.  

### **Swagger API Documentation**  
📌 Access interactive API docs:  
- **Swagger UI** → `http://127.0.0.1:8000/docs`  
- **Redoc UI** → `http://127.0.0.1:8000/redoc`  

---

## **📡 API Endpoints**  

| **Chatbot**    | **Endpoint**         | **Request Type** | **Description** |
|---------------|----------------------|-----------------|----------------|
| Fitness Chatbot | `/fitness`         | `POST`         | Get workout & nutrition advice |
| Mindfulness Chatbot | `/mindfulness` | `POST`         | Receive mindfulness tips |
| Recipe Generator | `/recipes`         | `POST`         | Generate personalized recipes |

### **Example API Request (Fitness Chatbot)**  
```bash
curl -X POST "http://127.0.0.1:8000/fitness" \
-H "Content-Type: application/json" \
-d '{"goal": "weight loss", "level": "beginner"}'
```

---

## **🌍 Environment Variables**  

The application requires the following environment variables (stored in `.env`):  

| **Variable**        | **Description**                                  | **Example Value** |
|--------------------|------------------------------------------------|----------------|
| `OPENAI_API_KEY`   | Your OpenAI API key                            | `sk-xxxxxx`   |
| `MODEL_NAME`       | OpenAI model used for chatbots                 | `gpt-3.5-turbo` |
| `TEMPERATURE`      | Controls randomness of responses               | `0.7`          |
| `MAX_TOKENS`      | Limits response length                          | `150`          |

---

## **🧪 Testing**  

To run tests, execute:  
```bash
python -m pytest tests/
```

This will perform unit tests for all chatbot functionalities.

---

## **📁 Project Structure**  

```
ai_fitness_app/
│── .env                  # Environment variables
│── .gitignore            # Ignore unnecessary files
│── main.py               # FastAPI entry point
│
├── models/               # Data models (Pydantic schemas)
│    ├── chat.py          # Chatbot request/response schemas
│
├── routes/               # API routes
│    ├── fitness.py       # Fitness chatbot API
│    ├── mindfulness.py   # Mindfulness chatbot API
│    ├── recipes.py       # Recipe generator API
│
├── services/             # Core chatbot logic
│    ├── chatbot.py       # Base chatbot functionality
│    ├── fitness_chat.py  # Fitness-specific logic
│    ├── mindful_chat.py  # Mindfulness logic
│    ├── recipe_gen.py    # Recipe generator logic
│
├── utils/                # Helper utilities
│    ├── config.py        # Environment config loader
│    ├── logger.py        # Logging setup
│
├── tests/                # Unit tests
│── requirements.txt      # Project dependencies
│── README.md             # Project documentation
```

---

## **📦 Dependencies**  

- **FastAPI** – High-performance web framework  
- **LangChain** – AI/LLM-powered chatbot framework  
- **OpenAI API** – Used for generating responses  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server for FastAPI  
- **Python-dotenv** – Environment variable management  

Install all dependencies with:  
```bash
pip install -r requirements.txt
```

---

## **📜 License**  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---
