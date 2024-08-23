#name
name_text = ['Name List']
my_text = ['mail to me', 'mail to myself', 'me']
rec_name_text = ['Receiver Name List']

#mail ids

my_mail = ['Sender Mail ID']

#mail_array
mail_id = ['Mail ID List']

def mail_list(name:str):
  if name in name_text:
    id = 0
    for i in range(len(name_text)):
      if name == name_text[i]:
        id = i
        break
    return 1, mail_id[id]

#mail templates
def battery_low():
  msg = "Your PC battery is low. Please plug in charger."
  sub = "Low Battery Notification"
  rec_id = "Receiver Mail ID"
  return rec_id, sub, msg

def birthday(receiver:str):
  msg = f"Wish you a very very happy birthday {receiver}"
  sub = "Birthday Notification"
  rec_id = mail_list(receiver)[1]
  return rec_id, sub, msg

def test(receiver:str):
  msg = "This is a test mail"
  sub = "Test Mail"
  rec_id = mail_list(receiver)[1]
  return rec_id, sub, msg
