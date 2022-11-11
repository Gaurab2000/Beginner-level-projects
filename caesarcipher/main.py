alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


"""
this below function is shortened into one further below
def encrypt(plain_text,shift_amount):
  cipher_text=""
  for letter in plain_text:
   position = alphabet.index(letter)
   new_position=position+shift_amount
   new_letter = alphabet[new_position]
   cipher_text+=new_letter
  print(f"The encoded text is {cipher_text}") 

def decrypt(cipher_text,shift_amount):
  plain_text=""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text+=alphabet[new_position]
  print(f"the decoded text is {plain_text} ")
    
  
if direction == "encode":
  encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text,shift_amount=shift)
"""
  #the above two function can be written into one as
  
  def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position= alphabet.index(char)
      new_position= position +shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
   
   
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
 
  shift=shift%25
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result=input("type yes if you want to go again otherwise no \n")
  if result == "no":
   should_continue= False
print (" bye bye")  
