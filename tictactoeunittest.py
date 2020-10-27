from tictactoe import findWinner, findTie, makeBoard

if __name__ == "__main__":
    # (Test Name, Test Init, Solution, Function)
    tests = [
        (
            "Vertical Test X 1", [
                [None, "X", None], 
                [None, "X", None], 
                [None, "X", None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Vertical Test X 2", [
                [None, None, "X", None], 
                [None, None, "X", None], 
                [None, None, "X", None],
                [None, None, "X", None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Horizontal Test X 1", [
                ["X", "X", "X"], 
                [None, None, None], 
                [None, None, None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Horizontal Test X 2", [
                ["X", "X", "X", "X"], 
                [None, None, None, None], 
                [None, None, None, None]
                ],
            "X",
            "findWinner"
        ),
        (
            "Vertical Test O 1", [
                ["O", None, None], 
                ["O", None, None], 
                ["O", None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Vertical Test O 2", [
                ["O", None, None], 
                ["O", None, None], 
                ["O", None, None],
                ["O", None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Horizontal Test O 1", [
                [None, None, None], 
                ["O", "O", "O"], 
                [None, None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Horizontal Test O 2", [
                ["O", "O", "O", "O"], 
                [None, None, None, None], 
                [None, None, None, None]
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
            "Bottom Left Diagonal Test 1", [
                [None, None, "O"], 
                [None, "O", None], 
                ["O", None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Bottom Left Diagonal Test 2", [
                [None, None, None, "O"],
                [None, None, "O", None], 
                [None, "O", None, None], 
                ["O", None, None, None]
                ],
            "O",
            "findWinner"
        ),
        (
            "Bottom Left Diagonal Test 3", [
                [None, None, None, "O"],
                [None, None, "O", None], 
                [None, None, None, None], 
                ["O", None, None, None]
                ],
            None,
            "findWinner"
        ),
        (
            "Top Left Diagonal Test 1", [
                ["X", None, None], 
                [None, "X", None], 
                [None, None, "X"]
                ],
            "X",
            "findWinner"
        ),
        (
            "Top Left Diagonal Test 2", [
                ["X", None, None, None], 
                [None, "X", None, None], 
                [None, None, "X", None],
                [None, None, None,"X"]
                ],
            "X",
            "findWinner"
        ),
        (
            "Top Left Diagonal Test 3", [
                ["X", None, None, None], 
                [None, "X", None, None], 
                [None, None, None, None],
                [None, None, None, "X"]
                ],
            None,
            "findWinner"
        ),
        (
            "Mixed Columns Test", [
                ["X", "O", "X"], 
                ["O", "O", "X"], 
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
        (
            "Tie Situation 4", [
                ["X", "O", "X", "O"], 
                ["X", "O", "X", "X"], 
                ["O", "X", "O", "O"]
                ],
            True,
            "findTie"
        ),
        (
            "Variable Board 1",
            (4,4),
            [
                [None, None, None, None], 
                [None, None, None, None], 
                [None, None, None, None], 
                [None, None, None, None]
            ],
            "makeBoard"
        ),
        (
            "Variable Board 2",
            (3,4),
            [
                [None, None, None], 
                [None, None, None], 
                [None, None, None], 
                [None, None, None]
            ],
            "makeBoard"
        ),
        (
            "Variable Board 3",
            (4,3),
            [
                [None, None, None, None], 
                [None, None, None, None], 
                [None, None, None, None]
            ],
            "makeBoard"
        ),
    ]

    print("Testing the program... \n")
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

        elif tests[i][3] == "makeBoard":
            board = makeBoard(tests[i][1])
            if board != tests[i][2]:
                print("There was a problem with the {}!".format(tests[i][0]))
                print("Expected {0}, but got {1}!\n".format(tests[i][2], board))
            else:
                print("{} passed!\n".format(tests[i][0]))
