import paramiko
import time
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router={"hostname":"10.1.1.10","port":"22","username":"cisco","password":"cisco"}
print("connecting 10.1.1.10")
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)

shell=ssh_client.invoke_shell()   ##bu çağırımla shelli getiriyoruz.
shell.send("terminal length 0\n")## terminallength 0 komutuyla more'u devreden çıakraıp tüm içerği alıyoruz
shell.send("show version\n")  ###shellin send metodunyla shell üzerinde bir komut çalıştırıyoruz.\n zorunludur.
shell.send("show ip int brief\n")###show ip int brief komutunu göndererek intfleri getiriyorum
time.sleep(1) #routerın bu komutu yürütmesi için bir zamana ihtiyacı bulunmakta bu yüzden time modülünü kullanıyorum.
output=shell.recv(10000) ##çıktığa ulaşmak için shell'in "recv" methodu kullanılır.Fakat bu byte değer gönderir bunu decode etmek lazım
                        ##bir kerede alınacak bayt sayısı döndürür örnek olarak 10000 verdim.
output=output.decode("utf-8") ##byte türünde bir nesneyi stringe decode ediyoruz
print(output)

if ssh_client.get_transport().is_active()==True:
    print("closing connection")
    ssh_client.close()