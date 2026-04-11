from fastapi import FastAPI
from server.email_env_environment import EmailEnv
from models import EmailAction

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    if hasattr(obs, "model_dump"):
        return obs.model_dump()
    return obs.dict()

@app.post("/step")
def step(action: EmailAction):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.model_dump() if hasattr(obs, "model_dump") else obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
@app.post("/state")
def state():
    s = env.get_state()
    if s is None:
        return {}
    if hasattr(s, "model_dump"):
        return s.model_dump()
    return s.dict()

def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()