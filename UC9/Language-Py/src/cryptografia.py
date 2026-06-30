import bcrypt as bc
from os import system

system("clear")

senha = b"123@senhacomplexa"

print(f"Bytes da senha: {senha}")

salt = bc.gensalt()
senha_cripto = bc.hashpw(senha, salt)
print(f"Senha criptografada: {senha_cripto}")