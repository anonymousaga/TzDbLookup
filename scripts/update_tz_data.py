#!/usr/bin/env python3
import csv
import requests
import os

url = "https://raw.githubusercontent.com/nayarsystems/posix_tz_db/master/zones.csv"
response = requests.get(url)
lines = response.text.splitlines()

reader = csv.reader(lines)

# Ensure target directory exists
os.makedirs("src", exist_ok=True)

with open("src/tz_data.h", "w") as header:
    header.write("#pragma once\n\nstruct TzEntry {\n  const char* iana;\n  const char* posix;\n};\n\n")
    header.write("static const TzEntry tzTable[] PROGMEM = {\n")
    for row in reader:
        iana, posix = row
        header.write(f'  {{"{iana}", "{posix}"}},\n')
    header.write("};\n")
    header.write("static const size_t tzCount = sizeof(tzTable) / sizeof(tzTable[0]);\n")
