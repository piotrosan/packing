

def check_up_to_ten(amount):
    small_box = 0
    medium_box = 0
    big_box = 0
    if amount <=3 and amount > 0:
        small_box = 1
    if amount <= 6 and amount > 3:
        medium_box = 1
    if amount <= 9 and amount > 6:
        big_box = 1
    return big_box, medium_box, small_box


def check_mod_amount(order_amount):
    big_box = order_amount % 9
    return big_box


def check_integer_amount(order_amount):
    big_box = order_amount // 9
    return big_box


def do_if_big(mod_big_box, integer_big_box):
    od_big_box, medium_box, small_box = check_up_to_ten(mod_big_box)
    return {
        "big_box": integer_big_box + od_big_box,
        "medium_box": medium_box,
        "small_box": small_box
    }


def packing_order(order_amount):
    if order_amount <= 9:
        od_big_box, medium_box, small_box = check_up_to_ten(order_amount)
        return {
            "big_box": od_big_box,
            "medium_box": medium_box,
            "small_box": small_box
        }

    mod_big_box = check_mod_amount(order_amount)
    integer_big_box = check_integer_amount(order_amount)

    if integer_big_box:
        if mod_big_box:
            return do_if_big(mod_big_box, integer_big_box)
        else:
            return {
                "big_box": integer_big_box,
                "medium_box": 0,
                "small_box": 0
            }
