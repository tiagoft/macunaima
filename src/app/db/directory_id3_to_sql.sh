#!/bin/sh

echo $1

files=$1/*.mp3
for fname in $files
do

  python src/app/db/id3tosql.py $fname ./db/macunaima.db
done
