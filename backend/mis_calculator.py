def calculate_mis(principal, original_rate, completed_months):
    # Premature rate (2% reduction total)
    premature_rate = original_rate - 2

    # Monthly interest calculations
    original_monthly = (principal * original_rate / 100) / 12
    eligible_monthly = (principal * premature_rate / 100) / 12

    # Total interest
    interest_received = original_monthly * completed_months
    eligible_interest = eligible_monthly * completed_months

    # Excess to deduct
    excess_deducted = interest_received - eligible_interest

    # Final settlement
    final_settlement = principal - excess_deducted

    total_effective = final_settlement + interest_received

    return {
        "premature_rate": premature_rate,
        "interest_received": interest_received,
        "eligible_interest": eligible_interest,
        "excess_deducted": excess_deducted,
        "final_settlement": final_settlement,
        "total_effective": total_effective
    }
