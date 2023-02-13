'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

EMPLOYEE = 'employee_data.csv'
#open the file

infile = open(EMPLOYEE,'r')
reader = csv.reader(infile)
next(reader)


#create an empty dictionary
employee = {'data' : []}


#use a loop to iterate through the csv file
for i in reader:
    department = i[3]
    title = i[4]
    #check if the employee fits the search criteria
    if  department == 'Marketing' and title == 'CSR':
        temp_dict = {}
        temp_dict['fname'] = i[1]
        temp_dict['lname'] = i[2]
        temp_dict['current'] = float(i[5])
        new_sal = float(i[5]) * 1.10
        
        employee['data'].append(temp_dict)


print(employee)
           

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for i in range(0, len(employee)):
   print('Manager Name: ', employee['data'][i]['fname'],employee['data'][i]['lname'], )



          
        

        
    
