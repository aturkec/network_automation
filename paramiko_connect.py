##pythonda cihazlara ssh ile bağlanabilmemiz için kullanılan kütüphane.Bunun için paramiko modülünü yükledim önceden
## router üzerinde sshı aktiflemem lazım.

import paramiko
print("connecting 10.1.1.0")
ssh_client=paramiko.SSHClient() ###ssh türünde bir paramiko nesnesi yarattım.Bunun bir ssh istemci uyg. olduğunu düşünebilirsiniz putty vs gibi
print(type(ssh_client))## bunu yazdırırsam bunun bir paramiko objesi olduğunu görürüm.


ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())##bu fonksiyonu eklemek gerekiyor bu fonksiyonun anlamı host keyi kabul ettiğini belirtir
ssh_client.connect(hostname="10.1.1.10",port="22",username="cisco",password="cisco",look_for_keys=False,allow_agent=False)
##yukarıda ki tanımımda look for keysi false yapıyorum çünkü public key authhnatication kullanmıyorum ya da bir ssh agent bu yüzden false
#olarak atama yaptım.normal username ve password kullanarak bağlanıyorum.bu iki false olan argüman birbiriyle ilişkilidir.
print(ssh_client.get_transport().is_active())##bu fonksiyonu çağırarak cihazın ayakta olup olmadığını gördüm.


print("closing connection")
ssh_client.close()
