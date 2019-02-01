#!/usr/sh 

http --ignore-stdin POST http://kong:8001/certificates cert=@/.secrets/ssl.crt key=@/.secrets/ssl.key snis:='["dereg.net"]' > /dev/null 
