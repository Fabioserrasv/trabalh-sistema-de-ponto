from entity.functionary import Functionary
from entity.input_output import InputOutput
from datetime import time

test1 = Functionary('Leandro')

FRIST_DAY = test1.get_time_sheet(2022, 1).get_day(0)
SECOND_DAY = test1.get_time_sheet(2022, 1).get_day(1)


FRIST_DAY.append(InputOutput(start=time(8, 30), end=time(12, 20)))
FRIST_DAY.append(InputOutput(start=time(14, 30), end=time(18, 0)))

SECOND_DAY.append(InputOutput(start=time(8, 30)))

print(str(test1.get_time_sheet(2022, 1)))