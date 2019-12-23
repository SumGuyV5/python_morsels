import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='fix csv files')
parser.add_argument('--in-delimiter', help='the delimiter used in the original file.')
parser.add_argument('--in-quote', help='the quote.')
parser.add_argument('read_file')
parser.add_argument('write_file')


def main(original, fixed, delim, quote):
    with open(original, 'r', newline='') as csvfile:
        arguments = {}
        if delim:
            arguments['delimiter'] = delim
        if quote:
            arguments['quotechar'] = quote
        if not delim and not quote:
            arguments['dialect'] = csv.Sniffer().sniff(csvfile.read())
            csvfile.seek(0)
        readercsv = csv.reader(csvfile, **arguments)

        csvfix = open(fixed, 'w', newline='')
        writercsv = csv.writer(csvfix)
        for row in readercsv:
            writercsv.writerow(row)
        csvfix.close()


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    main(args.read_file, args.write_file, args.in_delimiter, args.in_quote)