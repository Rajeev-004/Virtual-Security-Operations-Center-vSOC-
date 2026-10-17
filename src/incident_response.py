"""Safe, simulated incident-response actions for the VSOC demo."""


def respond_to_threat(threat: str) -> str:
    """Report a simulated response action without changing a real system."""
    message = f"Simulated response for threat: {threat}"
    print(message)
    return message
