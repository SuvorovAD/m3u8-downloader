import subprocess
import urllib.request
import os
import platform


encoding = 'utf-8'

url = input("Введите ссылку m3u8 файла:  ")
name = input("Введите имя файла:  ")
urllib.request.urlretrieve(url, f'{os.getcwd()}/1.m3u8')

with open ("1.m3u8", "r") as file:
    lines=file.readlines()
print(lines[-1])

head, sep, tail = lines[-1].partition('?')
link = head
os.remove(f'{os.getcwd()}/1.m3u8')

os = platform.system()
if os == 'Windows':
    command = f".\\ffmpeg.exe -i  \"{link}\" -c copy -bsf:a aac_adtstoasc \"{name}.mp4\" "
if  os == 'Linux' or os == 'Darwin':
    command = f'ffmpeg -i \"{link}\" -c copy -bsf:a aac_adtstoasc \"{name}.mp4\" '

subprocess.call(command, shell=True)
