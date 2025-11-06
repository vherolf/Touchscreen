# Touch screen learning tool


## Installation

```
git clone git@github.com:vherolf/Touchscreen.git
cd Toucscreen
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Running

for example
```
source venv/bin/activate
python two_images.py
```

## Building executables

```
bash build.sh
```

## Deploy on Linux

* clone the and install every thing in a user folder
* use autostart to run the ```touchscreen.sh```

> [!TIP]
> deploying on a Raspberry than activate "overlay file" to prevent SD card corruption.
> send log files per internet or add a usb stick.


## Build & Starting as systemd service as user

```
bash ./build.sh

mkdir -p ~/bin

cp dist/* ~/bin/

cp touchscreen.service ~/.config/systemd/user

systemctl --user daemon-reload && systemctl --user enable touchscreen.service && systemctl --user start touchscreen.service
``` 