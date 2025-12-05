# 
from PySide6.QtCore import QThread, Signal
from Framework.TrainingStimulus import TrainingStimulus
from Framework.ImageStimulusDisplay import ImageStimulusDisplay
from pynput.keyboard import Listener

class KeyboardInputImage(ImageStimulusDisplay):
    keyPressed = Signal()

    def __init__(self, trainingImage: TrainingStimulus, selected, shortcut, imageSize=None, parent=None):
        super(KeyboardInputImage, self).__init__(trainingImage, imageSize, parent)
        self.selected = selected
        self.shortcut = shortcut
        
        self.keyPressed.connect(self.stimulusSelected)

        listener = Listener(on_press=self.on_press)
        listener.start()

    
    def on_press(self, key):
        print(key)
        try:
            if key.char == self.shortcut:
                self.keyPressed.emit()
        except AttributeError:
            return

    def stimulusSelected(self):
        if self.trainingImage is not None:
            self.selected(self.trainingImage)

class WorkerThread(QThread):
    def __init__(self, stimulusSelected, parent=None):
        super().__init__(parent)
        self.stimulusSelected = stimulusSelected

    def run(self):
        self.stimulusSelected()

    