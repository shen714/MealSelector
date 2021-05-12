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
meal_categories = ["meals_healthy", "meals_ok", "meals_unhealthy"]

def update_records(selected_meal_category):
    with open("records", "r") as file:
        records = file.readlines()
     
    if selected_meal_category == meal_categories[0]:
        records[0] = float(records[0]) - HEALTHY_MEAL_DECAY
        if records[0] <= 0:
            records[0] = INIT_PROB
    elif selected_meal_category == meal_categories[1]:
        records[1] = float(records[1]) - OK_MEAL_DECAY
        if records[1] <= 0:
            records[1] = INIT_PROB
    else:
        records[2] = date.isoformat(date.today())
    
    for i in range(len(records)):
       records[i] = str(records[i]).strip() + "\n"

    with open("records", "w") as file:
        file.writelines(records)
    

def get_category_for_today():
    last_day_eating_unhealthy_meal = ""
    probabilities = []
    with open("records", "r") as file:
        for pos, record in enumerate(file):
            if pos == 2:
                last_day_eating_unhealthy_meal = date.fromisoformat(record.strip())
            else:
                probabilities.append(float(record.strip()))
    
    today = date.today()
    days_to_next_cheat_meal = abs(today - last_day_eating_unhealthy_meal).days
    
    probabilities.append(0) if days_to_next_cheat_meal < MEAL_BREAK else probabilities.append(INIT_PROB)
    
    category_for_today = choices(meal_categories, probabilities)[0]
 
    print("category for today: " + category_for_today)
    return category_for_today


category_for_today = get_category_for_today()
update_records(category_for_today)
# Select meal within the selected category
f = open(category_for_today, "r")
meals = []
for meal in f:
    meals.append(meal)

meal_for_today = choices(meals)[0]
f.close()
print("meal: " + meal_for_today)

