def calculate_fd(principal, original_rate, months):
    """
    FD Prematurity Logic:
    - Only 1% reduction
    - Simple interest calculation
    """

    premature_rate = original_rate - 1.0

    interest = principal * premature_rate / 100 * (months / 12)

    final_amount = principal + interest

    return {
        "premature_rate": premature_rate,
        "interest": interest,
        "final_amount": final_amount
    }
