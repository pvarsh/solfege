from collections.abc import Sequence

from mido import Message
from mido.midifiles.midifiles import MidiFile
from mido.midifiles.tracks import MidiTrack

MIDDLE_C = 60
NOTE_ON = "note_on"
NOTE_OFF = "note_off"
TIME_DELTA = 400
ACOUSTIC_BASS = 32
OCTAVE = 12
MAX_VELOCITY = 127
UPRIGHT_BASS_LOWEST = 28

MODES_OF_MAJOR = {
    1: 'ionian',
    2: 'dorian',
    3: 'phrygian',
    4: 'lydian',
    5: 'mixolydian',
    6: 'aeolian',
    7: 'locrian',
}

NOTE_NAMES = ['c', 'c#/db', 'd', 'd#/eb', 'e',
              'f', 'f#/gb', 'g', 'g#/ab', 'a', 'a#/bb', 'b']


def note_name(midi_note: int):
    note_names = {(60+i): name for i, name in enumerate(NOTE_NAMES)}
    return note_names[MIDDLE_C + (midi_note - MIDDLE_C) % len(NOTE_NAMES)]


class Note:
    def __init__(self, name: str) -> None:
        self._name = name

    def add(self, interval: int):
        if self._name == "c":
            self._name = "d"


class Pattern:
    def __init__(self, steps: Sequence[int], name: str):
        self._steps = steps
        self._name = name


class Scale:
    def __init__(self, intervals: Sequence[int], name: str):
        self._intervals = intervals
        self._name = name

    def __len__(self):
        return len(self._intervals)

    def mode(self, step: int, name: str):
        intervals = [self._intervals[(step + i) % len(self._intervals)]
                     for i in range(len(self._intervals))]
        return intervals


def make_scale_file(scale: Scale, root: int):
    root_on = Message(type=NOTE_ON, note=root, time=0)
    root_off = Message(type=NOTE_OFF, note=root, time=TIME_DELTA)
    messages = [root_on, root_off]
    for i, interval in enumerate(scale._intervals):
        previous_index = i*2
        previous = messages[previous_index]
        msg_on = Message(type=NOTE_ON, note=previous.note +
                         interval, time=TIME_DELTA)
        msg_off = Message(type=NOTE_OFF, note=previous.note +
                          interval, time=TIME_DELTA)
        messages.append(msg_on)
        messages.append(msg_off)

    filename = '{}_{}.mid'.format(note_name(root), scale._name)
    make_file(messages, filename)


def make_pattern_notes(scale: Scale, pattern: Pattern, root: int) -> list[int]:
    extended_scale = _make_extended_scale(scale, pattern, root)
    pattern_notes = [extended_scale[step-1] for step in pattern._steps]
    return pattern_notes


def make_messages(notes: Sequence[int], time_delta: int):
    messages = list[Message]()
    for note in notes:
        print(f"Note: {note}")
        messages.append(Message(type=NOTE_ON, velocity=MAX_VELOCITY-10, note=note, time=time_delta))
        messages.append(Message(type=NOTE_OFF, velocity=MAX_VELOCITY-100, note=note, time=time_delta))
    return messages


def make_file(messages: Sequence[Message], filename: str) -> None:
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=ACOUSTIC_BASS, time=0))
    for msg in messages:
        track.append(msg)
    mid.save(filename)


def _make_extended_scale(scale, pattern, root) -> Sequence[int]:
    pattern_max = max(pattern._steps)
    extended_scale = [root]
    print(f'root {root}')
    for i in range(pattern_max - 1):
        next_step = extended_scale[i] + scale._intervals[i % len(scale)]
        extended_scale.append(next_step)
    return extended_scale


def make_mode(scale: Scale, step: int, name="") -> Scale:
    name = name or f'{scale._name}-{step}-mode'
    step_index = step - 1  # steps are 1-based, indices are 0-based
    mode_intervals = []
    for i in range(len(scale)):
        mode_intervals.append(scale._intervals[(step_index + i) % len(scale)])
    return Scale(mode_intervals, name=name)



def note_for_step(scale: Scale, root: int, step: int) -> int:
    step_index = step - 1
    step_note = root
    for i in range(step_index):
        step_note += scale._intervals[i % len(scale)]
    print(f'scale: {scale} root: {root} step: {step} step_note: {step_note}')
    return step_note


if __name__ == "__main__":
    main()
