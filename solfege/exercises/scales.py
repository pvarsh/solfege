from solfege.lib.pattern import Scale

IONIAN = Scale(
    [2, 2, 1, 2, 2, 2, 1],
    "ionian"
)

ionian = IONIAN
dorian = IONIAN.mode(2, 'dorian')
phrygian = IONIAN.mode(3, 'phrygian')
lydian = IONIAN.mode(4, 'lydian')
mixolydian = IONIAN.mode(5, 'mixolydian')
aeolian = IONIAN.mode(6, 'aeolian')
locrian = IONIAN.mode(7, 'locrian')

modes_of_major = [
    ionian,
    dorian,
    phrygian,
    lydian,
    mixolydian,
    aeolian,
    locrian,
]

BLUES = Scale(
    [3, 2, 1, 1, 3, 2],
    'blues'
)

KLEZMER = Scale(
    [1, 3, 1, 2, 1, 2, 2],
    'klezmer'
)
