from moviepy.editor import VideoFileClip, concatenate_videoclips
import csv
import os
import glob

in_csv = 'in/csv' # where to look for the csv files
in_vid = 'in/vid' # where to look for the corresponding videos
out_vid = 'out/' # where to save the compiled video

src_csv = []
src_vid = []
timestamp_list = []
clips = []

def timestamp_convert(timestamp):
    sp = timestamp.split(':')
    return (float(sp[0])*60) + float(sp[1])

 # -----------------------
csv_file = 'in/csv/9.csv'
with open(csv_file, newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i, row in enumerate(rdr):
        if not i == 0:
            timestamps = row[0].split(',')
            timestamp_list.append((timestamp_convert(timestamps[0]), timestamp_convert(timestamps[1])))
        
video_file = 'in/vid/9.mp4'
for segment in timestamp_list:
    clip = VideoFileClip(video_file).subclip(segment[0], segment[1]) 
    clips.append(clip)

final = concatenate_videoclips(clips)

final.write_videofile("out/9.mp4")
