import hashlib, uuid

password_file = "100passwords.txt" #must be in same directory
file = open(password_file, "r")

salt = uuid.uuid4().hex.encode('utf-8')
password = "password".encode('utf-8')
md5_salt = hashlib.md5(password + salt).hexdigest()
print("MD5 with Salt: ", md5_salt)
print(salt)

def clean_line(line):
    line_converted = line.strip()
    line_converted = line_converted.encode('utf-8')
    return line_converted

#with salt
for line in file:
    line_converted = clean_line(line)
    hashed_password = hashlib.md5(line_converted).hexdigest()
    if(hashed_password == md5_salt):
        print(md5+" equals "+line)



