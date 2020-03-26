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
print '''
proyect of BOG
                                       
 _|_|_|_|      _|_|_|          _|_|_|  
 _|            _|    _|      _|        
 _|_|_|        _|    _|      _|  _|_|  
 _|            _|    _|      _|    _|  
 _|            _|_|_|          _|_|_|  v 0.1
                                       
01000110  01000100  01000111 
'''
print faker.name()
print faker.address()
print faker.job()
print faker.phone_number()
print faker.free_email()
print faker.date_of_birth()
