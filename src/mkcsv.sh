#!/bin/bash

#bunzip2 $1
#file=$(basename $1 .bz2)
file=$1
dir=$(dirname $0)

$dir/json2csv.py $file
head -n1 "${file}.csv" > ${file}.csv-shuf
sed 1d ${file}.csv | shuf >> ${file}.csv-shuf
rm ${file}.csv
mv ${file}.csv-shuf ${file}.csv
