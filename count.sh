#!/bin/bash


#get the text and rename it to "readme_text"
wget -O readme_text ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README


#every word in separate line and lower-case
cat readme_text | tr " " "\n" | tr A-Z a-z

#select all words and count quantity, show 10 most frequent words and delete the number
cat readme_text | tr -c '[:alnum:]' '[\n*]' | sort | uniq -c | sort -nr | head -10 | tr -d 0-9
