import hashlib, uuid

password_file = "100passwords.txt" #must be in same directory
file = open(password_file, "r")

password = "password".encode('utf-8')
md5 = hashlib.md5(password).hexdigest()

def clean_line(line):
    line_converted = line.strip()
    line_converted = line_converted.encode('utf-8')
    return line_converted

for line in file:
    line_converted = clean_line(line)
    hashed_password = hashlib.md5(line_converted).hexdigest()
    if(hashed_password == md5):
        print(md5+" equals "+line)



