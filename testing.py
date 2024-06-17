from pytube import YouTube
from tkinter import *
# import tkinter as tk
import os
import customtkinter

# def on_progress(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage_of_completion = (bytes_downloaded / total_size) * 100
#     progress.set(percentage_of_completion)
#     root.update_idletasks()

def download_vdo():
    url = entry_url.get()
    if url:
        if not os.path.exists("download"):
            os.makedirs("download")     
        yt = YouTube(url)
        option= input_option.get()
        if option == "mp3":
            yt.streams.filter(only_audio=True).first().download(output_path="downloads")
            status_label.config(text="Download completed!")
            print("Download completed!")
        else:
            yt.streams.get_highest_resolution().download(output_path="downloads")
            status_label.config(text="Download completed!", fg="green")
            print("Download completed!")
    else:
        status_label.config(text="Please enter a valid YouTube URL!", fg = "red")
        print("Invalid URL!")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress.set(float(percentage_of_completion)/100)
    progress.config(text=per + "%")
    progress.update()  

root = customtkinter.CTk()
root.title("Video Downloader")
root.geometry("650x500")

url = Label(root, text = 'Enter your url link: ').pack()
entry_url = Entry(root, width = 60)
entry_url.pack(pady = 10)
#input option for downloading audio or video
input_option = StringVar()
input_option.set(" ")

radio_audio = Radiobutton(root, text="Audio", variable=input_option, value="audio")
radio_audio.pack(pady=5)
radio_video = Radiobutton(root, text="Video", variable=input_option, value="video")
radio_video.pack(pady=10)

download_button = Button(root, text="Download Now!", command = download_vdo, width = 60).pack(pady = 10)

progress = Label(root, text='0%')
progress.pack()

progress = customtkinter.CTkProgressBar(root, width=400)
progress.pack(pady=10)
progress.set(50)

status_label = Label(root, text="")
status_label.pack(pady = 10)

root.mainloop()