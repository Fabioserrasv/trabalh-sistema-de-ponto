from entity.functionary import Functionary
from entity.input_output import InputOutput

from date_example import DateExample


name_functionary = input("Digite o nome do funcionario: ")
functionary = Functionary(name_functionary)

date_example = DateExample()

def bater_ponto():
  day_example = date_example.get_date()
  year = day_example.year
  month = day_example.month
  day = day_example.day - 1
  hour = day_example.time()

  time_sheet_day = functionary.get_time_sheet(year, month).get_day(day)
  
  if len(time_sheet_day) == 0:
    time_sheet_day.append(InputOutput(start=hour))
    return

  input_output = time_sheet_day[-1]
  if input_output.get_input() and not input_output.get_output():
    input_output.set_end_time(hour)
    return

  time_sheet_day.append(InputOutput(start=hour))
  

def passar_hora():
  date_example.add_one_hour()

def passar_dia():
  date_example.add_one_day()

def mostra_horarios():
  day_example = date_example.get_date()
  year = day_example.year
  month = day_example.month

  print(functionary.get_time_sheet(year, month))

options = [
  {
    "message": "Bater Ponto",
    "action": bater_ponto
  },
  {
    "message": "passar uma hora",
    "action": passar_hora
  },
  {
    "message": "passar um dia",
    "action": passar_dia
  },
  {
    "message": "Mosta horarios",
    "action": mostra_horarios
  }
]


def show_options():
  print("====================")
  for index in range(0, len(options)):
    message = options[index]['message']
    print(f"{index} - {message}")

  print("====================")



while True:
  show_options()
  option = int(input('Digite a opção: '))

  action = options[option]['action']
  action()