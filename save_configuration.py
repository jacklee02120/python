
from netmiko import ConnectHandler
import time
from datetime import datetime
import os

hpe_5950B = {
  'device_type':'hp_comware',
  'ip': '15.112.124.43',
  'username':'admin',
  'password':'admin',
}

hpe_5940B = {
  'device_type':'hp_comware',
  'ip': '15.112.124.44',
  'username':'admin',
  'password':'admin',
}

hpe_5940T = {
  'device_type':'hp_comware',
  'ip': '15.112.124.45',
  'username':'admin',
  'password':'admin',
}

hpe_5950T = {
  'device_type':'hp_comware',
  'ip': '15.112.124.46',
  'username':'admin',
  'password':'admin',
}

all_devices = [hpe_5950B, hpe_5940B,hpe_5940T,hpe_5950T]

t = time.strftime("%Y-%m-%d", time.localtime())

filepath = r'/home/ljk/switch_configuration/{0}/'.format(t)

if os.path.exists(filepath):
    message = 'OK,the  "%s" dir exists.'
else:
    message = "Now, I will create the %s"
    os.makedirs(filepath)

print (filepath)
#save = open (filename,'w')
#print ('\n show configuration')
#result = net_connect.send_command_expect('display cur')
#time.sleep(2)
#save.write(result)
#print (u'{0} file was saved!'.format(filename))
#save.close()

start_time = datetime.now()
print "start time is {0}".format(start_time)
for a_device in all_devices:
  net_connect = ConnectHandler(**a_device)
  result = net_connect.send_command_expect('display cur')


  t = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())
  filename = (u'{0}_{1}.txt'.format(a_device['ip'],t))

  save = open (filepath + filename,'w')
  print ('\n show configuration')
  time.sleep(2)
  save.write(result)
  print (u'{0} file was saved!'.format(filename))
  save.close()

end_time = datetime.now()
total_time = end_time - start_time
print total_time 