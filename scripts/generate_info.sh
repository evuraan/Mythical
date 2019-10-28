#!/bin/bash 

a="/tmp/$RANDOM-$RANDOM-$RANDOM"
out="/var/lib/mythtv/recordings/recordings.txt"

mysql -u mythtv -pmythtv -e "select title,description,basename,filesize,progstart from recorded order by progstart desc" mythconverg  | sed -e "s/\t/###---###/g"  > $a 
[ -s $a ] && {
	egrep -vi "title###---###description###---###basename###---###filesize###---###progstart" $a > $out
	rm -v $a || : 
}
