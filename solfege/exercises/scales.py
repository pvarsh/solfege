from solfege.lib.pattern import Scale

IONIAN = Scale(
    [2, 2, 1, 2, 2, 2, 1],
    "ionian"
)

ionian = IONIAN
dorian = IONIAN.mode(1, 'dorian')
phrygian = IONIAN.mode(2, 'phrygian')
lydian = IONIAN.mode(3, 'lydian')
mixolydian = IONIAN.mode(4, 'mixolydian')
aeolian = IONIAN.mode(5, 'aeolian')
locrian = IONIAN.mode(6, 'locrian')

modes_of_major = [
    ionian,
    dorian,
    phrygian,
    lydian,
    mixolydian,
    aeolian,
    locrian,
]

modes_of_minor = [
    aeolian,
    locrian,
    ionian,
    dorian,
    phrygian,
    lydian,
    mixolydian,
]

BLUES = Scale(
    [3, 2, 1, 1, 3, 2],
    'blues'
)

KLEZMER = Scale(
    [1, 3, 1, 2, 1, 2, 2],
    'klezmer'
)
