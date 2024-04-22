from pypdf import PdfReader
from gtts import gTTS
import os
class PDFtoSpeech:
    def __init__(self):
        self.text = ""
        self.filename = None
        pass

    def load(self, filename: str) -> None:
        self.filename = filename.split('.')[0]

        # creating a pdf reader object
        reader = PdfReader(filename)

        # printing number of pages in pdf file
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            self.text += page.extract_text()

    def to_speech(self):
        audioPDF = gTTS(text=self.text, lang='en', slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        audioPDF.save(f"{self.filename}.mp3")

        # Playing the converted file
        os.system(f"{self.filename}.mp3")