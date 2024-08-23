import base64

def encoder(password:str):
  password = password.encode("utf-8")
  encoded_password = base64.b64encode(password)
  return str(encoded_password)[2:-1]

def decoder(encoded_password:str):
  encoded_password = encoded_password.encode("utf-8")
  decoded_password = base64.b64decode(encoded_password)
  return str(decoded_password)[2:-1]