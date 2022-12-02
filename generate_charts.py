from pandas import DataFrame
from matplotlib.pyplot import savefig

from split_dataFrame_by_position import split_dataFrame_by_position
from compose_img import compose_img

def generate_charts (destination: str, template: str, data: DataFrame):      
    max_sum = max(data['SUMA_TOTAL'])
    dataFrames = split_dataFrame_by_position(data, 4)

    for i, dataFrame in enumerate(dataFrames):
      dataFrame.plot(kind = 'bar', x = 'GRUPO', y = 'SUMA_TOTAL', ylim = (0, max_sum), figsize = (27, 14), fontsize = 30)
      savefig(destination + str(i) + '.jpg')
      compose_img(destination, template, i)
