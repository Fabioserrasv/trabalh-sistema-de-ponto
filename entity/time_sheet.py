from calendar import monthrange
from datetime import time

from entity.input_output import InputOutput

class TimeSheetError(Exception):
  pass

class TimeSheet:

  def __init__(self, year: int, month: int):
    _, number_days = monthrange(year, month)

    self.year = year
    self.month = month
    self.days = [ [] for _ in range(0, number_days) ] 

  def get_day(self, day: int) -> [InputOutput]: 
    MAX_NUMBER_DAY = len(self.days) - 1

    if not (0 <= day <= MAX_NUMBER_DAY):
      raise TimeSheetError(f"Invalid day[{day}]!, Valid range from 0 to {MAX_NUMBER_DAY}!")
    
    return self.days[day]

  def __get_str_input_output_by_day(self, day:int):
    input_outputs = self.get_day(day)
    return f'{day + 1} ' + '; '.join([ 
      str(input_output) for input_output in input_outputs
    ])

  def add_hour(self, day: int, hour: time):

    time_sheet_day = self.get_day(day)

    if len(time_sheet_day) == 0:
      time_sheet_day.append(InputOutput(start=hour))
      return

    input_output = time_sheet_day[-1]
    if input_output.get_input() and not input_output.get_output():
      input_output.set_end_time(hour)
      return

    time_sheet_day.append(InputOutput(start=hour))

  def __str__(self):
    MAX_NUMBER_DAY = len(self.days)
    return f"{self.year}-{self.month}\n" + "\n".join([
      self.__get_str_input_output_by_day(day) for day in range(0, MAX_NUMBER_DAY)
    ])
    
