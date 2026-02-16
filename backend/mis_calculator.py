def calculate_mis(principal, original_rate, months):
    """
    MIS Prematurity Logic:
    - Premature rate = original_rate - 2%
    - Monthly payout system
    - Deduct excess interest already paid
    """

    premature_rate = original_rate - 2.0

    # Interest already received (monthly payout at original rate)
    monthly_original = (principal * original_rate / 100) / 12
    interest_received = monthly_original * months

    # Eligible interest at premature rate
    monthly_premature = (principal * premature_rate / 100) / 12
    eligible_interest = monthly_premature * months

    excess = interest_received - eligible_interest
    final_settlement = principal - excess

    return {
    "premature_rate": premature_rate,
    "interest_received": interest_received,
    "eligible_interest": eligible_interest,
    "excess": excess,
    "final_settlement": final_settlement,
    "total_effective": final_settlement + interest_received
   }



def compare_wait(principal, original_rate, months_completed, total_tenure):
    """
    Compare break now vs wait till maturity
    """

    # Break now
    now_result = calculate_mis(principal, original_rate, months_completed)

    # Full maturity
    monthly_original = (principal * original_rate / 100) / 12
    full_interest = monthly_original * total_tenure
    maturity_total = principal + full_interest

    difference = maturity_total - (now_result["final_amount"] + now_result["interest_received"])

    return {
        "maturity_total": maturity_total,
        "difference": difference
    }
