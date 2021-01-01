from helpers import *

def add_usd_rate(dataSet):
    convRate = convert_idr_usd()
    for idx,val in enumerate(dataSet):
        val['salaryInUSD'] = val['salaryInIDR']/convRate
        dataSet[idx] = val
    return dataSet

def filter_data_set(dataSet):
    reqFields = ['id','name','username','email','address', 'phone', 'salaryInIDR','salaryInUSD']
    newDataSet =[]
    for val in dataSet:
        d = {}
        for j in val:
            if j in reqFields:
                d[j] = val[j]
        newDataSet.append(d)
    return newDataSet

def convert_idr_usd():
    url ="https://free.currconv.com/api/v7/convert?q=USD_IDR&compact=ultra&apiKey=deef0097d334f3a096ad"
    usd2idr = get_url_data(url)
    return usd2idr['USD_IDR']

def join_data(urlDataSet,fileDataSet):
    outputData = []
    for key in urlDataSet:
        id1 = key['id']
        for i in fileDataSet['array']:
            if id1 ==  i['id']:
                key.update(i)
        outputData.append(key)
    return outputData

def main():
    ''' '''
    url = "http://jsonplaceholder.typicode.com/users"  
    urlDataSet = get_url_data(url)
    
    salaryFile ="../data/salary_data.json"
    fileDataSet = get_file_data(salaryFile)
    
    joinDataSet=join_data(urlDataSet,fileDataSet)
    usdDataSet = add_usd_rate(joinDataSet)
    
    finalDataSet = filter_data_set(usdDataSet)
    pprint(finalDataSet)
    
if __name__ == "__main__":
    main()