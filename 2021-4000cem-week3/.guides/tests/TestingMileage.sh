#!/bin/bash

echo 0 | match -s "£0.0" runpy Mileage.py
echo 6 | match -s "£3.0" runpy Mileage.py
echo 71 | match -s "£27.57" runpy Mileage.py
echo 110 | match -s "£38.3" runpy Mileage.py
