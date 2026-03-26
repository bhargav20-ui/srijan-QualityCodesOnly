from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import random
import os

# 🔐 Secure API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# 🟦 PROJECTS API
@api_view(['GET'])
def projects(request):
    return Response([
        {
            "project_id": "PROJ-1",
            "project_name": "Online Shopping App",
            "description": "E-commerce platform for browsing, cart, and payments.",
            "features": [
                {
                    "feature_id": "JIRA-101",
                    "title": "Login",
                    "description": "User can login using email and password",
                    "priority": "High"
                },
                {
                    "feature_id": "JIRA-102",
                    "title": "Add to Cart",
                    "description": "User can add products to cart",
                    "priority": "Medium"
                },
                {
                    "feature_id": "JIRA-103",
                    "title": "Payment",
                    "description": "User can complete payment securely",
                    "priority": "High"
                }
            ]
        },
        {
            "project_id": "PROJ-2",
            "project_name": "Mental Health Chatbot",
            "description": "AI chatbot for mental wellness support.",
            "features": [
                {
                    "feature_id": "JIRA-201",
                    "title": "Login",
                    "description": "User login for chatbot access",
                    "priority": "Medium"
                },
                {
                    "feature_id": "JIRA-202",
                    "title": "Chatbot Interaction",
                    "description": "Chatbot responds intelligently",
                    "priority": "High"
                }
            ]
        },
        {
            "project_id": "PROJ-3",
            "project_name": "Notes Sharing App",
            "description": "Collaborative notes platform.",
            "features": [
                {
                    "feature_id": "JIRA-301",
                    "title": "Login",
                    "description": "User login to access notes",
                    "priority": "Medium"
                },
                {
                    "feature_id": "JIRA-302",
                    "title": "Add/Delete Notes",
                    "description": "User can create and delete notes",
                    "priority": "Medium"
                },
                {
                    "feature_id": "JIRA-303",
                    "title": "Share Notes",
                    "description": "User can share notes with others",
                    "priority": "High"
                }
            ]
        }
    ])


# 🤖 AI GENERATION (IMPROVED 🔥)
def generate_ai_tests(description):
    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = f"""
You are a senior QA engineer.

User story:
{description}

Generate STRICT JSON only.

Requirements:
- Generate 8-12 test cases for each category
- Make them detailed and realistic
- Include:
  - Validation cases
  - Boundary cases
  - Security cases (SQL injection, XSS)
  - Performance scenarios
- Avoid generic sentences

Format:
{{
  "analysis": {{
    "feature": "{description}",
    "inputs": ["email", "password"],
    "expected": "expected behavior"
  }},
  "positive": [],
  "negative": [],
  "edge": [],
  "risk": "Low/Medium/High",
  "confidence": 80
}}
"""

    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception:
        return json.dumps({
            "analysis": {},
            "positive": ["Valid login with correct credentials"],
            "negative": ["Invalid password should fail"],
            "edge": ["Empty input handled"],
            "risk": "Medium",
            "confidence": 70
        })


# 🧪 EXECUTION SIMULATION
def execute_tests(test_cases):
    execution_details = []
    passed = 0
    failed = 0

    for test in test_cases:
        if "invalid" in test.lower() or "fail" in test.lower():
            status = "Failed"
        else:
            status = random.choice(["Passed", "Passed", "Failed"])

        execution_details.append({
            "test": test,
            "status": status,
            "time": random.randint(20, 200),
            "browser": "Chrome",
            "error": "-" if status == "Passed" else "Assertion failed"
        })

        if status == "Passed":
            passed += 1
        else:
            failed += 1

    total = len(test_cases)
    pass_rate = (passed / total) * 100 if total > 0 else 50

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "details": execution_details,
        "pass_rate": pass_rate
    }


# 🔥 MAIN API
@api_view(['POST'])
def generate_tests(request):

    description = request.data.get("description")

    if not description:
        return Response({"error": "No description provided"}, status=400)

    try:
        ai_response = generate_ai_tests(description)

        try:
            data = json.loads(ai_response)
        except:
            data = {}

        # ✅ FALLBACKS
        positive = data.get("positive") or ["Valid input works"] * 8
        negative = data.get("negative") or ["Invalid input fails"] * 8
        edge = data.get("edge") or ["Edge case handled"] * 8

        risk = data.get("risk", "Medium")

        all_tests = positive + negative + edge

        # 🎯 INITIAL CONFIDENCE
        if risk == "High":
            base_conf = 60
        elif risk == "Medium":
            base_conf = 75
        else:
            base_conf = 85

        initial_confidence = min(base_conf + len(all_tests), 95)

        # 🧪 EXECUTION
        execution = execute_tests(all_tests)

        # 📊 FINAL CONFIDENCE
        final_confidence = int(
            (initial_confidence * 0.6) +
            (execution["pass_rate"] * 0.4)
        )

        # 🎯 PRIORITY
        if final_confidence < 60 or risk == "High":
            priority = "Critical"
        elif final_confidence < 80:
            priority = "Moderate"
        else:
            priority = "Low"

        return Response({
            "analysis": data.get("analysis", {}),
            "test_cases": {
                "positive": positive,
                "negative": negative,
                "edge": edge
            },
            "risk": risk,
            "initial_confidence": f"{initial_confidence}%",
            "final_confidence": f"{final_confidence}%",
            "priority": priority,
            "execution": execution
        })

    except Exception as e:
        return Response({
            "error": "Processing failed",
            "details": str(e)
        }, status=500)