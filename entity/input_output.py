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
    if self.end and start > self.end:
      raise InputOutputError('Start time greater than End time!')

    self.start = start

  def set_end_time(self, end: time) -> None:
    if self.start and self.start > end:
      raise InputOutputError('End time less than start time!')

    self.end = end

  def __str__(self):
    start = self.__start if self.__start else ''
    end = self.__end if self.__end else ''
    return f"Entrada: {start}, Saída: {end}"