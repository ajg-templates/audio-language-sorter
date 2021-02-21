import os
from pydub import AudioSegment


print("[WARNING] Console printing may not be accurate dependent on the amount of files.")

path = "audio_files"
audio_files = os.listdir(path)
for file in audio_files:
    name, ext = os.path.splitext(file)
    try:
        if ext != ".wav": 
            output_dir = path + "//"
            mp3_sound = AudioSegment.from_file(output_dir + file, ext.replace(".", ""))
            mp3_sound.export(output_dir + "{0}.wav".format(name), format="wav")
        print("[SUCCESS] Converted '" + file + "' to '" + "{0}.wav'.".format(name))
    except:
        print("Couldn't convert '" + file + "'.")