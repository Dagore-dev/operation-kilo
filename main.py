from sys import argv
from pandas import read_csv

from generate_charts import generate_charts

def main ():
  if len(argv) != 2:
    print('Please, provide a path to a csv file')
    exit(1)
  
  try:
    filename = argv[1]

    data = read_csv(filename)
    data.drop(data.columns[2:], axis = 1, inplace = True) # Removes unnecessary data

    sorted_data = data.sort_values(by = ['SUMA TOTAL'], ascending = False)

    generate_charts(sorted_data)

  except:
    print('Error while trying to read the file')
    exit(1)
  

if __name__ == '__main__':
  main()
