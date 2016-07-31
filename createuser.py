#!/usr/bin/python

import requests
import getpass

k = open("usernames.txt")
a = k.read()
passwd = getpass.getpass("Enter the admin password: ")
phpreporturl = raw_input("Eneter your phpreport URL: ")
usernames = a.split('\n')
usernames = usernames[:-1]
s = requests.session()

loginUrl = "%s/web/services/loginService.php"% phpreporturl
createUserUrl = "%s/web/services/createUsersService.php" % phpreporturl
s.post(loginUrl, auth=('admin', passwd))
for item in usernames:
    a = s.post(createUserUrl,
       data = "<?xml version=\"1.0\" encoding=\"ISO-8859-15\"?><users><user><login>%s</login><password>%s</password><userGroups><admin>false</admin><staff>true</staff></userGroups></user></users>" % (item, item))
    print a.text

