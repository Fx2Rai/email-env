import os
import json
from openai import OpenAI
from server.email_env_environment import EmailEnv
from models import EmailAction

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o-mini")


def act(observation):
    try:
        text = observation["email_text"]
        task_type = observation.get("task_type", "classify")

        prompt = f"""
You are an email assistant.
Task: {task_type}
Email: {text}

Based on the task, respond with ONLY valid JSON. No explanation.
Format:
{{
  "classification": "spam | important | normal",
  "priority": "low | high",
  "reply": "your reply"
}}
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
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
        except Exception:
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


def run_task(env, task_name, episodes=3):
    """Run a single task for the given number of episodes and emit structured logs."""
    total_reward = 0

    print(f"[START] task={task_name}", flush=True)

    for step_num in range(episodes):
        obs = env.reset()

        # Force the task type to the one we want
        obs.task_type = task_name
        env.state.current_email.task_type = task_name

        if hasattr(obs, "model_dump"):
            obs_dict = obs.model_dump()
        else:
            obs_dict = obs.dict()

        action_dict = act(obs_dict)
        action = EmailAction(**action_dict)

        obs, reward, done, info = env.step(action)
        total_reward += reward

        print(f"[STEP] step={step_num + 1} reward={reward}", flush=True)

    avg_score = total_reward / episodes

    print(f"[END] task={task_name} score={avg_score} steps={episodes}", flush=True)

    return avg_score


def run():
    env = EmailEnv()
    episodes_per_task = 3

    # Run each task separately so the validator sees 3 tasks with graders
    tasks = ["classify", "priority", "reply"]

    for task_name in tasks:
        run_task(env, task_name, episodes=episodes_per_task)


if __name__ == "__main__":
    run()