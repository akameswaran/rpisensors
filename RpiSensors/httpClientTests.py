import urllib2
import httplib



passwdMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://192.168.1.71:8085/"
passwdMgr.add_password(None, top_level_url, "admin", "funk")

handler = urllib2.HTTPBasicAuthHandler(passwdMgr)

opener = urllib2.build_opener(handler)



headers = {
  'Content-Type': 'text/plain',
}

opener.addheaders = headers.items()
urllib2.install_opener(opener)
response = urllib2.urlopen("http://192.168.1.71:8085/api/devices")
print response.read()

req = urllib2.Request("http://192.168.1.71:8085/api/device/Motion9/","command=still")

response2 = urllib2.urlopen(req)

    

print response2.read()