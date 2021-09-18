#!/bin/bash
touch info.txt
echo 'date:' > info.txt
date >> info.txt
echo 'usr:' >> info.txt
whoami >> info.txt
echo 'os:' >> info.txt
uname >> info.txt
cur=`pwd`
#echo $cur
cd ~
echo 'folders in home:' >> $cur/info.txt
ls -l |grep ^d | wc -l >> $cur/info.txt
echo 'files in home:' >> $cur/info.txt
find -type f | wc -l >> $cur/info.txt

