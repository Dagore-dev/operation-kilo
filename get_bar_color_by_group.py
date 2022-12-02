from pandas import DataFrame

def get_bar_color_by_group (dataFrame: DataFrame) -> list[str]:
    colors = []
    colors_dict =  {
        'ESO1': 'lime',
        'ESO2': 'limegreen',
        'ESO3': 'green',
        'ESO4': 'darkgreen',
        'DAW1': 'silver',
        'DAW2': 'gray',
        'GAD1': 'purple',
        'GAD2': 'fuchsia',
        'ITL1': 'blue',
        'ITL2': 'navy',
        'IEA1': 'teal',
        'IEA2': 'aqua',
        'CIBER': 'blueviolet',
        'IOT': 'darkgoldenrod',
        'BTO1CT': 'gold',
        'BTO1HS': 'goldenrod',
        'BTO2': 'greenyellow',
        'FPB1': 'hotpink',
        'FPB2': 'indianred',
        'ASIR1': 'red',
        'ASIR2': 'maroon'
    }

    for group in dataFrame['GRUPO']:
        if group.startswith('ESO'):
            key = group[:len(group) - 1]
            colors.append(colors_dict[key])
        else:
            colors.append(colors_dict[group])
        
    return colors
