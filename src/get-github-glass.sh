#!/bin/bash
OLDIFS=$IFS
IFS='\n'
response=($(curl -Lso- "https://github.com/kato-k" | grep "var(--color-calendar-graph" | grep "data-date" | awk '{print $9,$7}' | sed "s/fill=\"var(--color-calendar-graph-day-//" | sed "s/-bg)\"//" | sed "s/data-date=\"//" | sed "s/\"\/\>//" | sed "s/)\"//" | sed "s/L//" | sed "s/bg/0/"))
echo $response
IFS=$OLDIFS
