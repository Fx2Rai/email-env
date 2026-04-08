from fastapi import FastAPI
from server.email_env_environment import EmailEnv
from server.models import EmailAction

app = FastAPI()

env = EmailEnv()

@app.get("/")
def root():
    return {"message": "Email Env Running 🚀"}

@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    action_obj = EmailAction(**action)

    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }