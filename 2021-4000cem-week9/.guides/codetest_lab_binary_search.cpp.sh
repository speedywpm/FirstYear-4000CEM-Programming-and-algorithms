#!/bin/bash

files=("lab_binary_search_iterative.cpp" "lab_binary_search_recursive.cpp")

for file in "${files[@]}"
do
	echo "$file"
  runcpp "$file"
  if [[ $? -eq 0 ]]
  then
    exit 0
  fi
  
  echo ""
done

exit 1
