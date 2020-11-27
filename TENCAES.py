from Crypto.Cipher import AES
import sys,random

#encrypt file into AES
#read data from file -> encode to base64 -> split data into 16 length then encrypt data
#key and iv will be randomly generate

if len(sys.argv) != 2:
	print """
	[Usage] %s <file>
"""%sys.argv[0]
	sys.exit(1)

file = sys.argv[1]
data = open(file,"r").read().encode("base64").strip("\n").strip("\r\n").replace("\r\n","").replace("\n","");
key = '';iv = '';
while len(key) != 16 and len(iv) != 16:
	key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16)); iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)]);

data_length = len(data)

encrypted_data = []; x = 0; y = 16; length = 0
while length < data_length:
	aes = AES.new(key, AES.MODE_CBC, iv)
	if len(data[x:y]) != 16:
		chunk = " " * (16 - len(data[x:y])); rawD = data[x:y] + chunk
	else:
		rawD = data[x:y]
	length += len(rawD)
	encd = encrypted_data.append(aes.encrypt(rawD).encode('hex').replace("\n","")); x = y; y = y + 16;

print encrypted_data
print "Key: " + key.encode('base64').strip("\n").strip("\r\n").replace("\r\n","").replace("\n","")
print "IV: " + iv.encode('base64').strip("\n").strip("\r\n").replace("\r\n","").replace("\n","")
