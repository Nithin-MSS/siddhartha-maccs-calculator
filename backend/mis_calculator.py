def calculate_mis(principal, original_rate, completed_months):
    """
    MIS Prematurity Logic:
    - Premature rate = original_rate - 2%
    - No separate 1% deduction
    - No 0.2% deduction
    - Calculation based on monthly payout logic
    """

    # Premature rate (2% reduction total)
    premature_rate = original_rate - 2

    # Monthly interest originally paid
    monthly_original = (principal * original_rate / 100) / 12
    interest_received = monthly_original * completed_months

    # Monthly interest at premature rate
    monthly_premature = (principal * premature_rate / 100) / 12
    eligible_interest = monthly_premature * completed_months

    # Excess interest deducted
    excess_deducted = interest_received - eligible_interest

    # Final settlement (principal minus excess)
    final_settlement = principal - excess_deducted

    # Total effective amount received
    total_effective = final_settlement + interest_received

    return {
        "premature_rate": premature_rate,
        "interest_received": interest_received,
        "eligible_interest": eligible_interest,
        "excess_deducted": excess_deducted,
        "final_settlement": final_settlement,
        "total_effective": total_effective
    }
