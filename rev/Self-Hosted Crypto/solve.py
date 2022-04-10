file = open("encrypted", "rb")
content = file.read()
print(''.join([chr(b - ord('\r')) for b in content]))