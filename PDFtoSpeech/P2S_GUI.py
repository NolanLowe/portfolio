from tkinter import *
from tkinter import filedialog, messagebox
from PDFtoSpeech import PDFtoSpeech


class P2S_GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('P2S - PDF to Speech')
        self.wrap = 250
        self.p2s = PDFtoSpeech()

        # self.p2s.load(filename='test_multipage.pdf')
        # self.p2s.to_speech()

        def pick_PDF() -> None:
            file = filedialog.askopenfilename()
            if file == "":
                return
            self.p2s.load(file)

        def create_speech_version() -> None:
            """
            response of "Execute" button. asks for confirmation, then starts marking process for all images in directory.
            images identified by containing '.' in their filename.
            :return: None
            """
            if self.p2s.filename is None:
                messagebox.showerror(title=f'Problem with file', message="you must pick a PDF first.")
                return

            if messagebox.askquestion('Create audio version?', f'Convert PDF {self.p2s.filename}.pdf to speech?') == 'yes':
                message, error = self.p2s.to_speech(slow=speech_speed.get())
                if error:
                    messagebox.showerror(title=f'Problem with file', message=message + f"\n{error}")

        add_dir_label = Label(text="Button will prompt you to choose your PDF.",
                              wraplength=self.wrap)
        add_directory = Button(text='Path', command=pick_PDF)

        speech_speed = IntVar()
        aggr_label = Label(text='If "slow" is ticked, speech output will be slow, fast otherwise.',
                           wraplength=self.wrap)
        aggr_bx = Checkbutton(self,
                              text="slow?",
                              variable=speech_speed,
                              onvalue=1,
                              offvalue=0)

        convert_to_speech = Button(text='Create Speech Version', command=create_speech_version)

        elements = {
            'pick_directory': {
                'item': add_directory,
                'label': add_dir_label
            },
            'options': {
                'item': aggr_bx,
                'label': aggr_label
            }
        }

        row = 1
        for (key, value) in elements.items():
            value['label'].grid(row=row, column=0, padx=20, pady=6)
            value['item'].grid(row=row, column=1, padx=20, pady=6)
            row += 1

        convert_to_speech.grid(row=row, columnspan=2, padx=2, pady=20)

        info_label = Label(
            text=".mp3 audio will be created alongside your input file.",
            wraplength=self.wrap)
        info_label.grid(row=7, column=0, columnspan=2, pady=5)

        self.mainloop()
