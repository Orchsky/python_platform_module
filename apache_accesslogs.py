import re
import csv 
import argparse
from collections import Counter

my_parser = argparse.ArgumentParser(description="Reading the log file...")
my_parser.add_argument("logfile", help='Please enter logfile to parse', type=argparse.FileType())
args = my_parser.parse_args()

logreg = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

with args.logfile as f:
    fread= f.read()
    ip_list = re.findall(logreg,fread)
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_ADRESS", "Count"])
        for k,v in Counter(ip_list).items():
            fwritercsv.writerow([k,v])