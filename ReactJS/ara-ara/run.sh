#!/bin/bash

# Clear the terminal
clear

# Initialize variables
mb_ctrl_url=""
hall_ctrl_url=""

# Function to check if the URL responds with HTTP 200 status
check_url() {
    local url=$1
    curl -s --max-time 3 -o /dev/null -w "%{http_code}" "$url"
}

# Colors for echo statements
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print a fancy banner
print_banner() {
    local message=$1
    echo -e "${YELLOW}=============================================${NC}"
    echo -e "${GREEN}$message${NC}"
    echo -e "${YELLOW}=============================================${NC}"
}

# Loop through IP suffixes to find the controllers
for ip_suffix in {1..255}; do 
    base_url="http://192.168.1.$ip_suffix"
    echo -e "${YELLOW}Scanning IP address: $base_url${NC}"

    # Check /home endpoint
    url="$base_url/home"
    http_status=$(check_url "$url")

    if [ "$http_status" -eq 200 ]; then
        mb_ctrl_url="$base_url"
        echo -e "${GREEN}Master Bedroom Controller found at $mb_ctrl_url${NC}"
    fi

    # Check /check endpoint
    url="$base_url/check"
    http_status=$(check_url "$url")

    if [ "$http_status" -eq 200 ]; then
        hall_ctrl_url="$base_url"
        echo -e "${GREEN}Hall Controller found at $hall_ctrl_url${NC}"
    fi

    if [ -n "$mb_ctrl_url" ] && [ -n "$hall_ctrl_url" ]; then
        break
    fi
done

# Check if the URLs were found
if [ -z "$mb_ctrl_url" ] || [ -z "$hall_ctrl_url" ]; then
    echo -e "${RED}Error: Unable to locate one or both controllers.${NC}"
    exit 1
fi

print_banner "Controller URLs Detected"
echo -e "${GREEN}Master Bedroom Controller URL: $mb_ctrl_url${NC}"
echo -e "${GREEN}Hall Controller URL: $hall_ctrl_url${NC}"

# Export the URLs as environment variables (assuming your React app uses them)
export REACT_APP_MB_CTRL_URL=$mb_ctrl_url
export REACT_APP_HALL_CTRL_URL=$hall_ctrl_url

# Start the React app (assuming you are using npm)
npm start
