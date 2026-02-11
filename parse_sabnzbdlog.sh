
echo "All lookups: newsservers with their ipv6:"
cat logs/sabnzbd.log | grep -i -e Fastest | awk '{ print $6 " " $11 }'  | sort -u | tee all.txt


echo "All failed:"
cat logs/sabnzbd.log | grep -i -e "no route to host" | awk -F'[@:]' '{print $(NF-1)}'  | sort -u | tee no-route.txt

echo "FAILED ... with their ipv6 addresses:"
cat no-route.txt | awk '{ print "grep " $1 " all.txt" }'  | sh

