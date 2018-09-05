#!/bin/bash
name=`echo "$1" | cut -d'.' -f1`
mkdir $name
awk -v x="F_0.xml" "/<\/us-patent-application>/ "'{ print "</us-patent-application>" > x; x="F_"++i".xml";next}{ print > x; }' $1
mv *_*.xml $name
rm $1
