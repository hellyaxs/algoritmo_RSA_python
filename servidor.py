import socket
import class_rsa as rsa 


def criandoServidor(n,e,d):    
  HOST = socket.gethostname()      # Endereco IP do Servidor
  PORT = 5000            # Porta que o Servidor esta
  servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  orig = (HOST, PORT)
  servidor_tcp.bind(orig)
  servidor_tcp.listen(1)  
  con, cliente = servidor_tcp.accept()
  print ('Concetado por:', cliente)
  con.send((str(n)+" "+str(e)).encode())
  msg = ''
  print("agardando dados do cliente:")
  while msg != '0':    
      msg = con.recv(1024).decode()
      msg = rsa.descifra(msg.split(" "),n,d)
      if not msg: break
      print(cliente, msg) 
  print('Finalizando conexao do cliente', cliente) 
  con.close()


print("-------------------Bem vindo----------------")
p = int(input("digite um valor para P:")) 
q = int(input("digite um valor para Q:"))
n = p*q
x = rsa.totient(p)
y = rsa.totient(q)
totient_de_N = x*y
e = rsa.generate_E(totient_de_N) # generate E
public_key = (n, e)
print("sua chave pubica é:",public_key)
private_key = rsa.calculate_private_key(totient_de_N,e)
print('sua chave privada é:', private_key)

criandoServidor(n,e,private_key)