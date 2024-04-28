from tkinter import Tk, filedialog, Button, Label
import PIL.Image
import pandas as pd
from PIL import ImageTk
from inputcomponent import InputComponent
from palette import Palette


class ColorExtractor(Tk):
    def __init__(self):
        super().__init__()
        self.title('ColorExtractor')
        self.configure(width=500, height=500)

        self.image = None
        self.logged_colors = []
        self.swatches = []

        self.image_path = None
        self.color_strictness = None

        self.palette = Palette(master=self)

        self.num_colors = InputComponent(master=self, text="Number of unique colors", default_value="10")
        self.num_colors.grid(row=0, column=0)

        self.max_diff = InputComponent(master=self, text="Color strictness",
                                       default_value="10")
        self.max_diff.grid(row=1, column=0)

        self.choose_image = Button(master=self, text="choose image", command=self.get_image_path)
        self.choose_image.grid(row=1, column=1)

        self.execute = Button(master=self, text="go", command=self.go)
        self.execute.grid(row=2, column=0, columnspan=2, pady=20)

        self.mainloop()

    def get_image_path(self):
        self.image_path = filedialog.askopenfilename()
        img = PIL.Image.open(self.image_path)
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img, pady=5, padx=5)
        panel.image = img
        panel.grid(row=0, column=1)

    def go(self):
        self.reset_palette()

        self.color_strictness = int(self.max_diff.get())

        with PIL.Image.open(self.image_path) as im:
            rgb_image = im.convert('RGB')
            num_colors = rgb_image.size[0] * rgb_image.size[1]

            colors = rgb_image.getcolors(maxcolors=num_colors)

            cols = ['count', 'color']
            df = pd.DataFrame(columns=cols, data=colors)
            df.sort_values('count', ascending=False, inplace=True)

            picked_colors = 0
            max_colors = self.num_colors.get()
            for index, row in df.iterrows():
                if picked_colors >= max_colors:
                    self.palette.construct()
                    return
                elif self.is_unique(row['color']):
                    self.logged_colors.append(row['color'])
                    self.palette.add_swatch(rgb=row['color'], prevalence=round(row['count'] / num_colors * 100, 5))
                    picked_colors += 1

            self.palette.construct()


    def reset_palette(self):
        self.palette.grid_forget()
        self.palette.destroy()
        self.palette = Palette(self)
        self.palette.grid(row=0, column=2, rowspan=3)
        self.logged_colors.clear()


    def is_unique(self, rgb):
        for color in self.logged_colors:
            if (abs(color[0] - rgb[0]) <= self.color_strictness
                    and abs(color[1] - rgb[1]) <= self.color_strictness
                    and abs(color[2] - rgb[2]) <= self.color_strictness):
                return False

        return True
