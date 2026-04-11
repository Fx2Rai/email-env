"""Grader for the classify task.

Evaluates whether the agent correctly classified the email
as spam, important, or normal. Returns a score between 0.0 and 1.0.
"""

from server.email_env_environment import EmailEnv
from models import EmailAction


def grade(action: dict, env_state: dict) -> float:
    """Grade the classify task.

    Args:
        action: The agent's action dictionary with 'classification' key.
        env_state: The current environment state dictionary.

    Returns:
        A float score between 0.0 and 1.0.
    """
    correct = env_state.get("correct_classification", "").strip().lower()
    predicted = (action.get("classification") or "").strip().lower()

    if predicted == correct:
        return 1.0
    return 0.0
