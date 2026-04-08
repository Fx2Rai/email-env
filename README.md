---
title: Email Env AI
emoji: 📧
colorFrom: green
colorTo: green
sdk: docker
pinned: false
---

# 📧 Email Environment AI (OpenEnv Project)

## 🚀 Overview

This project implements a **real-world email assistant environment** using the OpenEnv framework.
It simulates how an AI agent processes emails and takes actions such as classification, prioritization, and generating replies.

The environment follows the standard:

* `reset()`
* `step()`
* reward-based evaluation

---

## 🎯 Features

* ✔ Real-world task: Email handling assistant
* ✔ 3 difficulty levels: Easy, Medium, Hard
* ✔ Reward-based evaluation (0.0 → 1.0)
* ✔ FastAPI backend
* ✔ Gradio UI interface
* ✔ Deployed on Hugging Face Spaces

---

## 🧠 Task Design

### 🔹 Easy

* Input: Email
* Task: Classify email
* Output: `spam / important / normal`

---

### 🔹 Medium

* Input: Email
* Task:

  * Classify email
  * Assign priority (`low / high`)

---

### 🔹 Hard

* Input: Email
* Task: Generate appropriate reply

---

## 🏆 Reward Function

| Task      | Condition              | Reward      |
| --------- | ---------------------- | ----------- |
| Easy      | Correct classification | 1.0         |
| Medium    | Both correct           | 1.0         |
| Medium    | One correct            | 0.5         |
| Hard      | Correct reply          | 1.0         |
| Otherwise | Incorrect              | 0.0 or -1.0 |

---

## ⚙️ Action Space

```json
{
  "classification": "spam | important | normal",
  "priority": "low | high",
  "reply": "text response"
}
```

---

## 👀 Observation Space

```json
{
  "email_text": "string",
  "sender": "string",
  "task_type": "easy | medium | hard"
}
```

---

## 🔄 Environment Flow

1. `reset()` → generates new email task
2. `step(action)` → evaluates agent action
3. returns:

   * observation
   * reward
   * done
   * info

---

## 🤖 Baseline Agent

A rule-based agent is implemented in `inference.py` that:

* Detects spam using keywords
* Identifies important emails (meetings)
* Generates simple replies

Average reward achieved: **~0.9**

---

## 🌐 Live Demo

👉 Hugging Face Space:
[Add your link here]

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Gradio
* Pydantic

---

## 📁 Project Structure

```
email-env/
├── app.py
├── models.py
├── inference.py
├── requirements.txt
├── openenv.yaml
├── server/
│   ├── email_env_environment.py
│   ├── app.py
│   └── __init__.py
```

---

## 💡 Future Improvements

* Add ML-based classification model
* Improve reply generation using NLP
* Add logging and analytics

---

## 🏁 Conclusion

This project demonstrates how AI agents can interact with structured environments using reward-based learning, simulating real-world applications like email automation.

---