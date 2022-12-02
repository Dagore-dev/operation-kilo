from pandas import DataFrame
from matplotlib.pyplot import savefig

from split_dataFrame_by_position import split_dataFrame_by_position
from get_bar_color_by_group import get_bar_color_by_group
from compose_img import compose_img


def generate_charts (destination: str, template: str, data: DataFrame):      
    max_sum = max(data['SUMA_TOTAL']) + 10
    dataFrames = split_dataFrame_by_position(data, 4)

    for i, dataFrame in enumerate(dataFrames):
      colors = get_bar_color_by_group(dataFrame)
      plot = dataFrame.plot(kind = 'bar', x = 'GRUPO', y = 'SUMA_TOTAL', ylim = (0, max_sum), figsize = (27,14), fontsize = 30, legend = False, color = colors)

      plot.bar_label(plot.containers[0], label_type = 'edge', fontsize = 35)
      

      plot.set_ylabel("Kilos", fontdict = {"fontsize": 50})
      plot.set_xlabel("Curso", fontdict = {"fontsize": 1})
      

      savefig(destination + str(i) + '.jpg')
      compose_img(destination, template, i)
