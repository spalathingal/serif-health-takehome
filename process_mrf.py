import ijson
import time

# Parse through large json and obtain New York Anthem PPO URLs
def parseFile(json):
    # set of seen URLs (no duplicates)
    seen_urls = set()
    
    # open input and output files
    file = open(json, 'rb')
    output = open("result.txt","w")
    
    # initialize parser.
    parser = ijson.parse(file)
    
    # loop through json using parser
    for prefix, _, value in parser:
        # check description
        if prefix=='reporting_structure.item.in_network_files.item.description':
            desc = value.upper()
        # check location
        if prefix=='reporting_structure.item.in_network_files.item.location':
            if 'NEW YORK' in desc and 'PPO' in desc:
                # add to set & output if not seen
                if value not in seen_urls:
                    seen_urls.add(value)
                    output.write(f"{value}\n")
    
    # close input and output files
    file.close()
    output.close()
    
    return

parseFile('2024-02-01_anthem_index.json')