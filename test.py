# This code will power-on a VM if it is off and shut it down if it is on
from esxi_management_over_ssh import EsxiOverSSH

mn = EsxiOverSSH("Your ESXI's IP address here","your username here","your password here")
vid =mn.get_id_by_name("Your vm name here (will not work if you vm name contains spaces. See README). You can get it from mn.get_vm_names()")

print ("vm id: " +vid)
print ("powered on?: "+str(mn.is_vm_on(vid)))

if mn.is_vm_on(vid):
    print("shutting down..")
    mn.shutdown_vm(vid)
else:
    print("powering on..")
    mn.start_vm(vid)
