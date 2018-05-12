import csv

def nig():
    temp_data = []
    alt_data = []
    location = csv.reader(open("C:/Users/Talha/Google Drive/WINTER 2018/Capstone/Charts/temp/temp.csv"),delimiter=",")

    for i in location:
        one = int(i[0])
        two = int(i[1])
        temp_data.append(one)
        alt_data.append(two)
           
        

x = nig()

print(x)

