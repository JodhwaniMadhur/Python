line='nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh=line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


#for ignoring or dumping something not in use but needed to be removed from the important part of listwe can use 
# *_ which will create a list of unwanted part like in above case of fields or we can name it ign which means ignore

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(_)

print(year)

#here the list created that is pointed by underscore variable is not important so we have named it with _ however it can be referenced
# by the name _
#s if you print the output here it will represent the inner list that is 12 and 18 since it is not important we can refer n number of lists
# by that name but it will store the last stored list and remove the previous stored value on re assigning