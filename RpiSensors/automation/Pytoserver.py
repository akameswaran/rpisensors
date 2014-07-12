'''
Created on Jul 12, 2014

@author: ak
'''
import urllib2
from datetime import datetime
class PytoServer(object):
    '''
    classdocs
    '''
    API_BASE="/api/device/"

    def __init__(self,url,user,password):
        '''
        Constructor
        '''
        self.URL = url
        self.user = user
        self.password = password
        
        self.passwdMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        self.pytoUrl = url
        self.passwdMgr.add_password(None, self.pytoUrl, self.user, self.password)
        self.handler = urllib2.HTTPBasicAuthHandler(self.passwdMgr)
        self.opener = urllib2.build_opener(self.handler)
        
        headers = {
                   'Content-Type': 'text/plain',
        }

        self.opener.addheaders = headers.items()
        urllib2.install_opener(self.opener)
        
        
#        response = urllib2.urlopen("http://192.168.1.71:8085/api/devices")
#        print response.read()

#        req = urllib2.Request("http://192.168.1.71:8085/api/device/Motion9/","command=still")

#        response2 = urllib2.urlopen(req)

    def motion(self,deviceID):
        print "making call %s" % (datetime.now().time())
        myUrl = self.URL + PytoServer.API_BASE + deviceID
        req = urllib2.Request(myUrl,"command=motion")
        response = urllib2.urlopen(req)
        print "recieved %s" % (datetime.now().time())
    
    def still(self,deviceID):
        print "making call %s" % (datetime.now().time())
        myUrl = self.URL + PytoServer.API_BASE + deviceID
        req = urllib2.Request(myUrl,"command=still")
        response = urllib2.urlopen(req)
        print "recieved %s" % (datetime.now().time())
            