# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Code starts here
census = np.concatenate((data,new_record))
print(census)


# --------------
#Code starts her
import numpy as np 
age=np.array(census[:,0])
print(age)
max_age =age.max()
min_age = age.min()
age_mean = age.mean()
age_std=np.std(age)

print(max_age)
print(min_age)
print(age_mean)
print(age_std)



# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))
print(min(race_list))
print(minority_race)
#Code ends here






# --------------
#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]


print(high)
print(low)


avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]


if(avg_pay_high>avg_pay_low):
    {
        print("getting paid well")
    }
else:
    {
            print("not getting paid well")
    }

print(avg_pay_high)
print(avg_pay_low)


