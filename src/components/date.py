import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es-Es')

class DateToday:
	def __init__(self) -> None:
		self.__date = datetime.date.today()
		self.__time = datetime.datetime.now()
		self.__weekday = self.__date.strftime("%A")
		self.__day = self.__date.strftime("%d")
		self.__month = self.__date.strftime("%B")
		self.__year = self.__date.strftime("%Y")

		self.__hour = self.__time.strftime("%H")
		self.__minute = self.__time.strftime("%M")

	def getDatetoday(self):
		
		self.today = {
			'weekday': self.__weekday,
			'day': self.__day,
			'month': self.__month,
			'year': self.__year
		}

		return self.today
	
	def getHour(self):

		self.time =  {
			'hour': self.__hour,
			'minute': self.__minute
		}

		return self.time

