<p align="center"><img width=12.5% src="https://i.ibb.co/K6RrTjc/logo.png"></p>

## Basic Overview

This is just a simple python script to sort a large amoung of audio files by language spoken in them.
This also includes an audio conversion script for converting the base files to WAV format.
The tool as far as I can tell has about a 87/100 average accuracy.

## Usage Instructions

1) Run `pip install -r requirements.txt` to install the required modules.

2) Place all of your files of any format into the `audio_files` folder. If it doesnt exist, create it.

3) Run `main.py` and select `y` if you need to convert your files.

## Folder Scructure
  `audio_files` - Input files, these can be in any format.
  
  `output` - Where the sorted files go into subfolders labeled with the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1 codes</a>.
  
  `tools` - Where I store the extra python scripts for converting files.
  
  `main.py` - The main script you run to start the tool.

## Options

You can change the accuracy and directories at the top of the `main.py` directory.
