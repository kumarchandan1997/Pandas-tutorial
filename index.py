import pandas as pd


mydataset = {
    'cars' : ['bmw','suv','maruti','honda'],
    'passings': [3,2,5,10],
    'parking': [1,2,3,4]
}

myvar = pd.DataFrame(mydataset)

# print(myvar)

# print(myvar.loc[1])

# print(pd.__version__)
array = [1,2,3,4]

mydata = pd.Series(array)

# print(mydata)

arr = [1,2,3,4]

myvar1 = pd.Series(arr,index=["x","y","z","w"])

# print(myvar1)


df = pd.read_csv('data.csv')
print(df)

# print("csv data ",df.to_string())
