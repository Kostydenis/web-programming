class Discipline
	def __init__(self, code, name):
		self.code = code;
		self.name = name;

discipline_list = [
	web = Discipline('web', 'Веб-программирование'),
	ics = Discipline('ics', 'Проектирование АСОИУ'),
	electr = Discipline('electr', 'Схемотехника'),
]