import sys
import os
import csv
import string

with open( sys.argv[ 1 ], 'rb') as csvfile:
    table_string = ""
    reader       = csv.reader( csvfile )
    
    f = open("index.html", "w")
    f.write('<style type="text/css">td{padding:0 15px 0 15px;}</style>')
    f.write('<h2> ASDC Foosball Top 12')
    f.write("<table>")
    f.write('<tr style="font-weight:bold"><td>Rank</td><td>Name</td><td>Overall\t\t</td><td>Offense  </td><td>Defense  </td><td>1 Day Prior   </td><td>1 Week Prior  </td></tr>\n')
    for row in reader:
    	if int(row[4]) <= 12:
    		table_string+= "<tr><td>" + row[4] + "</td><td>" + row[0] + "</td><td>" + str(round(float(row[1]), 1)) + "</td><td>" + \
    				row[5] + " | " + str(round(float(row[2]), 1)) + "</td><td>" + row[6] + " | " + str(round(float(row[3]), 1)) + "</td><td>" + \
    				row[8] + "</td><td>" + row[12] + "</td></tr>\n"

    
    f.write(table_string)
    f.write("</table>")
    f.close()