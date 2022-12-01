from sys import argv
from os.path import exists, isdir

from read import read
from generate_charts import generate_charts

def main ():
  if len(argv) != 3:
    print('Please, provide a path to a csv file and a directory for the result')
    exit(1)

  filename = argv[1]
  destination = argv[2]

  if not exists(filename):
    print('csv file not found')
    exit(1)

  if not exists(destination) or not isdir(destination):
    print('Conflict with destination path')
    exit(1)

  data = read(filename)
  sorted_data = data.sort_values(by = ['SUMA TOTAL'], ascending = False)
  generate_charts(destination, sorted_data)
  

if __name__ == '__main__':
  main()
