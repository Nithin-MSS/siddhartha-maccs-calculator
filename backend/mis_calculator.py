from datetime import date

def calculate_mis(principal, rate, deposit_date, premature_date):

    total_days = (premature_date - deposit_date).days

    # Society rule: Rate already includes penalty
    premature_rate = rate - 2.0  # example 10.8 → 8.8

    # Interest actually paid (original rate)
    original_interest = principal * (rate / 100) * (total_days / 365)

    # Eligible interest at premature rate
    eligible_interest = principal * (premature_rate / 100) * (total_days / 365)

    # Excess paid
    excess = original_interest - eligible_interest

    # Final settlement
    final_settlement = principal - excess

    return {
        "total_days": total_days,
        "premature_rate": premature_rate,
        "original_interest": original_interest,
        "eligible_interest": eligible_interest,
        "excess": excess,
        "final_settlement": final_settlement
    }
