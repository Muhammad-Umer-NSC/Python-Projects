from level import get_level
import generate

def main():
    # Get the difficulty level from the user
    level = get_level()
    # Initialize the score
    score = 0

    # Loop to ask 10 questions
    for i in range(10):
        try:
            # Initialize the number of tries for each question
            tries = 0
            # Generate two integers and their sum based on the level
            x, y, answer = generate.generate_integer(level)

            # Allow up to 3 attempts to answer each question
            for j in range(3):
                # Prompt the user for the answer
                question = input(f"{x} + {y} = ")
                try:

                    question = int(question)

                except ValueError:
                    print("EEE")
                    tries += 1
                    continue

                # Check if the answer is correct
                if question == answer:
                    # Increment the score if correct
                    score += 1
                    break
                # If the answer is incorrect
                elif question != answer:
                    # Print an error message
                    print("EEE")
                    # Increment the number of tries
                    tries += 1
            # If the user fails 3 attempts
            if tries == 3:
                # Show the correct answer
                print(f"{x} + {y} = {answer}")

        except ValueError:
            # Ignore invalid input
            pass

     # Print the final score
    print(f"Score: {score}")


# Run the main function
if __name__ == "__main__":
    main()
