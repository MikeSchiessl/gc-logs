#!/bin/bash

echo -ne "Enter GC username: "
read username
echo -ne "Enter GC password: "
read password

curl -X POST -H "Content-Type: application/json" https://${GC_URL}/api/v3.0/authenticate -d "{\"username\": \"${username}\", \"password\": \"${password}\"}"