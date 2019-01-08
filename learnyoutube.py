
from netmiko import ConnectHandler
import time
from datetime import datetime
import os
import json
import getpass

username = raw_input ('enter username: ')

while 1:
    password =  getpass.getpass('enter password: ')
    password_verify = getpass.getpass('retype your password:')

    if password != password_verify:
       print ('passwords do not match, try again.')
    else:
        break

with open ('all_devices.json') as dev_file:
    all_devices = json.load(dev_file)

t = time.strftime("%Y-%m-%d", time.localtime())

filepath = r'/home/ljk/switch_configuration/{0}/'.format(t)

if os.path.exists(filepath):
    message = 'OK,the  "%s" dir exists.'
else:
    message = "Now, I will create the %s"
    os.makedirs(filepath)

print (filepath)
# save = open (filename,'w')
# print ('\n show configuration')
# result = net_connect.send_command_expect('display cur')
# time.sleep(2)
# save.write(result)
# print (u'{0} file was saved!'.format(filename))
# save.close()

start_time = datetime.now()
print "start time is {0}".format(start_time)
for a_device in all_devices:
    a_device['username'] = username
    a_device['password'] =  password
    net_connect = ConnectHandler(**a_device)
    result = net_connect.send_command_expect('display cur')

    t = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())
    filename = (u'{0}_{1}.txt'.format(a_device['ip'], t))

    save = open(filepath + filename, 'w')
    print ('\n show configuration')
    time.sleep(2)
    save.write(result)
    print (u'{0} file was saved!'.format(filename))
    save.close()

end_time = datetime.now()
total_time = end_time - start_time
print total_time
