# Serif Health Takehome Solution

## Overview
Here is my approach to the Serif Health Takehome assessment found [here](https://github.com/serif-health/takehome) submitted February 2024.


## Task
The input to this takehome is the Anthem machine readable index file [table of contents](https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2024-02-01_anthem_index.json.gz) for February 2024. 

To write code to open a machine readable index file and process it according to the schema published at [CMS' transparency in coverage repository](https://github.com/CMSgov/price-transparency-guide/tree/master/schemas/table-of-contents), and extract the data requested: 

**What is the list of machine readable file URLs that represent the Anthem PPO network in New York state?**

## PreReqs
Python 3
- Install [Python3](https://www.python.org/downloads/) if you don't already have it
- Install [pipenv](https://pipenv.pypa.io/en/latest/) using pip/homebrew/apt
Run '''pipenv install'''

## Approach
My approach was to use a python library for reading large JSON files. I picked [ijson](https://pypi.org/project/ijson/) as this is a solution to work with data as a stream, rather than a block.
Your output should be the list of machine readable file URLs corresponding to Anthem's PPO in New York state. Make sure to read through the hints and pointers section before declaring your solution complete.

## Metrics
-This took me about 3 hours to complete
-Processing the file takes about 2.5 mins (ends in premature EOF error)

### TradeOffs
-I had to write to the output per each url as opposed to waiting for the processing to finish just so I could see output as it came (to ensure it was working)
-I had to download the file, then extract, and then process when I should have figured out how to do it through code
-I manually typed the filename and had to create the output file ahead of time
