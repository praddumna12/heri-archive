data = "flag{c0ld_signals_thr0ugh_dead_air}"
key = "u9s1d3X0r"

enc = ""
for i in range(len(data)):
    enc += chr(ord(data[i]) ^ ord(key[i % len(key)]))

print(enc)
