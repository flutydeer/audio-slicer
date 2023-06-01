# Audio Slicer

A simple GUI application that slices audio with silence detection.

[中文文档](./README.zh-CN.md)

## Screenshots

![image](./screenshot/../screenshots/screenshot_dark.jpg)

The app also has a light theme.

## Usage

### Windows

- Download and extract the latest release [here](https://github.com/flutydeer/audio-slicer/releases).

- Run "slicer-gui.exe".

### MacOS & Linux

- Clone the repository.

- Run the following command to install requirements:

```shell
pip install -r requirements.txt
```

- Run the following command to launch GUI:

```Shell
python slicer-gui.py
```

Just simply add your audio files to the task list by clicking the "Add Audio Files..." button or dragging and drop them to the window, click the "Start" button and wait for it to finish. The progress bar cannot indicate the progress of individual tasks, so it keeps 0% until finished when there is only 1 task in the task list.
## Algorithm

### Silence detection

This application uses RMS (root mean score) to measure the quiteness of the audio and detect silent parts. RMS values of each frame (frame length set as **hop size**) are calculated and all frames with an RMS below the **threshold** will be regarded as silent frames.

### Audio slicing

Once the valid (sound) part reached **min length** since last slice and a silent part longer than **min interval** are detected, the audio will be sliced apart from the frame(s) with the lowest RMS value within the silent area. Long silence parts may be deleted.



## Parameters

### Threshold

The RMS threshold presented in dB. Areas where all RMS values are below this threshold will be regarded as silence. Increase this value if your audio is noisy. Defaults to -40.

### Minimum Length

The minimum length required for each sliced audio clip, presented in milliseconds. Defaults to 5000.

### Minimum Interval

The minimum length for a silence part to be sliced, presented in milliseconds. Set this value smaller if your audio contains only short breaks. The smaller this value is, the more sliced audio clips this application is likely to generate. Note that this value must be smaller than min_length and larger than hop_size. Defaults to 300.

### Hop Size

Length of each RMS frame, presented in milliseconds. Increasing this value will increase the precision of slicing, but will slow down the process. Defaults to 10.

### Maximum Silence Length

The maximum silence length kept around the sliced audio, presented in milliseconds. Adjust this value according to your needs. Note that setting this value does not mean that silence parts in the sliced audio have exactly the given length. The algorithm will search for the best position to slice, as described above. Defaults to 1000.

## Performance

This application runs over 400x faster than real-time on an Intel i7 8750H CPU. Speed may vary according to your CPU and your disk.
