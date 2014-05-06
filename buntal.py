import md5
#usr/bin/python
#progremmer : tukang ngael
#kerjaan : masang taot
"""
it just simple MD5 hash cracker :).
if Hash Not Found or can't cracked,You can add List of Password or Modification This Program.
You can add worlist.txt to crack it
"""
Hash = raw_input("Enter Your MD5 hash:")
ListPassword=("tengku","Tengkyu","BasriTengku","basteng","Tengku DianAyuni","tengkudianayuni",
              "Tengku Dian Ayuni")
for password in ListPassword:
    EncryptPassword = md5.md5(password).hexdigest()
    if Hash == EncryptPassword:
        print "[+] password Found :"+password
        break
    print "Hash Not Found"

