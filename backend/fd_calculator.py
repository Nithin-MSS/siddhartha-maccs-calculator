from datetime import date

def calculate_fd(principal, original_rate, deposit_date, premature_date):

    total_days = (premature_date - deposit_date).days

    # 1% reduction only
    premature_rate = original_rate - 1

    # Interest at premature rate
    interest = principal * premature_rate / 100 * (total_days / 365)

    final_settlement = principal + interest

    return {
        "total_days": total_days,
        "premature_rate": premature_rate,
        "interest": interest,
        "final_settlement": final_settlement
    }
