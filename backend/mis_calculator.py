from decimal import Decimal, getcontext

getcontext().prec = 28


def calculate_mis(principal, original_rate, completed_months):

    principal = Decimal(str(principal))
    original_rate = Decimal(str(original_rate))
    completed_months = Decimal(str(completed_months))

    # Premature rule: minus 2% (already includes penalty)
    premature_rate = original_rate - Decimal("2.0")

    # Monthly interest
    monthly_original = principal * (original_rate / Decimal("100")) / Decimal("12")
    monthly_premature = principal * (premature_rate / Decimal("100")) / Decimal("12")

    # Total interest
    interest_received = monthly_original * completed_months
    eligible_interest = monthly_premature * completed_months

    # Adjustment
    excess = interest_received - eligible_interest

    final_settlement = principal - excess
    total_effective = final_settlement + interest_received

    return {
        "premature_rate": float(premature_rate),
        "interest_received": float(interest_received),
        "eligible_interest": float(eligible_interest),
        "excess": float(excess),
        "final_settlement": float(final_settlement),
        "total_effective": float(total_effective)
    }


def compare_wait(principal, original_rate, current_months, wait_months):

    now = calculate_mis(principal, original_rate, current_months)
    future = calculate_mis(principal, original_rate, current_months + wait_months)

    gain = future["total_effective"] - now["total_effective"]

    return {
        "now": now,
        "future": future,
        "gain": gain
    }
