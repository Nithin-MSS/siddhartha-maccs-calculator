def calculate_fd(principal, original_rate, completed_months):
    # FD premature rule → only 1% reduction
    premature_rate = original_rate - 1

    # Simple interest using months
    original_interest = (principal * original_rate / 100) * (completed_months / 12)
    eligible_interest = (principal * premature_rate / 100) * (completed_months / 12)

    excess_deducted = original_interest - eligible_interest

    final_settlement = principal + eligible_interest

    total_effective = final_settlement

    return {
        "premature_rate": premature_rate,
        "original_interest": original_interest,
        "eligible_interest": eligible_interest,
        "excess_deducted": excess_deducted,
        "final_settlement": final_settlement,
        "total_effective": total_effective
    }
