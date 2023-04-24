#!/bin/bash
pwd
cd ../../files/
# cat results.csv | grep FALSE$
# cat results.csv | grep ^2018-06-03. | grep Costa | wc -l
cat results.csv | grep ^2018-06-03. | grep Costa | grep Ireland
