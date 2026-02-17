from datetime import date

def calculate_fd(principal, rate, deposit_date, premature_date):

    total_days = (premature_date - deposit_date).days

    # FD rule → Only 1% deduction
    premature_rate = rate - 1.0

    # Interest at premature rate
    interest = principal * (premature_rate / 100) * (total_days / 365)

    # Final settlement
    final_settlement = principal + interest

    return {
        "total_days": total_days,
        "premature_rate": premature_rate,
        "interest": interest,
        "final_settlement": final_settlement
    }
