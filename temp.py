import pandas as pd
import requests
df = pd.read_excel (r'./dns.xlsx')
temp= df['domains'].to_list()
list_of_url=temp[0:2]
print("\n\nall",list_of_url,"\n\n")
active=list()
#print (list_of_url)
def check(url):
	print("checking",url)
	try:
	    r = requests.head(url,timeout=1)
	    print(r.status_code)
	    if(r.status_code==200):
	    	active.append(url)
	    	print("\nadded",url,"\n")
	    else:
	    	pass
	except requests.ConnectionError:
	    print("failed to connect")
	    print("https://"+str(i))
	    return -1
	except:
		print('other error')
		return -1
	return (r.status_code)

for i in list_of_url:
	if int(check("https://"+ str(i)))==200:
		pass
	else:
		check("http://"+str(i))
print("\n\nactive",active,"\n\n")

print("\n\nall",list_of_url,"\n\n")



inactive=[]
for i in list_of_url:
	if "http://"+str(i) in active or "https://"+ str(i) in active:
		pass
	else:
		inactive.append(i)

print("\n\ninactive",inactive,"\n\n")
	