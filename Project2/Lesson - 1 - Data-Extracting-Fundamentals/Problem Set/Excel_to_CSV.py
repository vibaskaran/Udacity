# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "data/2013_ERCOT_Hourly_Load_Data.xls"
outfile = "data/2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall(path="data")


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    headers = sheet.row_values(0, start_colx=0, end_colx=None)

    writer_header = ["Station", "Year", "Month", "Day", "Hour", "Max Load"]
    data.append(writer_header)


    for i in range(1, len(headers)):
        temp_sheet_column = sheet.col_values(i, start_rowx=1, end_rowx=None)
        temp_max = max(temp_sheet_column)
        temp_max_index = temp_sheet_column.index(temp_max) + 1
        raw_max_date = sheet.cell_value(temp_max_index, 0)
        max_date_values = xlrd.xldate_as_tuple(raw_max_date, 0)


        d = [headers[i], max_date_values[0], max_date_values[1], max_date_values[2], max_date_values[3], temp_max]

        data.append(d)

    return data

def save_file(data, filename):
    with open(filename, 'wb') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(data)

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]
    print "Passed."

        
test()