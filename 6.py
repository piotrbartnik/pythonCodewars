# count people in buss

def number(bus_stops):
  i = 0
  people = 0
  while i < len(bus_stops):
    people += bus_stops[i][0]
    people -= bus_stops[i][1]
    i += 1
  return people

  
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])