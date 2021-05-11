# Rules:
# unhealthy meals: We can only eat one unhealty meal every week, so the selector won't give unhealthy mean unless it has been 7 days after last unhealthy meal.
# healthy meals: The chance of an healthy meal being selected decremented by 0.05 every time.
# ok meals: The chance of an ok meal being selected decremented by 0.1 every time.

from random import choices
from datetime import date

MEAL_BREAK = 7
INIT_PROB = 0.33
OK_MEAL_DECAY = 0.1
HEALTHY_MEAL_DECAY = 0.05

#def update_days_to_next_cheat_meal():


def get_category_for_today():
    meal_categories = ["meals_healthy", "meals_ok", "meals_unhealthy"]

    f = open("records", "r")
    last_day_eating_unhealthy_meal = date.fromisoformat(f.readline().strip())
    print("last_day_unhealthy_meal " + str(last_day_eating_unhealthy_meal))

    today = date.today()
    days_to_next_cheat_meal = abs(today - last_day_eating_unhealthy_meal).days

    print("days_to_next_cheat_meal " + str(days_to_next_cheat_meal))
    
    probabilities = []
    for line in f:
        print("prob " + str(line))
        probabilities.append(float(line.strip()))

    probabilities.append(0) if days_to_next_cheat_meal < MEAL_BREAK else probabilities.append(INIT_PROB)

    category_for_today = choices(meal_categories, probabilities)[0]
    # update last_day_eating_unhealthy_meal to today
 
    f.close()
    print("category: " + category_for_today)
    return category_for_today


category_for_today = get_category_for_today()
# Select meal within the selected category
f = open(category_for_today, "r")
meals = []
for meal in f:
    meals.append(meal)

meal_for_today = choices(meals)[0]
f.close()
print("meal: " + meal_for_today)

