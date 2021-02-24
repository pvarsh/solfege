from solfege.exercises.scales import BLUES
from solfege.lib.pattern import Pattern


def flatten(l):
    return [i for sublist in l for i in sublist]


TUNE_IN_PATTERN = Pattern(
    [
        0, 2, 4, 2, 0,
        3, 2, 1, 0,
        4, 5, 6, 7,
        0, 2, 4, 7,
        0, 2, 4, 6,
    ],
    'Tune-in-1')


def ascending(length: int) -> Pattern:
    return Pattern(
        list(range(length + 1)),
        'Ascending'
    )


ASCENDING = Pattern(
    [0, 1, 2, 3, 4, 5, 6, 7],
    'Ascending'
)

DESCENDING = Pattern(
    [7, 6, 5, 4, 3, 2, 1, 0],
    'Descending'
)


def descending(length: int) -> Pattern:
    return Pattern(
        list(range(length, -1, -1)),
        'Descending'
    )


DOWN_TO_ROOT = Pattern(
    [
        0,
        1, 0,
        2, 1, 0,
        3, 2, 1, 0,
        4, 3, 2, 1, 0,
        5, 4, 3, 2, 1, 0,
        6, 5, 4, 3, 2, 1, 0,
        7, 6, 5, 4, 3, 2, 1, 0,
    ],
    'Down to root from every step'
)


def down_to_root(length: int) -> Pattern:
    return Pattern(
        flatten([list(range(s, -1, -1)) for s in range(length+1)]),
        'Down to root from every step'
    )


UP_TO_ROOT = Pattern(
    [
        7,
        6, 7,
        5, 6, 7,
        4, 5, 6, 7,
        3, 4, 5, 6, 7,
        2, 3, 4, 5, 6, 7,
        1, 2, 3, 4, 5, 6, 7,
        0, 1, 2, 3, 4, 5, 6, 7,
    ],
    'Up to root from every step'
)


def up_to_root(length: int) -> Pattern:
    return Pattern(
        flatten([list(range(s, length+1)) for s in range(length, -1, -1)]),
        'Up to root from every step'
    )


THREE_NOTES_ASCENDING = Pattern(
    [
        0, 1, 2,
        1, 2, 3,
        2, 3, 4,
        3, 4, 5,
        4, 5, 6,
        5, 6, 7,
        6, 7, 8, 7,
    ],
    'Three notes ascending'
)


def three_notes_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([s, s+1, s+2] for s in range(length)) + [length],
        'Three notes ascending'
    )


THREE_NOTES_DESCENDING = Pattern(
    [
        7, 6, 5,
        6, 5, 4,
        5, 4, 3,
        4, 3, 2,
        3, 2, 1,
        2, 1, 0,
        1, 0, -1, 0,
    ],
    'Three notes descending'
)


def three_notes_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s-1, s-2] for s in range(length, 0, -1)]) + [0],
        'Three notes descending'
    )


THREE_DESCENDING_NOTES_ASCENDING = Pattern(
    [
        2, 1, 0,
        3, 2, 1,
        4, 3, 2,
        5, 4, 3,
        6, 5, 4,
        7, 6, 5,
        8, 7, 6, 7,
    ],
    "Three descending notes ascending"
)


def three_descending_notes_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s + 2, s + 1, s] for s in range(length)]) + [length],
        "Three descending notes ascending"
    )


THREE_ASCENDING_NOTES_DESCENDING = Pattern(
    [
        7, 8, 9,
        6, 7, 8,
        5, 6, 7,
        4, 5, 6,
        3, 4, 5,
        2, 3, 4,
        1, 2, 3, 0,
    ],
    "Three ascending notes descending"
)


def three_ascending_notes_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s + 1, s + 2] for s in range(length, 0, -1)]) + [0],
        "Three ascending notes descending"
    )


ASCENDING_THIRDS_ASCENDING = Pattern(
    [0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7],
    'Ascending thirds ascending'
)


def ascending_thirds_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s + 2] for s in range(length)]) + [length],
        'Ascending thirds ascending'
    )


DESCENDING_THIRDS_DESCENDING = Pattern(
    [7, 5, 6, 4, 5, 3, 4, 2, 3, 1, 2, 0, 1, -1, 0],
    'Descending thirds descending'
)


def descending_thirds_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s - 2] for s in range(length, 0, -1)]) + [0],
        'Descending thirds descending'
    )


ASCENDING_TRIADS_ASCENDING = Pattern(
    [
        0, 2, 4,
        1, 3, 5,
        2, 4, 6,
        3, 5, 7,
        4, 6, 8,
        5, 7, 9,
        6, 8, 10, 7,
    ],
    'Ascending triads ascending'
)


def ascending_triads_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s + 2, s + 4] for s in range(length)]) + [length],
        'Ascending triads ascending'
    )


DESCENDING_TRIADS_DESCENDING = Pattern(
    [
        7, 5, 3,
        6, 4, 2,
        5, 3, 1,
        4, 2, 0,
        3, 1, -1,
        2, 0, -2,
        1, -1, -3, 0  # ending on steps 5, 1 from below
    ],
    'Descending triads descending'
)


def descending_triads_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s - 2, s - 4] for s in range(length, 0, -1)]) + [0],
        'Descending triads descending'
    )


DESCENDING_TRIADS_ASCENDING = Pattern(
    [
        4, 2, 0,
        5, 3, 1,
        6, 4, 2,
        7, 5, 3,
        8, 6, 4,
        9, 7, 5,
        10, 8, 6, 7
    ],
    'Descending triads ascending'
)


def descending_triads_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s + 4, s + 2, s] for s in range(length)]) + [length],
        'Descending triads ascending'
    )


ASCENDING_TRIADS_DESCENDING = Pattern(
    [
        7, 9, 11,
        6, 8, 10,
        5, 7, 9,
        4, 6, 8,
        3, 5, 7,
        2, 4, 6,
        1, 3, 5, 0
    ],
    'Ascending triads descending'
)


def ascending_triads_first_inversion_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s+2, s+4, s+7] for s in range(length)]) + [length],
        'Ascending triads in first inversion ascending'
    )


def ascending_triads_second_inversion_ascending(length: int) -> Pattern:
    return Pattern(
        flatten([[s-5, s, s+2] for s in range(length)]) + [length],
        'Ascending triads in second inversion ascending'
    )


def descending_triads_first_inversion_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s - 3, s - 5] for s in range(length, 0, -1)]) + [0],
        'Descending triads in first inversion descending'
    )


def descending_triads_second_inversion_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s - 3, s, s+2] for s in range(length, 0, -1)]) + [0],
        'Descending triads in second inversion descending'
    )


def ascending_triads_descending(length: int) -> Pattern:
    return Pattern(
        flatten([[s, s + 2, s + 4] for s in range(length, 0, -1)]) + [0],
        'Ascending triads descending'
    )


def clb_scale_pattern_ascending() -> Pattern:
    return Pattern(
        flatten([[s, s + 1, s + 2, s + 3, s + 4, s + 3, s + 2, s] for s in range(7)]) + [7],
        'ChadLB ascending scale exercise'
    )

def clb_scale_pattern_descending() -> Pattern:
    return Pattern(
        flatten([[s, s + 1, s + 2, s + 3, s+2, s+1, s, s - 2 ] for s in range(7, 0, -1)]) + [0],
        'ChadLB ascending scale exercise'
    )

def blues_workout_1() -> list[Pattern]:
    return [
        p(len(BLUES)) for p in [
            ascending,
            descending,
            down_to_root,
            up_to_root,
            three_notes_ascending,
            three_notes_descending,
            three_descending_notes_ascending,
            three_ascending_notes_descending,
        ]
    ]


def mode_workout(mode_length: int) -> list[Pattern]:
    return [
        [TUNE_IN_PATTERN] + 
        p(mode_length) for p in [
            ascending,
            descending,
            down_to_root,
            up_to_root,
            three_notes_ascending,
            three_notes_descending,
            three_descending_notes_ascending,
            three_ascending_notes_descending,
            ascending_thirds_ascending,
            descending_thirds_descending,
            ascending_triads_ascending,
            descending_triads_descending,
            descending_triads_ascending,
            ascending_triads_descending,
        ]
    ]


def arpeggio_workout(mode_length: int) -> list[Pattern]:
    return [
        p(mode_length) for p in [
            ascending_triads_ascending,
            descending_triads_descending,
            ascending_triads_descending,
            descending_triads_ascending,
            ascending_triads_first_inversion_ascending,
            descending_triads_first_inversion_descending,
            ascending_triads_second_inversion_ascending,
            descending_triads_second_inversion_descending,
        ]
    ]

clb_scale_workout = [
        clb_scale_pattern_ascending(),
        clb_scale_pattern_descending(),
    ]
