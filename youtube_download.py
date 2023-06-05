from __future__ import unicode_literals
import yt_dlp
from yt_dlp.utils import download_range_func
import datetime
import ffmpeg
import os
import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir", type=str, required=True, help='file path of txt')
    parser.add_argument("-t", "--task_option", type=str, required=True, choices=['video', 'audio'], help='video or audio')
    parser.add_argument("-o", "--output_name", type=str, required=True, help='name of person, e.g. LawrenceWong')
    parser.add_argument("-v", "--video_ext", type=str, default='avi')
    parser.add_argument("-a", "--audio_ext", type=str, default='wav')
    args = parser.parse_args()
    return args

def main():
    args = arguments()
    file = open(args.input_dir,'r')
    lines = file.readlines()
    count=0
    for line in lines:
        count+=1
        url, start, end = line.split()
        start_h,start_m,start_s = start.split(':')
        end_h,end_m,end_s = end.split(':')
        count_str = str(count)
        print("count:" +count_str)
        start_int = int(datetime.timedelta(hours=int(start_h),minutes=int(start_m),seconds=int(start_s)).total_seconds())
        end_int = int(datetime.timedelta(hours=int(end_h),minutes=int(end_m),seconds=int(end_s)).total_seconds())

        if args.task_option == 'video':
            filename = f'Youtube_Video/{args.output_name}/{args.output_name}_{count_str}.{args.video_ext}'
            ydl_opts = {
                'format': f'bestvideo[ext={args.video_ext}]+bestaudio[ext={args.audio_ext}]/best[ext={args.video_ext}]/best',
                'download_ranges': download_range_func(None, [(start_int, end_int)]),
                'force_keyframes_at_cuts': True, 
                'outtmpl': filename,
            }
            
        elif args.task_option == 'audio':
            filename=f'Youtube_Audio/{args.output_name}/{args.output_name}_{count_str}.{args.audio_ext}'

            ydl_opts = {
            'format': f'bestaudio[ext={args.audio_ext}]/best',
            'download_ranges': download_range_func(None, [(start_int, end_int)]),
            # for yt links
            'force_keyframes_at_cuts': True, 
            'outtmpl': f'Youtube_Audio/{args.output_name}/{args.output_name}_{count_str}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if os.path.isfile(filename) is False:
                ydl.download([url])

if __name__ == "__main__":
    main()

    

    
