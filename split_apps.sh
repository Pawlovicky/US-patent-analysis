#!/bin/bash
name=`echo "$1" | cut -d'.' -f1`
mkdir $name
awk -v x="F_0.xml" "/<us-patent-application*/, /<\/us-patent-application>/"'{ print  > x; } /<\/us-patent-application>/ {close(x); x="F_"++i".xml"}' $1
mv *_*.xml $name
rm $1
