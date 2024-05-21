import itertools

def calculate_probabilities(dice_a, dice_b):
    probabilities = {}
    for roll in itertools.product(dice_a, dice_b):
        total = sum(roll)
        probabilities[total] = probabilities.get(total, 0) + 1
    return probabilities

def undoomed_dice():
    Die_a = [1, 2, 3, 4, 5, 6]
    Die_b = Die_a.copy()

    for new_dice_a in itertools.combinations_with_replacement(range(1, 5), 6):
        for new_dice_b in itertools.combinations_with_replacement(range(1, 9), 6):
            if max(new_dice_a) <= 4 and sum(new_dice_b) > 21:
                original_probabilities = calculate_probabilities(Die_a, Die_b)
                new_probabilities = calculate_probabilities(new_dice_a, new_dice_b)

                if original_probabilities == new_probabilities:
                    return new_dice_a, new_dice_b

    return None, None

def main():
    New_Die_a, New_Die_b = undoomed_dice()
    if New_Die_a is not None and New_Die_b is not None:
        print("New_Die_A:", New_Die_a)
        print("New_Die_B:", New_Die_b)
    else:
        print("No combinations found.")

if __name__ == "__main__":
    main()
