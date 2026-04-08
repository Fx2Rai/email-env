from server.email_env_environment import EmailEnv
from models import EmailAction

env = EmailEnv()

obs = env.reset()
print("Observation:", obs)

# try a sample action
action = EmailAction(
    classification="important",
    priority="high",
    reply="Sure, I will attend."
)

obs, reward, done, info = env.step(action)

print("Reward:", reward)
print("Done:", done)
print("Info:", info)