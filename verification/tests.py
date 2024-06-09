"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [60, 190, 98],
            "answer": -1,
        },
        {
            "input": [70, 140, 92],
            "answer": -1,
        },
        {
            "input": [70, 130, 98],
            "answer": 1,
        }
    ],
    "Extra": [
        {
            "input": [65, 155, 96],
            "answer": 0,
        },
    ]
}
