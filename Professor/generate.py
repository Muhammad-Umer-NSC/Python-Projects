import random


def generate_integer(level):
    if level not in range(1, 4):
        # Raise an error if the level is invalid
        raise ValueError

    try:
        if level == 1:
            # Generate integers between 0 and 9 for level 1
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            # Generate integers between 10 and 99 for level 2
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            # Generate integers between 100 and 999 for level 3
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        # Return the two integers and their sum
        return x, y, x + y

    except ValueError:
        # Ignore invalid input
        pass
