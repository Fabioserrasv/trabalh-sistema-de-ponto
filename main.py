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

  time_sheet = functionary.get_time_sheet(year, month)
  time_sheet.add_hour(day, hour)
  
  
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
    "message": "Passar uma hora",
    "action": date_example.add_one_hour
  },
  {
    "message": "Passar um dia",
    "action": date_example.add_one_day
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
  number_option = int(input('Digite a opção: '))

  option = options[number_option]
  message = option['message']
  action = option['action']

  print("====================")
  print(message)
  action()