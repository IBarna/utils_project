# coding=utf-8


def greet_dude_with_food(dude_name, food_today):
    return "Hey {dude_name}! Want a {food_today} today?".format(
        dude_name=dude_name,
        food_today=food_today,
        # q_marks='?' *num_question_marks
    )
