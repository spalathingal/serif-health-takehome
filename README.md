# Serif Health Takehome Interview

This repository contains the files and instructions for our takehome engineering interview. Please *locally* copy to your own public repo or [import](https://github.com/new/import) to your github account for use in sharing solutions back to us. Direct public forks and pull requests will expose your identity and solution to other candidates also working on this interview question, and we want the interview process to be fair for everyone. 

## Context
Serif Health was founded with a mission to make the US healthcare system more transparent, efficient, and affordable for everyone. One of the challenging problems we're solving at Serif Health is making healthcare *pricing* data transparent and uniform for all market participants. There are myriad reasons this is difficult.

At the macro level:
- Data in healthcare is protected by law, sensitive by default and tends to be locked up in proprietary systems or data formats.
- The data aggregators and clearinghouses that do have access to clean, normalized bulk data assets tend to employ extremely expensive and restrictive licensing terms. 
- Recent price transparency laws have required hospitals to publish their pricing, data sharing occurs at varying levels of completeness and consistency, and hospitals are only a fraction of the overall healthcare market.  

At the micro level:
- Medical billing and coding for a specific procedures can very complicated and is contingent on place of service, comorbidities, and structure of insurance arrangements. 
- Insurance companies (payers) establish pre-negotiated non-published contracted rates with each facility, physician group, or health system that reimburses the healthcare provider at a rate very different from what is 'charged'. 

Summed together, all this complexity contributes to a general lack of transparency and market efficency in our healthcare system.


## Objective
Our customers typically want to know and compare reimbursement rates for healthcare services from specific payers. As mentioned earlier, one public data source for reimbursement rates is hospital price transparency files - most hospitals at this point are at least partially compliant publishing their reimbursement rates. Unfortunately, those files do not come in a standardized format. 

The objective for this takehome is to write a script that can take the data from a couple of hospital price transparency files, parse them, and transform them to a normalized format we can ingest and leverage in our data warehouse for aggregation, search, and display by our customers. 


## Inputs
The input to this takehome are two JSON format hospital price files from different healthcare systems. A typical 'price' entity in these files consists of a procedure name, CPT or DRG code, code type (indicating procedure type which it is), gross charge (what is billed to the payer), and reimbursement rate (the mean rate the payer actually pays the provider under the established contract). 

[Centinela Hospital](https://www.centinelamed.com/261150758_CentinelaHospitalMedicalCenter_standardcharges.json)

[Advent Health Shawnee Mission Hospital](https://www.adventhealth.com/sites/default/files/CDM/2022/480637331_AdventHealthShawneeMission_standardcharges.json)

You should write code that can read in these two files (it's ok to copy them locally / assume on local disk if easier to work with), extract the price entities contained within, and convert the data into the requested output format below. 

## Outputs
Your output should be one CSV file per input file (two CSV files total) with the following header columns:
`CPT/DRG Code, Code Type, Procedure Description, Gross Charge, Insurance Payer Name, Insurance Rate`

You should extract as many of these 'price' rows as you can *without duplicating entries* and *ignoring empty or malformed data fields* (denoted by 'N/A', empty strings, etc.). 

For simplicity's sake you should ignore complicating data fields like modifiers, inpatient/outpatient status, provider specialities, facility types and other details that might be in the file. We can discuss these in the follow up. 


## Hints and Pointers
As you start working with the files, you'll quickly notice that field names aren't standardized and can overlap in non-ideal ways. For example, 'procedure code' in one of the files is a generic internal hospital identifier, NOT the industry-standard CPT or DRG code. Payer data might be represented as a tuple of payer_name and payer_rate, or it might be just key-value pairs of payer names to prices. Use your best judgement to proceed here, and discuss your decisions in your writeup. 


### Deliverable
You should send us a link to a public repository or zip file that contains at miminum:
1. The script or code used to parse the file and produce output. 
2. The setup or packaging file(s) required to bootstrap and execute your solution code
3. The two CSV output files generated by your code
4. A README file, explaining your solution, how long it took you to write, and the tradeoffs you made along the way. 

## Expectations
### Time vs Quality
We are a small engineering team with limited resources, and often have to make hard tradeoffs to meet deadlines and make rapid forward progress. We do not want this takehome to take more than a few hours out of your day. So, please timebox coding your solution to two hours max, and know that you have the opportunity to discuss the tradeoffs you made when submitting your solution. Experienced engineers should be able to complete the coding portion in about 90 minutes, perhaps less if you have prior healthcare experience. If you think this will take you dramatically more time than that, let us know before starting the takehome so we can discuss why. 

If you finish early, we'd recommend adding additional notes or commentary to the README (e.g. discussion of performance characteristics, how you would ideally test/deploy/run your code in a production environment, feature iterations that might come next, so on), but please don't exceed the timebox doing so. 

### Language Choice
You can choose any language you want, but your solution should be portable enough to run on someone else's machine. 

### Dependencies
You can and *probably should* use dependencies (JSON parsers, type validators, etc) and libraries from public package managers in your language of choice. Again, your solution should be portable enough to run on someone else's machine, so if you leverage packaged dependencies this please make sure relevant setup instructions to install the dependencies and execute the solution are included.
