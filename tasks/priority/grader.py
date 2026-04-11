"""Grader for the priority task.

Evaluates whether the agent correctly classified the email
AND assigned the correct priority level. Returns a score between 0.0 and 1.0.
"""

from server.email_env_environment import EmailEnv
from models import EmailAction


def grade(action: dict, env_state: dict) -> float:
    """Grade the priority task.

    Args:
        action: The agent's action dictionary with 'classification' and 'priority' keys.
        env_state: The current environment state dictionary.

    Returns:
        A float score between 0.0 and 1.0.
    """
    correct_class = env_state.get("correct_classification", "").strip().lower()
    correct_priority = (env_state.get("correct_priority") or "").strip().lower()

    predicted_class = (action.get("classification") or "").strip().lower()
    predicted_priority = (action.get("priority") or "").strip().lower()

    class_correct = predicted_class == correct_class
    priority_correct = predicted_priority == correct_priority

    if class_correct and priority_correct:
        return 1.0
    elif class_correct or priority_correct:
        return 0.5
    return 0.0
