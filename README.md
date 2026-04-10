---
title: Email Env AI
emoji: 🚀
colorFrom: green
colorTo: green
sdk: docker
app_port: 8000
pinned: false
---

# 📧 Email Env AI (OpenEnv Project)

🚀 A reinforcement-learning style email assistant environment built using OpenEnv + LLM integration.

---

## 🌟 Overview

This project simulates a **real-world email assistant agent** that:

* Classifies emails (spam / important / normal)
* Assigns priority (low / high)
* Generates replies for messages

It is designed for **agent-based evaluation using OpenEnv**, where actions are scored using a reward system.

---

## ⚡ Key Features

* ✅ 3 difficulty levels (easy, medium, hard)
* ✅ Reward-based evaluation (0.0 → 1.0)
* ✅ FastAPI environment server
* ✅ LLM-powered agent (via OpenAI-compatible API)
* ✅ Hugging Face Spaces deployment

---

## 🧠 Task Design

### 🔹 Easy

* Input: Email
* Output: Classification (`spam / important / normal`)

### 🔹 Medium

* Input: Email
* Output:

  * Classification
  * Priority (`low / high`)

### 🔹 Hard

* Input: Email
* Output: Reply generation

---

## 🏆 Reward System

| Task   | Condition              | Reward |
| ------ | ---------------------- | ------ |
| Easy   | Correct classification | 1.0    |
| Medium | Both correct           | 1.0    |
| Medium | One correct            | 0.5    |
| Hard   | Correct reply          | 1.0    |
| Other  | Incorrect / missing    | 0.0/-1 |

---

## ⚙️ Action Format

```json
{
  "classification": "spam | important | normal",
  "priority": "low | high",
  "reply": "text response"
}
```

---

## 👀 Observation Format

```json
{
  "email_text": "string",
  "sender": "string",
  "task_type": "easy | medium | hard"
}
```

---

## 🔄 Environment Flow

1. `reset()` → generates a new email
2. `step(action)` → evaluates agent action
3. returns:

   * observation
   * reward
   * done
   * info

---

## 🤖 Agent (inference.py)

This project uses an **LLM-based agent**:

* Uses OpenAI-compatible API
* Generates structured JSON output
* Handles:

  * classification
  * priority
  * reply generation

---

## 🔑 Environment Variables (IMPORTANT)

This project depends on runtime-injected variables:

```bash
API_BASE_URL=<provided_by_evaluator>
API_KEY=<provided_by_evaluator>
```

⚠️ Do NOT hardcode keys.

---

## ▶️ Quick Start (Local)

```bash
pip install -r requirements.txt

# run environment
uvicorn server.app:app --host 0.0.0.0 --port 8000

# run agent
python inference.py
```

---

## 📡 API Endpoints

* `POST /reset` → get new email
* `POST /step` → submit action

---

## 📁 Project Structure

```
email-env/
├── inference.py        # agent logic
├── models.py          # Pydantic models
├── server/
│   ├── app.py         # FastAPI server
│   ├── email_env_environment.py
│   └── __init__.py
├── openenv.yaml
├── requirements.txt
```

---

## 🌐 Deployment

👉 Hugging Face Space:
https://fabian9656-email-env.hf.space

---

## 💡 Future Improvements

* Improve LLM prompting strategy
* Add fine-tuned model
* Expand dataset
* Add logging & metrics

---

## 🏁 Conclusion

This project demonstrates how LLM-powered agents can interact with structured environments using reward-based evaluation — a key step toward real-world autonomous systems.

---
