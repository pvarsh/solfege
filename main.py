import os
import subprocess
import time

import eyed3
import music_tag

from solfege.lib.pattern import *
from solfege.exercises.scales import IONIAN 
from solfege.exercises.exercises import ASCENDING_THIRDS_ASCENDING, MODE_WORKOUT, TUNE_IN_PATTERN 

def make_tune_in_patterns():
    scales = {i: make_mode(IONIAN, i, name)
              for i, name in MODES_OF_MAJOR.items()}
    for i, s in scales.items():
        root = note_for_step(IONIAN, MIDDLE_C - 3*OCTAVE, i)
        while root < UPRIGHT_BASS_LOWEST:
            root += OCTAVE
        # tune-in-pattern
        # pattern_notes = make_pattern_notes(s, TUNE_IN_PATTERN, root)
        # print(s._name, 'tune-in', pattern_notes)
        # messages = make_messages(pattern_notes, TIME_DELTA)
        # dirname = os.path.join('output', TUNE_IN_PATTERN._name)
        # try: 
        #     os.makedirs(dirname)
        # except FileExistsError:
        #     pass
        # filename = f'{TUNE_IN_PATTERN._name}-{note_name(root)}-{s._name}.mid'
        # mid_filepath = os.path.join(dirname, filename)
        # make_file(messages, mid_filepath)
        # wav_filepath = f'{mid_filepath[:-4]}.wav'
        # subprocess.Popen(['timidity', mid_filepath, '-Ow', '-o', wav_filepath])

        # other patterns
        for track_number, p in enumerate(MODE_WORKOUT, 1):
            # if s._name != 'locrian':
            #     continue
            # if p._name != 'up_to_root':
            #     continue
            print(p._name, s._name)
            pattern_notes = make_pattern_notes(s, p, root)
            messages = make_messages(pattern_notes, TIME_DELTA)
            print(messages)
            filename = f'{track_number}-{p._name}-{note_name(root)}-{s._name}'
            output_dir = 'output'
            album_dir = s._name
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
            make_file(messages, mid_filepath)
            subprocess.Popen(['timidity', mid_filepath, '-Ow', '-o', wav_filepath])
            time.sleep(1)
            subprocess.Popen(['ffmpeg', '-i', wav_filepath, mp3_filepath])
            time.sleep(1)
            f = eyed3.load(mp3_filepath)
            print('FILE: ', f)
            album_name = f'{s._name.capitalize()} Workout in {note_name(root).capitalize} - low bass'
            f.tag.album = album_name
            f.tag.title = filename[:-4]
            f.tag.artist = 'Peter Varshavsky'
            f.tag.track_num = track_number
            f.tag.save()

            # f = music_tag.load_file(wav_filepath)
            # f['title'] = 'FOO' + filename[:-4] 
            # f['album'] = s._name
            # print('tags', f)
            # f.save()
            # print('LOAD AGAIN:', music_tag.load_file(wav_filepath)['album'])


def main():
    make_tune_in_patterns()

if __name__ == '__main__':
    main()