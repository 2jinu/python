import os
import vix

base_dir    = 'E:\\1.VM\\Windows\\10\\'
vm_name     = 'Analysis_20H2-19042.508'
target      = os.path.join(os.path.join(base_dir, vm_name),vm_name) + '.vmx'
host        = vix.VixHost()

vm          = host.open_vm(target)
target_file = 'C:\\Users\\admin\\Desktop\\Example\\test dir\\Lorem Ipsum.txt'
target_dir  = 'C:\\Users\\admin\\Desktop\\Example\\test dir'
vm.login(username='admin', password='admin')
if vm.file_exists(path=target_file): vm.file_delete(path=target_file)
if vm.dir_exists(path=target_dir): vm.dir_delete(path=target_dir)
vm.logout()