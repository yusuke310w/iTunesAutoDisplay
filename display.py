import configparser
import tkinter as tk
import time
import math

from MusicControl import MusicControl
 

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
c = config_ini["DEFAULT"]
m = MusicControl()
root = tk.Tk()
root.title(c["Title"])
root.geometry(f"{c["Width"]}x{c["Height"]}")

# operate = tk.Label(root, text="タイマー：Enter\n曲情報取得：↓\n一時停止・再生：↑\n次の曲：→\n前の曲：←")
# operate.pack()
playlist = tk.Label(root, text=f"プレイリスト：{m.playlist}", font=("family", 20))
# playlist.grid(row=0, column=0)
playlist.pack(padx=20, pady=5,anchor=tk.W)
name = tk.Label(root, text="", font=("family", 56), wraplength=int(c["Width"])-50)
# name.grid(padx=20, pady=5, row=0, column=0, columnspan=12)
name.pack(padx=20, pady=5,anchor=tk.W)
artist = tk.Label(root, text="", font=("family", 40), wraplength=int(c["Width"])-50)
# artist.grid(padx=20, pady=5, row=2, column=2)
artist.pack(padx=20, pady=5,anchor=tk.W)
album = tk.Label(root, text="", font=("family", 48), wraplength=int(c["Width"])-50)
# album.grid(row=3, column=1, sticky=tk.W+tk.E)
album.pack(padx=20, pady=5,anchor=tk.W)
# year = tk.Label(root, text="", font=("family", 36))
# year.pack(padx=20, pady=5)
# genre = tk.Label(root, text="", font=("family", 36))
# genre.pack(padx=20, pady=5)
genre = tk.Label(root, text="", font=("family", 36))
genre.pack(padx=20, pady=5,anchor=tk.W)
# composer = tk.Label(root, text="")
# composer.pack(padx=20, pady=5)
comment = tk.Label(root, text="", wraplength=int(c["Width"])-50)
comment.pack(padx=20, pady=5,anchor=tk.W)
timer = tk.Label(root, text="", font=("family", 40))
timer.pack()
def get_info():
    name.config(text=m.name)
    artist.config(text=m.artist)
    album.config(text=m.album)
    # year.config(text=m.year)
    # genre.config(text=m.genre)
    genre.config(text=f"{m.year} {m.genre}")
    # composer.config(text=m.composer)
    comment.config(text=m.comment)
    
btnCanvas = tk.Canvas(root, width=500, height=100)
# btnCanvas.pack()
def pause():
    m.pause()
pausebtn = tk.Button(btnCanvas, text="一時停止・再生", command=pause)
pausebtn.place(x=10, y=10)
pausebtn.pack()
def play():
    m.play()
# playbtn = tk.Button(btnCanvas, text="再生", command=play)
# playbtn.pack()
def next():
    m.next_track()
def prev():
    m.prev_track()
nextbtn = tk.Button(btnCanvas, text="次へ", command=next)
nextbtn.place(x=100, y=10)
nextbtn.pack()
prevbtn = tk.Button(btnCanvas, text="戻る", command=next)
prevbtn.place(x=150, y=10)
prevbtn.pack()
getbtn = tk.Button(btnCanvas, text="取得", command=get_info)
getbtn.place(x=200, y=10)
getbtn.pack()
if __name__ == "__main__":
    def key_event(e):
        if e.keysym == "p":
            play()
        elif e.keysym == "Up":
            pause()
        elif e.keysym == "Right":
            next()
            # get_info()
        elif e.keysym == "Left":
            prev()
            get_info()
        elif e.keysym == "Down":
            get_info()
        # elif e.keysym == "Return":

    root.bind("<KeyPress>", key_event)
    root.mainloop()
