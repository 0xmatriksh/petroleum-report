from .models import Data
from django.db.models import Max,Min

first_five = Data.objects.all().filter(year__range=['2000','2004'])
second_five = Data.objects.filter(year__range=['2005','2009'])
third_five = Data.objects.filter(year__range=['2010','2014'])

petrol_data = Data.objects.filter(petroleum_product='Petrol') #range year__range(['2014'],['2010'])
diesel_data = Data.objects.filter(petroleum_product='Diesel')
kerosene_data = Data.objects.filter(petroleum_product='Kerosene')
turbine_data= Data.objects.filter(petroleum_product='Aviation Turbine Fuel')
lightdiesel_data = Data.objects.filter(petroleum_product='Light Diesel Oil')
furnace_data =Data.objects.filter(petroleum_product='Furnace Oil')
lpg_data =Data.objects.filter(petroleum_product='LPG in MT')
mineral_data =Data.objects.filter(petroleum_product='Mineral Turpentine Oil')

total_data = [petrol_data,diesel_data,kerosene_data,turbine_data,lightdiesel_data,furnace_data,lpg_data,mineral_data]
total_year = [third_five,second_five,first_five]

#to store the refined data
rdata = []

for x in total_data:
    name = str(x[0])
    for y in total_year:
        salesdata = list(y.filter(petroleum_product=name).values('sale')) #it contains list of dict of 'sale' as key and values
        
        #we have to store the data of the sale only 
        #so to store the values of calculating data
        calcdata = []
        for e in salesdata: #now e consists particular dict 
            for value in e.values():
                calcdata.append(value) #appending the every value which is used later to calculte min and avg.

        #we have to calculate the min and avg for the non zero value only
        #so to store the non zero data only we create:
        nonzero = []
        for n in calcdata:
            if n!=0:
                nonzero.append(n)
            
        
        #to calculate the min and average for the data
        if len(nonzero) == 0:
            min = 0
            avg = 0
        else :
            min = nonzero[0]
            sum = 0
            for num in nonzero:
                sum = sum + num
                if num<min:
                    min = num
            avg = sum/len(nonzero) 

        #to calculate the maximum value of sale
        maximum = y.filter(petroleum_product=name).aggregate(Max('sale'))
        for value in maximum.values():
            max = value

        #to show the range of year for particular petroleum product
        startyear = y.aggregate(Min('year'))
        for value in startyear.values():
            mystartyear = str(value)
        
        lastyear = y.aggregate(Max('year'))
        for value in lastyear.values():
            mylastyear = str(value)

        myyearrange = mystartyear + " - " + mylastyear #range

        data = [name,myyearrange,min,max,avg]
        rdata.append(data)
