import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "email-agent")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

from server.email_env_environment import EmailEnv
from models import EmailAction


def smart_agent(obs):
    text = obs.email_text.lower()

    if "free" in text:
        classification = "spam"
    elif "meeting" in text:
        classification = "important"
    else:
        classification = "normal"

    if classification == "important":
        priority = "high"
    else:
        priority = "low"

    if classification == "important":
        reply = "Sure, I will attend the meeting."
    else:
        reply = "Sounds good, let's plan soon!"

    return EmailAction(
        classification=classification,
        priority=priority,
        reply=reply
    )


def run_agent():
    env = EmailEnv()

    total_reward = 0
    episodes = 10

    print("START")

    for i in range(episodes):
        obs = env.reset()

        action = smart_agent(obs)   

        obs, reward, done, info = env.step(action)

        total_reward += reward      

        print("STEP")
        print({
            "email": obs.email_text,
            "task": obs.task_type,
            "action": action.dict(),
            "reward": reward
        })

    print("END")
    print("Average Reward:", total_reward / episodes)


if __name__ == "__main__":
    run_agent()