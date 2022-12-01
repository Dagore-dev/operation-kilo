from pandas import DataFrame, read_csv

def read (filename: str) -> DataFrame:
  try:
    data = read_csv(filename)
    data.drop(data.columns[2:], axis = 1, inplace = True) # Removes unnecessary data
    
    return data
  except:
    print('Error while trying to read the file')
    exit(1)
    