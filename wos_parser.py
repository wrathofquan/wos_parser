import os
import gc
import pandas as pd
import wos_parser as wp

#place xml files in parser folder


directory = ("./")

# Funding/Dynamic Id/Conferences/Addresses/Publisher/Pub Info/Authors

gc.collect()

temp_funding = pd.DataFrame()
temp_identifier = pd.DataFrame()
temp_conferences = pd.DataFrame()
temp_addresses = pd.DataFrame()
temp_publisher = pd.DataFrame()
temp_pub_info = pd.DataFrame()
temp_authors = pd.DataFrame()


for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith('.xml'):
         records = wp.read_xml(filename)
         funding = [wp.extract_funding(record) for record in records]
         temp_funding = temp_funding.append(funding)
         identifiers = [wp.extract_identifiers(record) for record in records]
         temp_identifier = temp_identifier.append(identifiers)
         conferences = [wp.extract_conferences(record) for record in records]
         conferences = pd.concat(map(pd.DataFrame, conferences), sort = True)
         temp_conferences = temp_conferences.append(conferences)
         addresses= [wp.extract_addresses(record) for record in records]
         addresses = pd.concat(map(pd.DataFrame, addresses), sort = True)
         temp_addresses = temp_addresses.append(addresses)
         publisher = [wp.extract_publisher(record) for record in records]
         publisher = pd.concat(map(pd.DataFrame, publisher), sort = True)
         temp_publisher = temp_publisher.append(publisher)
         pub_info = [wp.extract_pub_info(record) for record in records]
         temp_pub_info = temp_pub_info.append(pub_info)
         authors = [wp.extract_authors(record) for record in records]
         authors = pd.concat(map(pd.DataFrame, authors), sort = True)
         temp_authors = temp_authors.append(authors)


temp_funding.to_csv(f'{filename[3:22]}_funding.csv', index = False)
temp_identifier.to_csv(f'{filename[3:22]}_identifier.csv', index = False)
temp_conferences.to_csv(f'{filename[3:22]}_conferences.csv', index = False)
temp_addresses.to_csv(f'{filename[3:22]}_addresses.csv', index = False)
temp_publisher.to_csv(f'{filename[3:22]}_publisher.csv', index = False)
temp_pub_info.to_csv(f'{filename[3:22]}_pub_info.csv', index = False)
temp_authors.to_csv(f'{filename[3:22]}_authors.csv', index = False)



gc.collect()

# References

temp = pd.DataFrame()

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith('.xml'):
         records = wp.read_xml(filename)
         references = [wp.extract_references(record) for record in records]
         references = pd.concat(map(pd.DataFrame, references), sort = True)
         temp = temp.append(references)

temp.to_csv(f'{filename[3:22]}_references.csv', index = False)
