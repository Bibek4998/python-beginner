import pandas as pd
data={
    "Name":["Bibek Joshi","Nabin Dhami","Ankit Saud"],
    "Age":[13,12,21],
    "Address":["Dadeldhura","Bajhang","Darchula"],
    "Current Address":["Kathmandu","Kathmandu","Dhangadhi"]
}
a=pd.DataFrame(data)
print("Dataframe:")
print(a)