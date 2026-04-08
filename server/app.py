from fastapi import FastAPI
from server.email_env_environment import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

from models import EmailAction

@app.post("/step")
def step(action: EmailAction):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }