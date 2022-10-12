import re
import csv 
import argparse
from collections import Counter

logreg = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

my_parser = argparse.ArgumentParser(description="Reading the log file...")
my_parser.add_argument("logfile", help='Please enter logfile to parse', type=argparse.FileType())
args = my_parser.parse_args()

def read_file(logfile):
    with args.logfile as f:
        fread = f.read()
        ip_list = re.findall(logreg,fread)
        return ip_list

def read_count():
    ip_list = read_file(args.logfile)
    ip_count = Counter(ip_list)
    return ip_count.items()

def csv_write():
    counter = read_count()
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_ADRESS", "Count"])
        for k,v in counter:
            fwritercsv.writerow([k,v])

if __name__ == '__main__':
    csv_write()