from datetime import date

def get_slab_rate(days):
    if 30 <= days <= 90:
        return 6
    elif 91 <= days <= 180:
        return 7
    elif 181 <= days < 365:
        return 7.5
    elif 365 <= days < 730:
        return 10
    elif 730 <= days < 1095:
        return 11
    elif 1095 <= days <= 2190:
        return 12
    else:
        return 5  # fallback

def calculate_mis(principal, deposit_date, premature_date):

    days = (premature_date - deposit_date).days

    slab_rate = get_slab_rate(days)

    # Monthly MIS effective rate
    monthly_effective_rate = slab_rate - 0.2

    # Premature penalty for MIS = 2%
    premature_rate = monthly_effective_rate - 2

    # Months completed (full months only)
    months = days // 30

    # Interest already paid monthly
    interest_paid = principal * (monthly_effective_rate / 100) * (months / 12)

    # Eligible interest (daily calculation)
    eligible_interest = principal * (premature_rate / 100) * (days / 365)

    excess = interest_paid - eligible_interest

    final_settlement = principal - excess

    return {
        "days": days,
        "slab_rate": slab_rate,
        "monthly_effective_rate": monthly_effective_rate,
        "premature_rate": premature_rate,
        "interest_paid": round(interest_paid, 2),
        "eligible_interest": round(eligible_interest, 2),
        "excess": round(excess, 2),
        "final_settlement": round(final_settlement, 2)
    }
