#!/bin/bash

source ./venv/bin/activate

pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile two_images.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile matching_to_sample.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile go_nogo.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile random_position.py
pyinstaller --add-data Training_Stimuli:Training_Stimuli --add-data SoundEffects:SoundEffects  --windowed --onefile sequential_learning.py
