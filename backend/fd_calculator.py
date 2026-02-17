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
        return 5

def calculate_fd(principal, deposit_date, premature_date):

    days = (premature_date - deposit_date).days

    slab_rate = get_slab_rate(days)

    # FD premature penalty = 1%
    premature_rate = slab_rate - 1

    eligible_interest = principal * (premature_rate / 100) * (days / 365)

    final_settlement = principal + eligible_interest

    return {
        "days": days,
        "slab_rate": slab_rate,
        "premature_rate": premature_rate,
        "interest": round(eligible_interest, 2),
        "final_settlement": round(final_settlement, 2)
    }
