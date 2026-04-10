from typing import Tuple
import random

from models import EmailObservation, EmailAction, EmailState


class EmailEnv:

    def __init__(self):
        self.state = None

        self.samples = [
            {
                "email": "Win a free iPhone now!",
                "sender": "spam@ads.com",
                "classification": "spam"
            },
            {
                "email": "Meeting at 5pm today",
                "sender": "boss@company.com",
                "classification": "important",
                "priority": "high",
                "reply": "Sure, I will attend the meeting."
            },
            {
                "email": "Let's catch up sometime",
                "sender": "friend@gmail.com",
                "classification": "normal",
                "priority": "low",
                "reply": "Sounds good, let's plan soon!"
            }
        ]

    def reset(self) -> EmailObservation:
        sample = random.choice(self.samples)

        task_type = random.choice(["classify", "priority", "reply"])

        observation = EmailObservation(
            email_text=sample["email"],
            sender=sample["sender"],
            task_type=task_type
        )

        self.state = EmailState(
            current_email=observation,
            correct_classification=sample["classification"],
            correct_priority=sample.get("priority"),
            expected_reply=sample.get("reply"),
            step_count=0
        )

        return observation

    def step(self, action: EmailAction):

        reward = 0.1   # default safe value
        done = True

        task = self.state.current_email.task_type

        if task == "classify":
            if (action.classification or "").strip().lower() == self.state.correct_classification.strip().lower():
                reward = 0.9
            else:
                reward = 0.1

        elif task == "priority":
            correct_class = (action.classification or "").strip().lower() == self.state.correct_classification.strip().lower()
            correct_priority = (action.priority or "").strip().lower() == (self.state.correct_priority or "").strip().lower()

            if correct_class and correct_priority:
                reward = 0.9
            elif correct_class or correct_priority:
                reward = 0.6
            else:
                reward = 0.1

        elif task == "reply":
            if self.state.expected_reply:
                if action.reply and self.state.expected_reply.lower() in action.reply.lower():
                    reward = 0.9
                elif action.reply:
                    reward = 0.6
                else:
                    reward = 0.2
            else:
                    reward = 0.2

        info = {
            "task": task,
            "correct_classification": self.state.correct_classification,
            "correct_priority": self.state.correct_priority,
            "expected_reply": self.state.expected_reply
        }

        return self.state.current_email, reward, done, info

    def get_state(self) -> EmailState:
        return self.state