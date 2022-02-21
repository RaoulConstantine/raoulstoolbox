# BATCH CONVERT MIDI TO AUDIO
import os
from midi2audio import FluidSynth
def batch_midi_convert(midi_path, target_path):
    """
    Requires directory path to directory containing
    midi files and target path
    to store converted audio
    """
    fs = FluidSynth('MuseScore_General.sf2')
    for filename in os.listdir(midi_path):
        filename = filename.strip('.mid')
        print(filename)
        fs.midi_to_audio(f'{midi_path}/{filename}.mid', f'{target_path}]/{filename}.wav')
    return print("Batch conversion completed")
