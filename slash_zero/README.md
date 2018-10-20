#levels:\n 
flag is slash{POSTS_MAKE_LIFE}zero\n
fake flag : Slash{I_am_the_real_pass}Zero\n
singleByteXored is sent over the packet dump.\n
xor the file with 0xea to get b.out\n
run b.out and enter Slash{I_am_the_real_pass}Zero to get a file called server.py\n
decode server.py with base64\n
change get to post in server.py\n
run server.py to get the flag\n

#greyap:\n
command: strings * | grep slash
