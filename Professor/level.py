def get_level():
    while True:
        try:
            # Prompt the user for the level
            level = int(input("Level: "))
            # Check if the level is valid (1, 2, or 3)
            if level in range(1, 4):
                return level

        except ValueError:
            # Ignore invalid input
            pass