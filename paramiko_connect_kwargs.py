import paramiko

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router={"hostname":"10.1.1.10","port":"22","username":"cisco","password":"cisco"}
print("connecting 10.1.1.10")
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)

print(ssh_client.get_transport().is_active())


print("closing connection")
ssh_client.close()

##Yukarıdaki örnekte ise paramiko kullanarak bağlanmanın başka bir yolu.**kwargs mantığı ile dictionary veri yapısı kullanarak.
