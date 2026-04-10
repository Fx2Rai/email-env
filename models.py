from pydantic import BaseModel
from typing import Optional


# 👀 What AI sees
class EmailObservation(BaseModel):
    email_text: str
    sender: str
    task_type: str   # classify / priority / reply 


# 🎮 What AI does
class EmailAction(BaseModel):
    classification: Optional[str] = None   # spam / important / normal
    priority: Optional[str] = None         # high / medium / low
    reply: Optional[str] = None            # generated reply


# 🧠 Internal state
class EmailState(BaseModel):
    current_email: EmailObservation
    correct_classification: str
    correct_priority: Optional[str] = None
    expected_reply: Optional[str] = None
    step_count: int = 0