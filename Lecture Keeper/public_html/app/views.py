
from flask import render_template
from app import app
# import disciplines

class Discipline:
    def __init__(self, code, name):
        self.code = code
        self.name = name

web = Discipline('web', 'Веб-программирование')
ics = Discipline('ics', 'Проектирование АСОИУ')
electr = Discipline('electr', 'Схемотехника')

discipline_list = [web, ics, electr]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', discipline_list = discipline_list)

@app.route('/about')
def about():
	return render_template('about.html', discipline_list = discipline_list)