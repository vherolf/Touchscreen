#!/bin/bash

source ./venv/bin/activate

pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/two_images.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/matching_to_sample.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/go_nogo.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/random_position.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/sequential_learning.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile Trainings/two_images_keyboard_input.py
