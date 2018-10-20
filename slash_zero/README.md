levels: flag is slash{POSTS_MAKE_LIFE}zero
fake flag : Slash{I_am_the_real_pass}Zero
singleByteXored is sent over the packet dump.
xor the file with 0xea to get b.out
run b.out and enter Slash{I_am_the_real_pass}Zero to get a file called server.py
decode server.py with base64
change get to post in server.py
run server.py to get the flag

greyap:
command: strings * | grep slash
