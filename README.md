# Touch screen learning tool


## Installation

```
Clone Repo

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

Clone the and install every thing in a user folder.


```
cd ./Touchscreen/App

bash build.sh
```

## Deploy on Linux


### Simple start script for testing

edit script for the the App you wanna use and run the ```touchscreen.sh```

### Build & Starting as systemd service as user

Edit ```touchscreen.service``` for which App to start.  

```
cd Touchscreen

mkdir -p ~/bin

cp App/dist/* ~/bin/

cp touchscreen.service ~/.config/systemd/user

systemctl --user daemon-reload && systemctl --user enable touchscreen.service && systemctl --user start touchscreen.service
``` 


> [!TIP]
> deploying on a Raspberry than activate "overlay file" to prevent SD card corruption.
> send log files per internet or add a usb stick.
