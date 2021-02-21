import speech_recognition as sr
import wave, os, glob
from langdetect import detect, lang_detect_exception
from langid.langid import LanguageIdentifier, model
from shutil import copyfile
import subprocess
import sys

# Options
path = "audio_files" # base files folder
output = "output" # output folder
accuracy = 0.9999999 # required accuracy (Best to leave this at default)

# Check if the user wants to convert their files to WAV format.
answer = None 
while answer not in ("y", "n", "yes", "no"): 
   answer = input("Files need to be in WAV format, do you want to convert all files in '" + path + "' to WAV format? [y, n] ") 
   if answer == "y" or answer == "yes": 
      print("Converting files to WAV format...")
      exec(open("tools/convert.py").read())
   elif answer == "n" or answer == "no": 
      print("Skipping WAV format conversion...")
   else: 
      print("Please enter yes or no.") 

# Do the audio to language conversion.
r = sr.Recognizer()
language_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

wav_files = glob.glob(os.path.join(path, '*.wav'))
files_length = len(wav_files)
current = 0

# Check if theres files to convert.
if files_length == 0:
   sys.exit("[FAILED] No files in WAV format were found in the '" + path + "' directory. Try rerunning the script and saying yes to conversion.")

for filename in wav_files:
   current_file_string = "(" + str(current) + " / " + str(files_length) + ")"
   file_audio = sr.AudioFile(filename)
   with file_audio as source:
      try:
         audio_text = r.recognize_google(r.record(source))
         global_unsure_dir = output + "//_unsure"

         lang, score = language_identifier.classify(audio_text)
         lang2 = detect(audio_text)

         out_dir = output + "//" + lang
         out_unsure_dir = output + "//" + lang + "//_unsure"
         head, tail = os.path.split(filename)
         
         # Check the accuracy and double check with other language interpreter.
         if score >= accuracy or lang2 == lang:
            if not os.path.exists(out_dir):
               os.makedirs(out_dir)
            copyfile(filename, out_dir + "//" + tail)
            print(current_file_string + " [SUCCESS] Detected " + lang + " copying to '" + out_dir + "'.")
         else:
            if not os.path.exists(out_unsure_dir):
               os.makedirs(out_unsure_dir)
            copyfile(filename, out_unsure_dir + "//" + tail)
            print(current_file_string + " [MINOR SUCCESS] Mostly detected " + lang + " copying to '" + out_unsure_dir + "'.")
      except (sr.UnknownValueError, lang_detect_exception.LangDetectException):
            if not os.path.exists(global_unsure_dir):
               os.makedirs(global_unsure_dir)
            print(current_file_string + " [FAILED] Didn't detect a language with high enough probability. Copying to '" + global_unsure_dir + "'.")
   current += 1
