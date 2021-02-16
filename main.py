import os
import subprocess
from collections import namedtuple

import eyed3

from solfege.lib.pattern import *
from solfege.exercises.scales import IONIAN, modes_of_major, modes_of_minor
from solfege.exercises.exercises import ASCENDING_THIRDS_ASCENDING, DOWN_TO_ROOT, MODE_WORKOUT, TUNE_IN_PATTERN

instrument = namedtuple('instrument', ['name', 'midi_number'])

def makedirs_if_not_exists(path: str):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def make_tune_in_patterns(instrument, root, modes, modes_name):
    print('FOO', modes_name, root)
    for i, s in enumerate(modes):
        mode_root = note_for_step(modes[0], root, i)
        print('MODE_ROOT', mode_root)
        while mode_root < UPRIGHT_BASS_LOWEST:
            mode_root += OCTAVE
        pattern_notes = make_pattern_notes(s, TUNE_IN_PATTERN, mode_root)
        print(i, s._name, TUNE_IN_PATTERN._name, pattern_notes, note_name(mode_root))
        messages = make_messages(pattern_notes, TIME_DELTA)
        temp_dirname = os.path.join('output', f'{TUNE_IN_PATTERN._name}-{modes_name}')
        mp3_dirname = os.path.join('output', 'mp3', f'{TUNE_IN_PATTERN._name}-{modes_name}-{instrument.name}')
        makedirs_if_not_exists(temp_dirname)
        makedirs_if_not_exists(mp3_dirname)
        filename = f'{TUNE_IN_PATTERN._name}-{note_name(mode_root)}-{s._name}-{instrument.name}'
        mid_filepath = os.path.join(temp_dirname, f'{filename}.mid')
        wav_filepath = os.path.join(temp_dirname, f'{filename}.wav')
        mp3_filepath = os.path.join(mp3_dirname, f'{filename}.mp3')
        make_file(messages, mid_filepath, instrument.midi_number)
        wav_filepath = f'{mid_filepath[:-4]}.wav'
        subprocess.run(['timidity', mid_filepath, '-Ow', '-o', wav_filepath])
        subprocess.run(['ffmpeg', '-y', '-i', wav_filepath,
                        mp3_filepath], capture_output=True, check=True)
        f = eyed3.load(mp3_filepath)
        album_name = f'Tune-in pattern 1 - {modes_name} - {instrument.name}'
        f.tag.album = album_name
        f.tag.title = filename
        f.tag.artist = 'Peter Varshavsky'
        f.tag.track_num = i + 1
        f.tag.save()


def make_drills(instrument, root):
    scales = {i: make_mode(IONIAN, i, name)
              for i, name in MODES_OF_MAJOR.items()}
    for i, s in scales.items():
        mode_root = note_for_step(IONIAN, root, i)
        while mode_root < UPRIGHT_BASS_LOWEST:
            mode_root += OCTAVE
        # tune-in-pattern
        # pattern_notes = make_pattern_notes(s, TUNE_IN_PATTERN, mode_root)
        # print(s._name, 'tune-in', pattern_notes)
        # messages = make_messages(pattern_notes, TIME_DELTA)
        # dirname = os.path.join('output', TUNE_IN_PATTERN._name)
        # try:
        #     os.makedirs(dirname)
        # except FileExistsError:
        #     pass
        # filename = f'{TUNE_IN_PATTERN._name}-{note_name(mode_root)}-{s._name}.mid'
        # mid_filepath = os.path.join(dirname, filename)
        # make_file(messages, mid_filepath)
        # wav_filepath = f'{mid_filepath[:-4]}.wav'
        # subprocess.Popen(['timidity', mid_filepath, '-Ow', '-o', wav_filepath])

        # other patterns
        for track_number, p in enumerate(MODE_WORKOUT, 1):
            # if s._name.lower() != IONIAN._name.lower():
            #     continue
            # if p._name != DOWN_TO_ROOT._name:
            #     continue
            pattern_notes = make_pattern_notes(s, p, mode_root)
            messages = make_messages(pattern_notes, TIME_DELTA)
            filename = f'{track_number}-{p._name}-{note_name(mode_root)}-{s._name}-{instrument.name}'
            output_dir = 'output'
            album_dir = f'{s._name}-{instrument.name}'
            temp_dirname = os.path.join(output_dir, album_dir)
            mp3_dirname = os.path.join(output_dir, 'mp3', album_dir)
            try: 
                os.makedirs(mp3_dirname)
                os.makedirs(temp_dirname)
            except FileExistsError:
                pass
            mid_filepath = os.path.join(temp_dirname, f'{filename}.mid')
            wav_filepath = os.path.join(temp_dirname, f'{filename}.wav')
            mp3_filepath = os.path.join(mp3_dirname, f'{filename}.mp3')
            make_file(messages, mid_filepath, instrument.midi_number)
            subprocess.run(['timidity', mid_filepath, '-Ow', '-o',
                            wav_filepath], capture_output=True, check=True)
            subprocess.run(['ffmpeg', '-y', '-i', wav_filepath,
                            mp3_filepath], capture_output=True, check=True)
            f = eyed3.load(mp3_filepath)
            album_name = f'{s._name.capitalize()} drill in {note_name(mode_root).capitalize()} - {instrument.name}'
            f.tag.album = album_name
            f.tag.title = filename
            f.tag.artist = 'Peter Varshavsky'
            f.tag.track_num = track_number
            f.tag.save()


def main():
    bass = instrument('bass', ACOUSTIC_BASS)
    bass_root = MIDDLE_C - 3 * OCTAVE

    piano = instrument('piano', PIANO)
    piano_root = MIDDLE_C - OCTAVE

    # make_drills(bass, bass_root)
    # make_drills(piano, piano_root)

    make_tune_in_patterns(piano, piano_root, modes_of_major, 'modes-of-major')
    make_tune_in_patterns(piano, piano_root, modes_of_minor, 'modes-of-minor')


if __name__ == '__main__':
    main()
