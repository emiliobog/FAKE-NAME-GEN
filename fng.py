import os
try:
 from faker import Faker
except:
	if os.name=='nt':
  		os.system('pip install Faker')
  		os.system("pip install Dumper")    	
	else:  
  		os.system('pip2 install Faker')
  		os.system("pip2 install Dumper")
faker = Faker()

print faker.name()
print faker.address()
print faker.job()
print faker.phone_number()
print faker.free_email()
print faker.date_of_birth()