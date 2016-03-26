import glob
import csv
import random
from faker import Factory
from datetime import datetime
from randomdate import *

fake = Factory.create()

list_size = [10000,50000,100000,300000,1000000,10000000]


for size in list_size:
	file_path = "C:\Users/valued/Desktop/garytest" + str(size)+".csv"
	f=open(file_path,"w+")
	k=csv.reader(f)

	g=open(file_path,"a")
	w=csv.writer(g, lineterminator = '\n')
	w.writerow(('id','registration_type',	'shift_id',	'created_by_user_id',	'form_number',
	'first_name','middle_name'	,'last_name'	'name_suffix','voting_street_address_one',	
	'voting_street_address_two','voting_city','voting_state','voting_zipcode',
	'mailing_street_address_one','mailing_street_address_two','mailing_city','mailing_zipcode','county',	
	'precinct','gender','date_of_birth','registration_date','identification','phone_number','email_address'	
	,'us_citizen','eligible_voting_age','signature','extras','created_at','updated_at','contacted_voter',
	'score','batch_id','attempted','party','name_prefix'))

	for i in range(size):

		w.writerow(
		(i+1,
		'',
		i+1,
		random.randrange(size),
		str(random.choice(['CO',"NV"])+str(random.randrange(1000,9999))),
	str(fake.first_name()),
	random.choice(['',str(fake.first_name())]),
	str(fake.last_name()),
	random.choice(["","DR","ESQ"]),
	str(fake.address().split('\n')[0]),	
	'',
	str(fake.city()),
	str(fake.state()),
	str(fake.zipcode()),
	'',
	'',
	str(fake.city()),
	'',
	'',	
	'',
	random.choice(["M","F",'']),
	get_random_date(),
	get_random_date(),
	'',
	random.randrange(1000000000,99999999999),
	'',
	'1',
	get_random_date(),
	'1',
	'',
	get_random_date()
	,get_random_date()
	,'0',
	random.randrange(0,100),
	random.randrange(1,10000),
	'0',
	random.choice(['DEM','Republican','Independent','The Pizza Party']),
	random.choice(['MR','MRS','DR']))
	)
	
		
		
		
		
		
		
	f.close()