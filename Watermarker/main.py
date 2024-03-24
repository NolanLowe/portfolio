import os
import random
from os import listdir
from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError

window = Tk()
window.title('WATERMARKER')
wrap = 250

files = []
dest_folder = ""


def parse_directory() -> None:
    """
    response of pick directory button. prompts system finder -> pick your folder.
    :return: None
    """
    global files, dest_folder

    folder_selected = filedialog.askdirectory()
    dest_folder = folder_selected + "/WATERMARKED"

    files = listdir(folder_selected)

    for f in files:
        if "." not in f.split("/")[-1]:
            files.remove(f)

    for i in range(len(files)):
        files[i] = folder_selected + "/" + files[i]


def batch() -> None:
    """
    response of "Execute" button. asks for confirmation, then starts marking process for all images in directory.
    images identified by containing '.' in their filename.
    :return: None
    """
    global files, dest_folder

    # prompt for confirmation
    if messagebox.askquestion('Apply Watermark', f'Apply watermarks to {len(files)} images?') == 'no':
        return

    # make sure the /WATERMARKED directory exists -> will fill with images
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for f in files:
        try:
            with Image.open(f).convert("RGBA") as im:
                font_size = 40
                square_side = font_size * len(text_field.get())
                transparency = 60

                # make a blank image for the text, initialized to transparent text color
                txt = Image.new("RGBA", im.size, (255, 255, 255, 0))

                fnt = ImageFont.truetype(font='arial', size=font_size, index=0, encoding='', layout_engine=None)

                # get a drawing context
                d = ImageDraw.Draw(txt)

                # user wants aggressive watermarking
                if aggr.get() == 1:
                    random_offset_x = random.randint(-round(square_side / 2), -round(square_side / 4))
                    random_offset_y = -round(font_size / 2) + random.randint(-round(font_size / 8),
                                                                             round(font_size / 8))
                    flipflop = 0
                    for y in range(random_offset_y, im.height + square_side + abs(random_offset_y), square_side):
                        for x in range(random_offset_x, im.width + square_side + abs(random_offset_x), square_side):
                            if flipflop % 2 == 0:
                                x += square_side / 2
                            d.text((x, y), text_field.get(), font=fnt, fill=(255, 255, 255, transparency))

                        flipflop += 1
                else:
                    # draw text, half opacity
                    x_loc = im.width - square_side
                    y_loc = im.height - font_size - 10
                    d.text((x_loc, y_loc), text_field.get(), font=fnt, fill=(255, 255, 255, transparency))

                out = Image.alpha_composite(im, txt)
                out = out.convert('RGB')

                filename = dest_folder + "/" + f.split('/')[-1]
                print(f"MARKED: {f.split('/')[-1]}")
                out.save(fp=filename)

        except UnidentifiedImageError:
            print(f"ERROR: bad format on image: {f}")


add_dir_label = Label(text="Button will prompt you to choose a directory. Pick the one containing images, etc.",
                      wraplength=wrap)
add_directory = Button(text='Path', command=parse_directory)

text_label = Label(text="Text field is for your desired watermark: eg, artist moniker, name, etc.", wraplength=wrap)
text_field = Entry()

aggr = IntVar()
aggr_label = Label(text='If "aggressive" is ticked, watermarking will tile over entire image, '
                        'otherwise only 1 watermark in bottom right.', wraplength=wrap)
aggr_bx = Checkbutton(window,
                      text="aggressive",
                      variable=aggr,
                      onvalue=1,
                      offvalue=0)


add_watermarks = Button(text='execute', command=batch)

elements = {
    'pick_directory': {
        'item': add_directory,
        'label': add_dir_label
    },
    'customize_watermark': {
        'item': text_field,
        'label': text_label
    },
    'aggressive?': {
        'item': aggr_bx,
        'label': aggr_label
    }
}

row = 1
for (key, value) in elements.items():
    value['label'].grid(row=row, column=0, padx=2, pady=2)
    value['item'].grid(row=row, column=1, padx=2, pady=2)
    row += 1

add_watermarks.grid(row=6, column=0, columnspan=2, pady=15)
info_label = Label(text="All watermarked images will be placed in new directory: dir you supplied + /WATERMARKED",
                   wraplength=wrap)
info_label.grid(row=7, column=0, columnspan=2, pady=5)
window.mainloop()
