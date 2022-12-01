from pandas import DataFrame
from matplotlib import pyplot

def generate_charts (destination: str, data: DataFrame):  
    # This is just an example
    print(data)
    pyplot.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
    pyplot.savefig(destination + '1.jpg')
