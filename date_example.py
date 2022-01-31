from datetime import datetime, timedelta

class DateExample:

  def __init__(self):
    self.__date = datetime.now()

  def add_one_hour(self):
    ONE_HOUR = timedelta(hours=1)
    self.__date = self.__date + ONE_HOUR

  def add_one_day(self):
    ONE_DAY = timedelta(days=1)
    self.__date = self.__date + ONE_DAY

  def get_date(self):
    return self.__date