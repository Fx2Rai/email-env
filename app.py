import gradio as gr
from server.email_env_environment import EmailEnv
from models import EmailAction   

env = EmailEnv()

def reset_env():
    obs = env.reset()
    return obs.dict()

def take_step(classification, priority, reply):
    action = {
        "classification": classification,
        "priority": priority,
        "reply": reply
    }

    action_obj = EmailAction(**action)

    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

with gr.Blocks() as demo:
    gr.Markdown("# 📧 Email Environment UI")

    with gr.Row():
        reset_btn = gr.Button("Reset Environment")
        reset_output = gr.JSON()

    reset_btn.click(fn=reset_env, outputs=reset_output)

    gr.Markdown("## Take Action")

    classification = gr.Textbox(label="Classification")
    priority = gr.Textbox(label="Priority")
    reply = gr.Textbox(label="Reply")

    step_btn = gr.Button("Submit Action")
    step_output = gr.JSON()

    step_btn.click(
        fn=take_step,
        inputs=[classification, priority, reply],
        outputs=step_output
    )

demo.launch()