from solfege.lib.pattern import Pattern

TUNE_IN_PATTERN = Pattern(
    [
        1, 3, 5, 3, 1,
        4, 3, 2, 1,
        5, 6, 7, 8,
        1, 3, 5, 8,
        1, 3, 5, 7,
    ],
    'tune_in')

ASCENDING = Pattern(
    [1, 2, 3, 4, 5, 6, 7, 8],
    'ascending'
)

DESCENDING = Pattern(
    [8, 7, 6, 5, 4, 3, 2, 1],
    'descending'
)

DOWN_TO_ROOT = Pattern(
    [1,
    2, 1,
    3, 2 ,1,
    4, 3, 2, 1,
    5, 4, 3, 2, 1,
    6, 5, 4, 3, 2, 1,
    7, 6, 5, 4, 3, 2, 1,
    8, 7, 6, 5, 4, 3, 2, 1],
    'down_to_root'
)

UP_TO_ROOT = Pattern(
    [
        8,
        7, 8,
        6, 7, 8,
        5, 6, 7,8 ,
        4, 5, 6, 7, 8,
        3, 4, 5, 6, 7, 8,
        2, 3, 4, 5, 6, 7, 8,
        1, 2, 3, 4, 5, 6, 7, 8,
        ],
    'up_to_root'

)

ASCENDING_THIRDS_ASCENDING = Pattern(
    [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],
    'ascending_thirds_ascending'
)

DESCENDING_THIRDS_DESCENDING= Pattern(
    [8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1],
    'ascending_thirds_ascending'
)

MODE_WORKOUT = [
    TUNE_IN_PATTERN,
    ASCENDING,
    DOWN_TO_ROOT,
    UP_TO_ROOT,
    ASCENDING_THIRDS_ASCENDING,
    DESCENDING_THIRDS_DESCENDING,
    ]