from pandas import DataFrame
from matplotlib.pyplot import savefig

from split_dataFrame_by_position import split_dataFrame_by_position

def generate_charts (destination: str, data: DataFrame):      
    max_sum = max(data['SUMA_TOTAL'])
    dataFrames = split_dataFrame_by_position(data, 4)

    for i, dataFrame in enumerate(dataFrames):
      dataFrame.plot(kind = 'bar', x = 'GRUPO', y = 'SUMA_TOTAL', ylim = (0, max_sum), figsize = (35, 22), fontsize = 36)
      savefig(destination + str(i) + '.jpg')
