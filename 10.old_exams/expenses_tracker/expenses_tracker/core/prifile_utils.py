from expenses_tracker.web_app.models import Profile, Expense


def has_profile():
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    profile.budget_left = profile.budget - sum(e.price for e in expenses)
    return profile




# def has_profile():
#     profile = Profile.objects.all()
#     try:
#         return profile[0]
#     except IndexError:
#         return None

