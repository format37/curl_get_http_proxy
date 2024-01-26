#!/bin/bash

# Proxy server URL
PROXY_URL="http://localhost:5000/send_message"

# Message to send
MESSAGE="Test 01"

# URL-encode the message
ENCODED_MESSAGE=$(echo $MESSAGE | sed 's/ /%20/g')

# Send GET request
curl "${PROXY_URL}?message=${ENCODED_MESSAGE}"
