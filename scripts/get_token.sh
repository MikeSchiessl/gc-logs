#!/bin/bash
echo -ne "ENTER GC hostname:" 
read hostname
echo -ne "Enter GC username: "
read username
echo -ne "Enter GC password: "
read password

curl -X POST -H "Content-Type: application/json" https://${hostname}/api/v3.0/authenticate -d "{\"username\": \"${username}\", \"password\": \"${password}\"}"
