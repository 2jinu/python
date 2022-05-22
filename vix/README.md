# vix

VMware의 VIX API를 위한 객체 지향 파이썬 wrapper

vix를 사용하기 위해서 pip3 install vix로 설치한다.

# **INDEX**

**1. [VMware 상태 체크](#VMware-상태-체크)**

**2. [VMware 전원 명령](#VMware-전원-명령)**

**3. [VMware 스냅샷 명령](#VMware-스냅샷-명령)**

**4. [Guest와 Host간 상호작용](#Guest와-Host간-상호작용)**

**5. [Reference](#Reference)**

# **VMware 상태 체크**

power_state를 이용하여 vm의 상태를 확인할 수 있다.

| power_state  | return value |
| :---         | :---:        |
| POWERED_OFF  | 2            |
| POWERED_ON   | 8            |
| SUSPENDED    | 8            |
| PAUSED       | 520          |

```py
import os
import vix

base_dir    = 'E:\\1.VM\\Windows\\10\\'
vm_name     = 'Analysis_20H2-19042.508'
target      = os.path.join(os.path.join(base_dir, vm_name),vm_name) + '.vmx'
host        = vix.VixHost()

try:
    vm      = host.open_vm(target)
    print(vm.power_state)
except vix.VixError as ex:
    print("Error : {0}".format(ex))
```

다른 방법으로 is_running으로 vm의 상태를 확인할 수 있다.

반환 값은 True 혹은 False이다.

```py
import os
import vix

base_dir    = 'E:\\1.VM\\Windows\\10\\'
vm_name     = 'Analysis_20H2-19042.508'
target      = os.path.join(os.path.join(base_dir, vm_name),vm_name) + '.vmx'
host        = vix.VixHost()

try:
    vm      = host.open_vm(target)
    print(vm.is_running)
except vix.VixError as ex:
    print("Error : {0}".format(ex))
```


# **VMware 전원 명령**

vm의 전원을 키고 끄고 일시 정지 등 시킬 수 있다.

| 모드 | 예시 |
| :---: | :---: |
| 전원 종료 | vm.power_off() |
| 전원 켜기 | vm.power_on() |
| 일시 정지 | vm.suspend() |
| 재부팅 | vm.reset() |
| 멈춤 | vm.pause() |
| 재생 | vm.unpause() |


# **VMware 스냅샷 명령**

vm의 스냅샷의 생성, 제거, 복구 등 시킬 수 있다.

스냅샷을 생성해보자.

```py
vm.create_snapshot(name='test', description='hello world', include_memory=True)
```

스냅샷 정보를 확인해보자.

```py
test_snapshot = vm.snapshot_get_named('test')
print(current_snapshot.name)
print(current_snapshot.description)
print(current_snapshot.power_state)
print(current_snapshot.get_num_children())
```

스냅샷으로 돌려보자.

```py
test_snapshot = vm.snapshot_get_named('test')
vm.snapshot_revert(snapshot=test_snapshot)
```

스냅샷을 제거해보자.

```py
test_snapshot = vm.snapshot_get_named('test')
vm.snapshot_remove(snapshot=test_snapshot, remove_children=True)
```


# **Guest와 Host간 상호작용**

guest vm에 로그인 후 폴더를 생성할 수 있다.

```py
vm.login(username='admin', password='admin')
vm.create_directory(path='C:\\Users\\admin\\Desktop\\Example\\test dir')
vm.logout()
```

생성한 폴더에 host의 파일을 guest로 복사해보자.

```py
vm.login(username='admin', password='admin')
if vm.dir_exists(path='C:\\Users\\admin\\Desktop\\Example\\test dir'):
    vm.copy_host_to_guest(host_path='C:\\Users\\admin\\Downloads\\hello world.txt', guest_path='C:\\Users\\admin\\Desktop\\Example\\test dir\\hello world.txt')
vm.logout()
```

파일 명을 변경한 후 guest에서 host로 복사해보자.

```py
target_file = 'C:\\Users\\admin\\Desktop\\Example\\test dir\\hello world.txt'
new_file    = 'C:\\Users\\admin\\Desktop\\Example\\test dir\\Lorem Ipsum.txt'
vm.login(username='admin', password='admin')
if vm.file_exists(path=target_file):
    print(vm.get_file_info(target_file))
    vm.file_rename(old_name=target_file, new_name=new_file)
    vm.copy_guest_to_host(guest_path=new_file, host_path='C:\\Users\\admin\\Downloads\\Lorem Ipsum.txt')
vm.logout()
```

guest의 파일과 폴더를 삭제해보자.

```py
target_file = 'C:\\Users\\admin\\Desktop\\Example\\test dir\\Lorem Ipsum.txt'
target_dir  = 'C:\\Users\\admin\\Desktop\\Example\\test dir'
vm.login(username='admin', password='admin')
if vm.file_exists(path=target_file): vm.file_delete(path=target_file)
if vm.dir_exists(path=target_dir): vm.dir_delete(path=target_dir)
vm.logout()
```


# **Reference**

vm 복제, guest 프로세스 실행 등 기타 [다양한 사용법](https://naim94a.github.io/vix/vix.html)이 있다.