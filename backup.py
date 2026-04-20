import urllib.request

target = "http://backup.0x10.cloud"
env_file = "http://backup.0x10.cloud/.env.backup"

response = urllib.request.urlopen(env_file)
body = response.read().decode()

if response.status == 200:
    print("Target:", target)
    print("[!] VULNERABILITY FOUND - File is publicly accessible")
    print(body)
else:
    print("[OK] File is not accessible")