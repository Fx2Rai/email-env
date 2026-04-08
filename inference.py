from server.email_env_environment import EmailEnv

def act(observation):
    try:
        text = observation["email_text"].lower()

        if "win" in text or "free" in text or "offer" in text:
            return {
                "classification": "spam",
                "priority": "low",
                "reply": ""
            }

        if "meeting" in text or "urgent" in text:
            return {
                "classification": "important",
                "priority": "high",
                "reply": "Sure, I will attend."
            }

        return {
            "classification": "normal",
            "priority": "low",
            "reply": "Sounds good, let's plan soon!"
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
        obs_dict = obs.dict()

        action = act(obs_dict)

        obs, reward, done, info = env.step(action)
        total_reward += reward

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

    avg_score = total_reward / episodes

    print(f"[END] task=email_env score={avg_score} steps={episodes}", flush=True)


if __name__ == "__main__":
    run()