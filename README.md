## What does this repository contain?
This repository contains a small code of face detection using Haar Cascade. This can be done both real time and on a particular video (downloaded or from youtube)

## How to use this repository?
Simply downlaod requirements.txt and run face_detection.py.

	pip install -r requirements.txt

You may use your own xml file for a different object.

To switch between youtube and real time, change the function call in "detection" cap = realtime() or cap = youtube_url()

Output from RealTime:
![alt text](https://github.com/shivekchhabra/face_detection/blob/master/Output.png)


Output from YouTube:
![alt text](https://github.com/shivekchhabra/face_detection/blob/master/youtube_output.png)
