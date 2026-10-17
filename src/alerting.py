"""Alerting helpers for the VSOC demonstration."""


def send_alert(threat: str) -> str:
    """Create a console alert and return its message.

    This demo prints alerts; it does not send email, SMS, or block traffic.
    """
    message = f"ALERT: Threat detected - {threat}"
    print(message)
    return message
