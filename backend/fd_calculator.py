from decimal import Decimal, getcontext

getcontext().prec = 28


def calculate_fd(principal, original_rate, completed_months):

    principal = Decimal(str(principal))
    original_rate = Decimal(str(original_rate))
    completed_months = Decimal(str(completed_months))

    # FD rule: minus only 1%
    premature_rate = original_rate - Decimal("1.0")

    # Interest calculation (month based)
    interest = principal * (premature_rate / Decimal("100")) * (completed_months / Decimal("12"))

    final_settlement = principal + interest

    return {
        "premature_rate": float(premature_rate),
        "interest": float(interest),
        "final_settlement": float(final_settlement)
    }
