from entity.time_sheet import TimeSheet

class Functionary:

  def __init__(self, name: str) -> None:
    self.name = name
    self.list_time_sheet = {}
    
  def get_time_sheet(self, year: int, month: int) -> TimeSheet:
    key = f"{year}-{month}"

    if not self.list_time_sheet.get(key, None):
      self.list_time_sheet[key] = TimeSheet(year, month)

    return self.list_time_sheet[key]

  
  