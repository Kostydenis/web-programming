
from flask import render_template
from flask import send_file
from app import app
# import disciplines

class Discipline:
    def __init__(self, code, name, pdf):
        self.code = code
        self.name = name
        self.pdf = pdf

web = Discipline('web', 'Веб-программирование', 'webPDF')
ics = Discipline('ics', 'Проектирование АСОИУ', 'icsPDF')
electr = Discipline('electr', 'Схемотехника', 'electrPDF')

discipline_list = [web, ics, electr]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', discipline_list = discipline_list)

@app.route('/about')
def about():
	return render_template('about.html', discipline_list = discipline_list)

@app.route('/web')
def web():
	return render_template('/web/index.html', discipline_list = discipline_list)

@app.route('/webPDF')
def webPDF():
	return send_file('static/pdfs/web.pdf', as_attachment=True)

@app.route('/ics')
def ics():
	return render_template('/ics/index.html', discipline_list = discipline_list)

@app.route('/icsPDF')
def icsPDF():
	return send_file('static/pdfs/ics.pdf', as_attachment=True)

@app.route('/electr')
def electr():
	return render_template('electr/index.html', discipline_list = discipline_list)

@app.route('/electrPDF')
def electrPDF():
	return send_file('static/pdfs/electr.pdf', as_attachment=True)
