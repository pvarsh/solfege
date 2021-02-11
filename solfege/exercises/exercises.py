from solfege.lib.pattern import Pattern

TUNE_IN_PATTERN = Pattern(
    [
        1, 3, 5, 3, 1,
        4, 3, 2, 1,
        5, 6, 7, 8,
        1, 3, 5, 8,
        1, 3, 5, 7,
    ],
    'Tune-in')

ASCENDING = Pattern(
    [1, 2, 3, 4, 5, 6, 7, 8],
    'Ascending'
)

DESCENDING = Pattern(
    [8, 7, 6, 5, 4, 3, 2, 1],
    'Descending'
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
    'Down to root from every step'
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
    'Up to root from every step'
)

THREE_NOTES_ASCENDING = Pattern(
    [
        1, 2, 3,
        2, 3, 4,
        3, 4, 5,
        4, 5, 6,
        5, 6, 7,
        6, 7, 8,
    ],
    'Three notes ascending'
)

THREE_DESCENDING_NOTES_ASCENDING = Pattern(
    [
        3, 2, 1,
        4, 3, 2,
        5, 4, 3,
        6, 5, 4,
        7, 6, 5,
        8, 7, 6,
        9, 8, 7,
        10, 9, 8,
    ],
    "Three descending notes ascending"
)

THREE_ASCENDING_NOTES_DESCENDING = Pattern(
    [
        8, 9, 10,
        7, 8, 9,
        6, 7, 8,
        5, 6, 7,
        4, 5, 6,
        3, 4, 5,
        2, 3, 4,
        1, 2, 3,
    ],
    "Three ascending notes descending"
)

THREE_NOTES_DESCENDING = Pattern(
    [
        8, 7, 6,
        7, 6, 5,
        6, 5, 4,
        5, 4, 3,
        4, 3, 2,
        3, 2, 1,
        2, 1, 0,
        1, 0, -1,
    ],
    'Three notes descending'
)

ASCENDING_THIRDS_ASCENDING = Pattern(
    [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],
    'Ascending triads ascending'
)

DESCENDING_THIRDS_DESCENDING= Pattern(
    [8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1],
    'Descending triads descending'
)

ASCENDING_TRIADS_ASCENDING = Pattern(
    [
        1, 3, 5,
        2, 4, 6,
        3, 5, 7,
        4, 6, 8,
        5, 7, 9,
        6, 8, 10,
        7, 9, 11,
        8, 10, 12,
    ],
    'Ascending triads ascending'
)

DESCENDING_TRIADS_DESCENDING = Pattern(
    [
        8, 6, 4,
        7, 5, 3,
        6, 4, 2,
        5, 3, 1,
    ],
    'Descending triads descending'
)

MODE_WORKOUT = [
    TUNE_IN_PATTERN,
    ASCENDING,
    DESCENDING,
    DOWN_TO_ROOT,
    UP_TO_ROOT,
    THREE_NOTES_ASCENDING,
    THREE_NOTES_DESCENDING,
    THREE_DESCENDING_NOTES_ASCENDING,
    THREE_ASCENDING_NOTES_DESCENDING,
    ASCENDING_THIRDS_ASCENDING,
    DESCENDING_THIRDS_DESCENDING,
    ASCENDING_TRIADS_ASCENDING,
    DESCENDING_TRIADS_DESCENDING,
    ]