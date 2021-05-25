#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Spencer Good 4/27/2021

#Write a program that will calculate the cost of a custom cup of coffee at a gourmet coffee shop, based on the size of 
#the cup, the type of coffee selected, and flavors that can be added to the coffee. 

#how much the sizes will cost
small = 2;
medium = 3;
large = 4;

#how much the brewing/espresso cost
brewed = 0;
espresso = .50;
coldBrew = 1;

#how much the flavoring cost
noOption = 0;
options = .50;

#user inputs what they would like
userSize = input("What size would you like? ");
userType = input("What type would you like? ");
userFlavor = input("Would you like flavoring? ");

#if answer is yes the user is promted for what syrup and if not then its no flavoring
if userFlavor == "yes":
    userFlavor = input("Do you want hazelnut syrup, vanilla syrup, or caramel syrup? ")
else:
    userFlavor = ("no flavoring");
    
#printed what the user asked for    
print("You asked for a "+userSize +" " +userType +" coffee with "+userFlavor);

#turns the variables into integers
small = int(small);
medium = int(medium);
large = int(large);
brewed = int(brewed);
espresso = int(float(espresso));
coldBrew = int(coldBrew);
noOption = int(noOption);
options = int(float(options));

#elif statments dealing with user input about the size to get how much the size is
if userSize == "small":
    userSize = small
elif userSize == "medium":
    userSize = medium
elif userSize == "large":
    userSize = large
else:
    print("Invaild size");

#elif statments dealing with user input about the type to get how much the type is    
if userType == "brewed":
    userType = brewed
elif userType == "espresso":
    userType = espresso
elif usertype == "cold brew":
    userType = coldBrew
else:
    print("Invaild brew or espresso")

#elif statments dealing with user input about the options to get how much the option is
if userFlavor == "hazelnut syrup":
    userFlavor = options
elif userFlavor == "vanilla syrup":
    userFlavor = options
elif userFlavor == "caramel syrup":
    userFlavor = options
else: 
    userFlavor = noOption

#turns the user inputs into integers
userSize = int(float(userSize));
userType = int(float(userType));
userFlavor = int(float(userFlavor));

#equations to find the total of the purchase
withoutTax = (userSize + userType + userFlavor);
total = ((withoutTax * 15)/100) + withoutTax;

#turns the total into a string
total = str(total)

#prints what the total is
print("Your total is: "+total);


# In[ ]:




