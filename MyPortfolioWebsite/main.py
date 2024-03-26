import json
# from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, url_for
import pathlib
import os
from parser import Parser

app = Flask(__name__)
# bootstrap = Bootstrap4(app)


def load_projects() -> Parser:
    git_lnk = 'https://github.com/NolanLowe/portfolio/tree/e91af27b29f4e6ea615172e1d3a69660dc6a3b68/'
    root = pathlib.Path(os.getcwd())

    readme_files = []
    for d in root.parents[0].iterdir():
        if '.' in str(d).split('/')[-1]:
            pass
        else:
            readme_files.append(str(d))

    par = Parser(git_lnk)
    for r in readme_files:
        filename = "readme.txt"
        with open(file=f"{r}\\{filename}", mode='r') as file:
            data = file.readlines()
            image_url = url_for('static', filename=f"assets/{r.split('\\')[-1]}_ss.png")
            par.append(title=data[0],
                       language=data[1],
                       desc=data[2:],
                       image=image_url)
    return par

@app.route("/")
def home():
    par = load_projects()

    return render_template('index.html', projects=par.data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()



