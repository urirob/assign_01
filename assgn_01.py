# to find average of three numbers given by the user

a1= int(input("enter first number : \n" ))

a2= int(input("enter second number : \n" ))

a3= int(input("enter third number : \n" ))

avg = (a1+a2+a3)/3
a4 =("average of given numbers is: ", avg)

print(a4)


# problem 2 : find person's income

# note : all currency is in $

standard_deduction= 10000
number_of_dependents=int(input("enter the number of depedents : \n" ))
gross_income=float(input("enter the gross income : \n"))
total_dependent_deduction=number_of_dependents*3000
taxable_income=gross_income - standard_deduction - total_dependent_deduction
tax=taxable_income*0.2
print(tax)


# problem 3: to store different data type into a list
# for giving entry for the gender use 
# M= male , F= female, U= unknown


a1=int(input("enter SID : \n", ))
a2=input("enter name :\n", )
a3=input("enter your gender :\n",)
a4=input("enter your course name :\n",)
a5=float(input("enter the CGPA :",))

b=[a1,a2,a3,a4,a5]
print(b)

# problem 4: to get input of 5 students in a list and arrange them in a sorted manner

a1=int(input("enter marks of 1st student :\n"))
a2=int(input("enter marks of 2nd student :\n"))
a3=int(input("enter marks of 3rd student :\n"))
a4=int(input("enter marks of 4th student :\n"))
a5=int(input("enter marks of 5th student :\n"))

marks =[a1,a2,a3,a4,a5]
marks.sort()
print(marks)

# problem 5: given color=[red, green , white , black, pink, yellow]

# problem 5a: remove black from the list and print the rest of the list

color= ["red" , "green" , "white" , "black", "pink" , "yellow"]

#color.remove(color[3])
#print(color)

# problem 5b: remove black and pink and replace them with purple

color[3]='purple'
color[4]='purple'
print(color)