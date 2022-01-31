from datetime import time

class InputOutputError(Exception):
  pass 

class InputOutput:

  def __init__(self, start: time = None, end: time = None) -> None:
    if (start and end) and start > end:
      raise InputOutputError('Start time greater than End time!')

    self.__start = start
    self.__end = end

  def set_start_time(self, start: time) -> None:
    if self.__end and start > self.__end:
      raise InputOutputError('Start time greater than End time!')

    self.__start = start

  def set_end_time(self, end: time) -> None:
    if self.__start and self.__start > end:
      raise InputOutputError('End time less than start time!')

    self.__end = end

  def __str__(self):
    start = self.__start if self.__start else ''
    end = self.__end if self.__end else ''
    return f"Entrada: {start}, Saída: {end}"

  def get_input(self):
    return self.__start

  def get_output(self):
    return self.__end