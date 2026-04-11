import os
import json
from openai import OpenAI
from server.email_env_environment import EmailEnv
from models import EmailAction

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

def act(observation):
    try:
        text = observation["email_text"]

        prompt = f"""
You are an email assistant.

Classify the email and generate a reply.

Email: {text}

Return ONLY valid JSON. No explanation.

Format:
{{
  "classification": "spam | important | normal",
  "priority": "low | high",
  "reply": "your reply"
}}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content

        # Extract JSON safely
        try:
            start = output.find("{")
            end = output.rfind("}") + 1
            json_str = output[start:end]
            return json.loads(json_str)
        except:
            return {
                "classification": "normal",
                "priority": "low",
                "reply": "Sorry, something went wrong."
            }

    except Exception:
        return {
            "classification": "normal",
            "priority": "low",
            "reply": "Sorry, something went wrong."
        }


def run():
    env = EmailEnv()
    total_reward = 0
    episodes = 3

    print("[START] task=email_env", flush=True)

    for step in range(episodes):
        obs = env.reset()

        if hasattr(obs, "model_dump"):
            obs_dict = obs.model_dump()
        else:
            obs_dict = obs.dict()

        action_dict = act(obs_dict)
        action = EmailAction(**action_dict)

        obs, reward, done, info = env.step(action)
        total_reward += reward

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

    avg_score = total_reward / episodes

    print(f"[END] task=email_env score={avg_score} steps={episodes}", flush=True)


if __name__ == "__main__":
    run()