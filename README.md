# 🚀 AI Testing Dashboard – Backend

## 🌐 Live Links

- 🔗 Backend (Deployed): (https://srijan-qualitycodesonly.onrender.com)
- 🔗 Frontend (Deployed): (https://srijan-quality-codes-only.vercel.app/) 
- 🔗 Frontend GitHub Repository: (https://github.com/kamalsushank/srijan-QualityCodesOnly)  

---

## 📌 Overview

The **AI Testing Dashboard Backend** powers an intelligent testing system that automates test case generation, execution simulation, and risk analysis.

It acts as the core engine that:
- Provides project and feature data
- Integrates with AI models
- Generates structured test cases
- Simulates execution results
- Calculates confidence and priority levels

---

## 🎯 Problem We Are Solving

Traditional testing workflows face several challenges:

- Manual test case creation is slow  
- Inconsistent risk assessment  
- Limited visibility into feature reliability  
- Lack of intelligent automation  

### ❗ Our Goal

To build a backend system that:
- Automates test generation using AI  
- Provides real-time insights  
- Simulates execution intelligently  
- Helps teams make faster decisions  

---

## ⚙️ What This Backend Does

This backend enables a complete AI-driven testing pipeline:

### 🔹 Project & Feature Management
- Provides predefined projects
- Each project contains multiple features (user stories)

### 🔹 AI-Based Test Generation
- Uses LLM APIs (OpenRouter / GPT models)
- Generates:
  - Positive test cases  
  - Negative test cases  
  - Edge cases  
  - Risk level  
  - Initial confidence  

### 🔹 Execution Simulation
- Simulates test execution results
- Provides:
  - Pass/Fail status  
  - Execution details (time, browser, etc.)  

### 🔹 Confidence Calculation
- Initial confidence based on:
  - Risk level  
  - Test coverage  

- Final confidence based on:
  - Execution results  
  - Pass rate  

### 🔹 Priority Detection
- Automatically categorizes features into:
  - Critical  
  - Moderate  
  - Low  

---

## 🧠 How It Works

### 🔹 API Flow

1. **GET /api/projects/**
   - Returns list of projects and features

2. **POST /api/generate/**
   - Accepts feature description
   - Calls AI model
   - Generates test cases
   - Simulates execution
   - Returns full analysis

---

## 💡 Why This Is Useful

### 👨‍💻 Developers
- Quickly identify risky features  
- Reduce manual testing effort  

### 🧪 Testers
- Get structured test cases instantly  
- Focus on critical failures  

### 📊 Teams / Managers
- Use confidence scores for decision-making  
- Prioritize releases effectively  

---

## 📈 Key Features

- AI-powered test generation  
- Risk-based analysis  
- Dynamic confidence scoring  
- Execution simulation engine  
- Structured API responses  
- Scalable architecture  

---

## 🚀 Future Improvements

- 🔗 Real Jira API integration  
- 🧪 Real Selenium execution  
- 📊 Historical analytics & trends  
- 🔐 Authentication & role-based access  
- ☁️ Deployment with Docker & CI/CD  
- 🧠 Advanced AI tuning for better accuracy  

---

## 🛠️ Tech Stack

- Python  
- Django  
- Django REST Framework  
- OpenRouter API (LLM)  
- JSON-based API architecture  

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone (https://github.com/bhargav20-ui/srijan-QualityCodesOnly)
cd srijan-QualityCodesOnly
