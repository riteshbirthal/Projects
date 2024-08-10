#!/bin/bash

master_bedroom_controller_url=""
hall_controller_url=""

for ip_suffix in {1..255}
do 
    # Capture the HTTP status code for /home endpoint
    http_status=$(curl -s -o /dev/null -w "%{http_code}" http://192.168.1.$ip_suffix/home)

    if [ "$http_status" -eq 200 ]; then
        master_bedroom_controller_url="http://192.168.1.$ip_suffix"
    fi

    # Capture the HTTP status code for /check endpoint
    http_status=$(curl -s -o /dev/null -w "%{http_code}" http://192.168.1.$ip_suffix/check)

    if [ "$http_status" -eq 200 ]; then
        hall_controller_url="http://192.168.1.$ip_suffix"
    fi

    if [ -n "$master_bedroom_controller_url" ] && [ -n "$hall_controller_url" ]; then
        break
    fi
done

echo "Master Bedroom Controller URL => $master_bedroom_controller_url"
echo "Hall Controller URL => $hall_controller_url"
