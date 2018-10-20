*levels*:<br/>
flag is slash{POSTS_MAKE_LIFE}zero<br/>
fake flag : Slash{I_am_the_real_pass}Zero<br/>n
singleByteXored is sent over the packet dump.<br/>
xor the file with 0xea to get b.out<br/>
run b.out and enter Slash{I_am_the_real_pass}Zero to get a file called server.py<br/>
decode server.py with base64<br/>
change get to post in server.py<br/>
run server.py to get the flag<br/>

*greyap*:<br/>
command: strings * | grep slash
