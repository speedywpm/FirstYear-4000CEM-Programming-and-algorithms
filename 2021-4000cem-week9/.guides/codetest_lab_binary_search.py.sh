#!/bin/bash

files=("lab_binary_search_iterative.py" "lab_binary_search_recursive.py")

for file in "${files[@]}"
do
	echo "$file"
  runpy "$file"
  if [[ $? -eq 0 ]]
  then
    exit 0
  fi
  
  echo ""
done

exit 1
