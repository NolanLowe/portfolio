import json
from flask_bootstrap import Bootstrap4
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap4(app)


def load_projects():
    with open(file='project_list.txt', mode='r') as file:
        data = json.load(file)
    return data


def add_project():
    data = load_projects()

    while True:
        if input("Add project to list? (Y/N):").lower() == 'n':
            break
        name = input("Add a new project: first, the name of the project: ")
        description = input("A short description: ")
        link = input("Now the github hyperlink: ")
        data[name] = {
            "name": name,
            "link": link,
            "description": description
        }


    with open(file='project_list.txt', mode='w') as file:
        json.dump(data, fp=file, indent=4)



@app.route("/")
def home():
    data = load_projects()
    return render_template('index.html', projects=data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

