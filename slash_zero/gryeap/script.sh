#! /bin/bash
for n in {1..1000}; do
    base64 /dev/urandom | head -c 1024 >file$( printf %03d "$n" ).txt
done