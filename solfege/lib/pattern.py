from __future__ import annotations
from collections.abc import Sequence

from mido import Message
from mido.midifiles.midifiles import MidiFile
from mido.midifiles.tracks import MidiTrack

MIDDLE_C = 60
NOTE_ON = "note_on"
NOTE_OFF = "note_off"
TIME_DELTA = 500
PIANO = 0
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

NOTE_NAMES = ['c', 'c#-db', 'd', 'd#-eb', 'e',
              'f', 'f#-gb', 'g', 'g#-ab', 'a', 'a#-bb', 'b']


def note_name(midi_note: int):
    note_names = {(60+i): name for i, name in enumerate(NOTE_NAMES)}
    return note_names[MIDDLE_C + (midi_note - MIDDLE_C) % len(NOTE_NAMES)]


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

    def mode(self, step: int, name: str) -> Scale:
        return Scale(self._intervals[step:] + self._intervals[:step], name)


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
    make_file(messages, filename, PIANO)


def make_pattern_notes(scale: Scale, pattern: Pattern, root: int) -> list[int]:
    # extended_scale = _make_extended_scale(scale, pattern, root)
    scale_notes = make_scale_notes(scale, pattern, root)
    pattern_notes = [scale_notes[step] for step in pattern._steps]
    return pattern_notes


def make_messages(notes: Sequence[int], time_delta: int):
    messages = list[Message]()
    for note in notes:
        messages.append(Message(type=NOTE_ON, velocity=MAX_VELOCITY-10, note=note, time=time_delta))
        messages.append(Message(type=NOTE_OFF, velocity=MAX_VELOCITY-100, note=note, time=time_delta))
    return messages


def make_file(messages: Sequence[Message], filename: str, instrument: int) -> None:
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=instrument, time=0))
    for msg in messages:
        track.append(msg)
    mid.save(filename)


def _make_extended_scale(scale, pattern, root) -> Sequence[int]:
    pattern_max = max(pattern._steps)
    extended_scale = [root]
    for i in range(pattern_max - 1):
        next_step = extended_scale[i] + scale._intervals[i % len(scale)]
        extended_scale.append(next_step)
    return extended_scale

def make_scale_notes(scale: Scale, pattern: Pattern, root) -> dict[int, int]:
    scale_notes = dict[int, int]()
    min_step = min(pattern._steps)
    max_step = max(pattern._steps)
    scale_notes[0] = root
    note = root
    for i in range(-1, min_step - 1, -1):
        note = note - scale._intervals[i % len(scale)]
        scale_notes[i] = note
    note = root
    for i in range(1, max_step + 1):
        note = note + scale._intervals[(i-1) % len(scale)]
        scale_notes[i] = note
    return scale_notes

def make_mode(scale: Scale, step: int, name="") -> Scale:
    name = name or f'{scale._name}-{step}-mode'
    step_index = step - 1  # steps are 1-based, indices are 0-based
    mode_intervals = []
    for i in range(len(scale)):
        mode_intervals.append(scale._intervals[(step_index + i) % len(scale)])
    return Scale(mode_intervals, name=name)


def note_for_step(scale: Scale, root: int, step: int) -> int:
    step_note = root
    for i in range(step):
        index = i % len(scale)
        step_note += scale._intervals[index]
    return step_note
