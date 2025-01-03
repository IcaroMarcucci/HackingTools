#!/bin/bash
# Use Mode: ./direcon TARGET_URL PATH_WORDLIST

if [ $# -ne 2 ]; then
    echo "Uso correto: ./direcon TARGET_URL PATH_WORDLIST"
    exit 1
fi

for word in $(cat $2)

do

result=$(curl -s -H "User-Agent: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36" -o /dev/null -w "%{http_code}" $1/$word/)

if [ "$result" == "200" ]; then
echo "Directory Found: $1/$word/"
fi

done