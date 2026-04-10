---
title: Email Env AI
emoji: 🚀
colorFrom: green
colorTo: green
sdk: docker
app_port: 8000
pinned: false
---

---

title: Email Env AI
emoji: 📧
colorFrom: green
colorTo: blue
sdk: docker
app_port: 8000
pinned: false
-------------

# 📧 Email Env AI

🚀 An OpenEnv-based environment where an AI agent learns to handle real-world email tasks using reward-driven evaluation.

---

## 🌟 Overview

This project simulates a **real-world email assistant**.
An AI agent interacts with the environment by:

* Observing an email
* Taking an action
* Receiving a reward

The goal is to evaluate how well the agent performs realistic tasks like classification, prioritization, and reply generation.

---

## 🎯 Tasks (3 Required Tasks ✅)

The environment includes **three independent tasks with graders**:

### 1️⃣ Classify

* Classify email as:

  * `spam`
  * `important`
  * `normal`

### 2️⃣ Priority

* Determine:

  * classification
  * priority (`low / high`)

### 3️⃣ Reply

* Generate a suitable reply for the email

---

## 🔄 Task Execution Flow

Tasks are executed in a **cyclic order**:

```
classify → priority → reply → repeat
```

✔ Ensures all tasks are covered
✔ Required for OpenEnv validation

---

## 🏆 Reward System (Strictly (0,1) ✅)

All rewards are strictly between 0 and 1:

| Task     | Condition    | Reward |
| -------- | ------------ | ------ |
| Classify | Correct      | 0.9    |
| Classify | Incorrect    | 0.1    |
| Priority | Both correct | 0.9    |
| Priority | One correct  | 0.6    |
| Priority | Incorrect    | 0.1    |
| Reply    | Good reply   | 0.9    |
| Reply    | Partial      | 0.6    |
| Reply    | Weak/none    | 0.2    |

⚠️ No reward is 0.0 or 1.0 (required by evaluator)

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
  "task_type": "classify | priority | reply"
}
```

---

## 🔄 Environment Flow

1. `reset()` → generates new email + task
2. `step(action)` → evaluates agent action
3. returns:

   * observation
   * reward
   * done
   * info

---

## 🔌 API Endpoints

* `POST /reset` → get new observation
* `POST /step` → submit action

---

## 🤖 Agent (inference.py)

The agent is powered by an **LLM using OpenAI-compatible API**:

* Uses:

  * `API_BASE_URL`
  * `API_KEY`
* Generates structured JSON output
* Handles:

  * classification
  * priority
  * reply

---

## 🔑 Environment Variables

These are injected by the evaluator:

```bash
API_BASE_URL=<provided_by_evaluator>
API_KEY=<provided_by_evaluator>
```

⚠️ Do NOT hardcode these values

---

## ▶️ Quick Start (Local)

```bash
pip install -r requirements.txt

# Run server
uvicorn server.app:app --host 0.0.0.0 --port 8000

# Run agent
python inference.py
```

---

## 📁 Project Structure

```
email-env/
├── inference.py
├── models.py
├── server/
│   ├── app.py
│   ├── email_env_environment.py
│   └── __init__.py
├── openenv.yaml
├── requirements.txt
├── pyproject.toml
```

---

## 🌐 Deployment

Hugging Face Space:
👉 https://fabian9656-email-env.hf.space

---

## ✅ OpenEnv Compliance

✔ 3 tasks with graders
✔ Reward strictly within (0,1)
✔ LLM API usage via proxy
✔ Structured output `[START][STEP][END]`
✔ FastAPI environment

---

## 🚀 Future Improvements

* Add more email samples
* Improve reply generation quality
* Integrate fine-tuned models
* Add analytics and evaluation dashboard

---

## 🏁 Conclusion

This project demonstrates how **LLM-powered agents interact with structured environments using reward-based evaluation**, simulating real-world automation tasks like email handling.

---
