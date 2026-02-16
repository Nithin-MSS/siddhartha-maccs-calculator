def calculate_mis_prematurity(principal, roi, months):
    """
    MIS Rule:
    Premature Rate = ROI - 0.2 - 1
    """

    premature_rate = roi - 0.2 - 1

    monthly_original = principal * (roi / 100) / 12
    interest_received = monthly_original * months

    monthly_premature = principal * (premature_rate / 100) / 12
    eligible_interest = monthly_premature * months

    excess_interest = interest_received - eligible_interest
    final_amount = principal - excess_interest

    return {
        "premature_rate": premature_rate,
        "interest_received": interest_received,
        "eligible_interest": eligible_interest,
        "excess_interest": excess_interest,
        "final_amount": final_amount
    }
