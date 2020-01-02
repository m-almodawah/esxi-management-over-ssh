##########################################################
#
#   Author: Mohammed Almodaeah
#   Date 1/1/2020
#   version: v 1.0 pre-alpha
#
#   Description:
#   This library provides basic interaction with ESXI
#   through SSH. It allows powering on and shutting down VMs as
#   well as shutting down ESXI itself. It also allows
#   executing any command on ESXI
#
#   Tested on ESXI 6.7
#
##########################################################

import paramiko

class EsxiOverSSH:
    def __init__(self,server_ip, username, password):
        self.__server_ip = server_ip
        self.__username = username
        self.__password = password
    
    def exec(self, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.__server_ip, username=self.__username, password=self.__password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        return "".join(ssh_stdout.readlines())

    # The command below "vim-cmd vmsvc/getallvms" returns a table that contain VMs information
    # The table is parsed by splitting lines and spaces. The function
    # will not work properly if one of your VMs has a description that contains
    # multiple lines or if it has a name that contains spaces.
    def __get_all_vms(self):
        cout = self.exec("vim-cmd vmsvc/getallvms")
        cout = cout.splitlines()
        cout.pop(0)
        vms = []
        for x in cout:
            vms.append(x.split())
        return vms

    def get_vm_names(self):
        vms = self.__get_all_vms()
        vm_names = []
        for x in vms:
            vm_names.append(x[1])
        return vm_names

    def get_vm_ids(self):
        vms = self.__get_all_vms()
        vm_ids = []
        for x in vms:
            vm_ids.append(x[0])
        return vm_ids

    def get_id_by_name(self, name):
        vms = self.__get_all_vms()
        for x in vms:
            if name == x[1]:
                return x[0]
    def get_name_by_id(self, id):
        vms = self.__get_all_vms()
        for x in vms:
            if id == x[0]:
                return x[1]

    def is_vm_on(self,vm_id):
        if "on" in self.exec("vim-cmd vmsvc/power.getstate "+str(vm_id)):
            return True
        else:
            return False

    def shutdown_vm(self, vm_id):
        self.exec("vim-cmd vmsvc/power.shutdown "+str(vm_id))

    def start_vm(self,vm_id):
        self.exec("vim-cmd vmsvc/power.on "+str(vm_id))

    def shutdown_esxi(self):
        self.exec("poweroff")
