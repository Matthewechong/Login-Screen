from cryptography.fernet import Fernet
import pandas as pd
# generate a key, write key into key.txt file
def create_key():
    key = Fernet.generate_key()
    file = open('key.txt','wb')
    file.write(key)


#Create function to get key value from key.txt
def get_key():
    file = open('key.txt','rb')
    key = file.read()
    #Fernet is an object type
    key = Fernet(key)
    return key


#Encryption
def encrypt_msg(message,key):
    print("Encrypt")
    encMessage = key.encrypt(message.encode())
    # print("Encoded message is: " + encMessage)
    print("Encoded message is: {}".format(encMessage))
    return encMessage

# Decryption
def decrypt_msg(message,key):
    print("Decrypt")
    decMessage = key.decrypt(message).decode()
    print("Decoded message is: {}".format(decMessage))
    return decMessage

def stringToBytes(message):
    message = bytes(message, 'utf-8')
    message = list(message)[2:len(message)-1]
    message = bytes(message)
    return message


# Username: matthewechong
# Password: asian12
def decrypt_data(username):
    df = pd.read_csv('credentials.csv')
    key = get_key()
    index = None
    usernames = df['Username']
    usernames = list(usernames)
    for i in range(len(usernames)):
        if username == decrypt_msg(stringToBytes(usernames[i]),key):
            index = i
            break
    if index == None:
        return index
    else:
        user_info = {
            'Username' : df['Username'].iloc[index],
            'Password' : df['Password'].iloc[index],
            'First' : df['First'].iloc[index],
            'Last' : df['First'].iloc[index]
        }
        return user_info

def check_password(original,copy):
    if original == copy:
        return True
    return False

def encrypt_data(values):
    df = pd.read_csv('credentials.csv')
    key = get_key()
    all_values = []
    for i in range(len(values)):
        safe = encrypt_msg(values[i],key)
        all_values.append(safe)

    df.loc[len(df.index)] = [all_values[2],all_values[3],all_values[0],all_values[1]]
    df.to_csv("credentials.csv",index= False)
    