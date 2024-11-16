from gtts import gTTS
from pygame import mixer
from pypdf import PdfReader
from tkinter import Tk, Text, Button, filedialog, END, Label
import os


class Putfile():

    def __init__(self, window):
        self.window = window
        self.window.config(width=500, height=500)
        self.window.title("將純文字轉換成語音檔案")

        self.title = Label(text="輸入文字 或 上傳ＰＤＦ檔案")
        self.title.place(x=160, y=20)

        self.textarea = Text(height=20, width=50)
        self.textarea.place(x=80, y=80)

        self.read_botton_zh = Button(text="閱讀中文", command=self.read_zh)
        self.read_botton_zh.place(x=100, y=380)
        self.read_botton_en = Button(text="閱讀英文", command=self.read_en)
        self.read_botton_en.place(x=100, y=410)
        self.add_botton = Button(text="新增檔案", command=self.add)
        self.add_botton.place(x=300, y=400)

    def add(self):
        self.file = filedialog.askopenfilename()
        if self.file:
            self.reader = PdfReader(self.file)
            self.context = ""
            for page in self.reader.pages:
                self.context += page.extract_text()
            self.textarea.insert(1.0, self.context)
        else:
            self.context = "無效的資料"
            self.textarea.insert(1.0, self.context)

    def read_zh(self):
        self.langue = "zh-tw"
        self.context = self.textarea.get("1.0", END)
        if self.context:
            Mp3reader(self.context, self.langue)

    def read_en(self):
        self.langue = "en"
        self.context = self.textarea.get("1.0", END).strip()
        if self.context:
            Mp3reader(self.context, self.langue)


class Pdfreader():
    def __init__(self, CONTEXT):

        self.mp3 = "temporary.mp3"
        self.context = CONTEXT
        for row in self.context:
            try:
                self.text = gTTS(text=row, lang="zh")
                self.text.save(self.mp3)

                mixer.init()
                mixer.music.load(self.mp3)

                mixer.music.play()
                while mixer.music.get_busy():
                    continue

                os.remove(self.mp3)
            except:
                continue


class Mp3reader():

    def __init__(self, MP3, LANGUE):
        self.mp3 = "temporary.mp3"
        self.context = MP3
        self.langue = LANGUE
        self.convert_to_audio()

    def convert_to_audio(self):
        if self.langue == "zh-tw":
            for row in self.context:
                try:
                    self.text = gTTS(text=row, lang=self.langue)
                    self.text.save(self.mp3)

                    mixer.init()
                    mixer.music.load(self.mp3)

                    mixer.music.play()
                    while mixer.music.get_busy():
                        continue

                    os.remove(self.mp3)
                except Exception as e:
                    print(f"Error: {e}")
        else:
            try:
                self.text = gTTS(text=self.context, lang=self.langue)
                self.text.save(self.mp3)

                mixer.init()
                mixer.music.load(self.mp3)

                mixer.music.play()
                while mixer.music.get_busy():
                    continue

                os.remove(self.mp3)
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    window = Tk()
    app = Putfile(window)
    window.mainloop()
