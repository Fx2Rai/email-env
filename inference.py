def act(observation):
    try:
        text = observation["email_text"].lower()

        # spam detection
        if "win" in text or "free" in text or "offer" in text:
            return {
                "classification": "spam",
                "priority": "low",
                "reply": ""
            }

        # important emails
        if "meeting" in text or "urgent" in text:
            return {
                "classification": "important",
                "priority": "high",
                "reply": "Sure, I will attend."
            }

        # normal emails
        return {
            "classification": "normal",
            "priority": "low",
            "reply": "Sounds good, let's plan soon!"
        }

    except Exception:
        return {
            "classification": "normal",
            "priority": "low",
            "reply": "Sorry, something went wrong."
        }