"""Grader for the reply task.

Evaluates whether the agent generated a meaningful reply
to the email. Returns a score between 0.0 and 1.0.
"""

from server.email_env_environment import EmailEnv
from models import EmailAction


def grade(action: dict, env_state: dict) -> float:
    """Grade the reply task.

    Args:
        action: The agent's action dictionary with 'reply' key.
        env_state: The current environment state dictionary.

    Returns:
        A float score between 0.0 and 1.0.
    """
    expected = (env_state.get("expected_reply") or "").strip().lower()
    reply = (action.get("reply") or "").strip().lower()

    if not reply:
        return 0.0

    if not expected:
        # No expected reply defined; give partial credit for any reply
        return 0.5

    # Check if the expected reply is contained in the agent's reply
    if expected in reply:
        return 1.0

    # Partial credit: check word overlap
    expected_words = set(expected.split())
    reply_words = set(reply.split())
    if not expected_words:
        return 0.5

    overlap = len(expected_words & reply_words) / len(expected_words)
    return round(min(max(overlap, 0.0), 1.0), 2)
