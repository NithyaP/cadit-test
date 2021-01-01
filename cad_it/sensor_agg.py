from helpers import *
import pandas as pd

def get_agg_data(sensorData,sdType, aggAction):
    aggData = sensorData.groupby(['roomArea','dayDate'],as_index=False)[sdType].agg(aggAction)
    colName = aggAction+'_'+sdType
    aggData.rename(columns={sdType:colName}, inplace=True)
    return aggData

def generate_combined_agg(dataSet):
    minHumData = get_agg_data(dataSet,'humidity', 'min')
    minTemData =get_agg_data(dataSet,'temperature', 'min')
    maxHumData = get_agg_data(dataSet,'humidity', 'max')
    maxTemData =get_agg_data(dataSet,'temperature', 'min')
    medHumData = get_agg_data(dataSet,'humidity', 'median')
    medTemData =get_agg_data(dataSet,'temperature', 'median')
    avgHumData = get_agg_data(dataSet,'humidity', 'mean')
    avgTemData =get_agg_data(dataSet,'temperature', 'mean')
    # Merge datasets
    finalDf = minHumData
    for i in [minTemData,maxHumData,maxTemData,medHumData,medTemData,avgHumData,avgTemData]:
        finalDf = pd.merge(finalDf, i, on=["roomArea", "dayDate"])
    return finalDf

def main():
    sensorData = get_file_data('../data/sensor_data.json')['array']
    sensorPd = pd.DataFrame.from_dict(sensorData)
    sensorPd['dayDate'] = pd.to_datetime(sensorPd['timestamp'], unit='ms').dt.day_name() 
    resultDf = generate_combined_agg(sensorPd)
    pprint(resultDf)

if __name__ == "__main__":
    main()