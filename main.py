# This is a sample Python script.
import csv
from random import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gamers/", methods=['GET','POST'])
def create_new_gamer():
    if request.method == 'GET':
        context = {"Имя": []}
        with open('main_base.csv', 'r') as csvfile:
            text = csv.reader(csvfile, delimiter=';')
            for row in text:
              context["Имя"].append(row[0])
        return render_template('gamers.html', context_names=context["Имя"],  num=len(context["Имя"]))
    elif request.method =='POST':
        input_name = request.form['input_name']
        with open('main_base.csv', 'a+') as f:
            f.write(f'{input_name}\n')
        return render_template('pre_game.html')

@app.route("/game/", methods=['GET','POST'])
def game():
    if request.method == 'GET':
        context = {"Имя": []}
        with open('main_base.csv', 'r') as csvfile:
            text = csv.reader(csvfile, delimiter=';')
            for row in text:
              context["Имя"].append(row[0])
            return render_template('game.html', context_names=context["Имя"],  num=len(context["Имя"]))
    elif request.method =='POST':
        context = {"Имя": [], "счет": []}
        with open('main_base.csv', 'r') as csvfile:
            text = csv.reader(csvfile, delimiter=';')
            for row in text:
              context["Имя"].append(row[0])
        for i in range(len(context["Имя"])):
          context["счет"].append(int(random()*100))
        return render_template('results.html', context_names=context["Имя"],  score=context["счет"], max=context["счет"].index(max(context["счет"])), num=len(context["Имя"]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5001)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
