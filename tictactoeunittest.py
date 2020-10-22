from tictactoe import findWinner, findTie

if __name__ == "__main__":
    # (Test Name, Test Init, Solution, Function)
    tests = [
        (
            "Vertical Test X", [
                ["X", None, None], 
                ["X", None, None], 
                ["X", None, None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Horizontal Test X", [
                ["X", "X", "X"], 
                [None, None, None], 
                [None, None, None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Vertical Test O", [
                ["O", None, None], 
                ["O", None, None], 
                ["O", None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Horizontal Test O", [
                ["O", "O", "O"], 
                [None, None, None], 
                [None, None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Mixed Vertical Test", [
                ["X", None, None], 
                ["O", None, None], 
                ["X", None, None]
                ],
            None,
            "findWinner"
        ),
        (
            "Mixed Horizontal Test", [
                ["X", "O", "X"], 
                [None, None, None], 
                [None, None, None]
                ],
            None,
            "findWinner"
        ),
        (
            "Bottom Left Diagonal Test", [
                [None, None, "X"], 
                [None, "X", None], 
                ["X", None, None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Top Left Diagonal Test", [
                ["X", None, None], 
                [None, "X", None], 
                [None, None, "X"]
                ],
            "X",
            "findWinner"
        ),
        (
            "Mixed Columns Test", [
                ["X", "O", "X"], 
                ["X", "O", "X"], 
                ["O", "X", "X"]
                ],
            "X",
            "findWinner"
        ),
        (
            "Tie Situation 1", [
                ["X", "O", "X"], 
                ["X", "O", "X"], 
                ["O", "X", "O"]
                ],
            True,
            "findTie"
        ),
        (
            "Tie Situation 2", [
                ["X", "O", "X"], 
                ["X", "O", "X"], 
                ["O", "X", "X"]
                ],
            False,
            "findTie"
        ),
        (
            "Tie Situation 3", [
                ["X", "O", "X"], 
                ["X", "O", "X"], 
                ["O", "X", None]
                ],
            False,
            "findTie"
        ),
    ]

    for i in range(len(tests)):
        if tests[i][3] == "findWinner":
            winner = findWinner(tests[i][1])
            if winner != tests[i][2]:
                print("There was a problem with the {}!".format(tests[i][0]))
                print("Expected {0}, but got {1}!\n".format(tests[i][2], winner))
            else:
                print("{} passed!\n".format(tests[i][0]))
        elif tests[i][3] == "findTie":
            tie = findTie(tests[i][1])
            if tie != tests[i][2]:
                print("There was a problem with the {}!".format(tests[i][0]))
                print("Expected {0}, but got {1}!\n".format(tests[i][2], tie))
            else:
                print("{} passed!\n".format(tests[i][0]))
