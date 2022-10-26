from pydub import AudioSegment
import os as path
# # files                                                                       
src = "audio.ogg"
dst = "test.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_ogg("audio.ogg")
audSeg.export(dst, format="wav")
