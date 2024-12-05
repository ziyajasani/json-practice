#!/bin/bash

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

jq -r '.features[].properties.receiptTime' aviation.json | head -n 6 | while read -r line; do
    echo "$(date -d "$line" '+%Y-%m-%d %H:%M:%S')"
done
