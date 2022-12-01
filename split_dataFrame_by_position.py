from pandas import DataFrame

def split_dataFrame_by_position(dataFrame: DataFrame, splits: int) -> list[DataFrame]:
    """
    Takes a dataFrame and an integer of the number of splits to create.
    Returns a list of dataFrames.
    """
    dataFrames = []
    index_to_split = len(dataFrame) // splits
    start = 0
    end = index_to_split
    
    for split in range(splits):
        temporary_df = dataFrame.iloc[start:end, :]
        dataFrames.append(temporary_df)
        start += index_to_split
        end += index_to_split
    
    return dataFrames
