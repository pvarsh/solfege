from solfege.exercises.scales import IONIAN
from solfege.lib.pattern import MIDDLE_C, Pattern, Scale, make_pattern_notes, make_scale_notes

IONIAN = Scale(
        [2, 2, 1, 2, 2, 2, 1],
        "ionian",
    )

# def test_make_pattern_notes():
#     UP_TO_ROOT = Pattern(
#         [
#             8,
#             7, 8,
#             6, 7, 8,
#             5, 6, 7,8 ,
#             4, 5, 6, 7, 8,
#             3, 4, 5, 6, 7, 8,
#             2, 3, 4, 5, 6, 7, 8,
#             1, 2, 3, 4, 5, 6, 7, 8,
#             ],
#         'Up to root from every step'
#     )
#     expected = [72, 71, 72, 69, 71, 72, 67, 69, 71, 72, 65, 67, 69, 71, 72, 64, 65, 67, 69, 71, 72, 62, 64, 65, 67, 69, 71, 72, 60, 62, 64, 65, 67, 69, 71, 72]
#     notes = make_pattern_notes(IONIAN, UP_TO_ROOT, 60)
#     assert notes == expected

def test_make_scale_notes():
    p = Pattern(
        [-8, -7, -4, -2, -1, 0, 1, 2, 7],
        'test_pattern'
    )
    scale_notes = make_scale_notes(IONIAN, p, MIDDLE_C)
    expected = {
        -8: 47, # ti
        -7: 48, # do
        -4: 53, # fa
        -2: 57, # la
        -1: 59, # ti
        0: 60, # do
        1: 62, # re
        2: 64, # mi
        7: 72, # do
        }
    for step in expected:
        assert expected[step] == scale_notes[step]
