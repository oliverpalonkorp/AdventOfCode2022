def score_strategy(filename: str) -> int:
    # Read the strategy string from the file
    with open(filename) as f:
        strategy = f.read()

    # Map each hand shape to its corresponding score
    shape_scores = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    # Initialize the total score to 0
    total_score = 0

    # Split the strategy string into lines
    lines = strategy.strip().split("\n")

    # Iterate over the lines
    for line in lines:
        # Parse the opponent's hand shape and your hand shape
        opp_shape, your_shape = line.split()

        # Calculate the round score as the sum of your hand shape score and
        # the outcome score (0 for loss, 3 for draw, 6 for win)
        if opp_shape == your_shape:
            round_score = shape_scores[opp_shape] + 3
        elif (opp_shape == "A" and your_shape == "Y") or (opp_shape == "B" and your_shape == "X") or (opp_shape == "C" and your_shape == "Z"):
            round_score = shape_scores[your_shape] + 6
        else:
            round_score = shape_scores[your_shape]

        # Add the round score to the total score
        total_score += round_score

    # Return the total score
    return total_score


# Define the file name
filename = "data2.txt"

# Calculate the score for the strategy in the file
score = score_strategy(filename)

# Print the score
print(score)  # This should print the total score for the strategy in the file
