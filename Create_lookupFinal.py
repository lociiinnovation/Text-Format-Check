#FINAL CODE
import json
import pandas as pd
import re
import unicodedata
import csv
import os

 

file_path = "NSWHEAVYFRONT.ndjson"
with open(file_path, 'r') as file:
    json_data = file.read()

 

data = json.loads(json_data)

 

#EXTRACT THE DATA FROM JSON FILE (HEAVYLICNSEFRONT.NDJSON)
class_code=data["data_row"]["external_id"]
classification_code=class_code.replace('.png', '')
fld_name="Field Name"
title_case = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][0]['radio_answer']['name']
first_name_field = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][0]['name']
last_name_case = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][1]['name']
upper_case = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][1]['radio_answer']['name']
#last_name_pos = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][2]['name']
#pos = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][2]['radio_answer']['name']
#licenceclass = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][1]['classifications'][0]['name']
#pos = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects']['bounding_box'][0]['classifications'][2]['radio_answer']['name']
#licenceClass = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][1]['classifications'][0]['radio_answer']['classifications'][0]['text_answer']['content']
licencenumber = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['name']
licno_name=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][0]['name']
licno_format= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][0]['radio_answer']['name']
licno_minlength=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][2]['name']
licno_minlength_num=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][2]['text_answer']['content']
licno_maxlength=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][3]['name']
licno_maxlength_num=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][2]['classifications'][3]['text_answer']['content']
address=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][3]['name']
address_format=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][3]['classifications'][0]['name']
address_case= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][3]['classifications'][0]['radio_answer']['name']
dob=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][4]['name']
dob_format= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][4]['classifications'][2]['name']
dob_format_number= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][4]['classifications'][2]['radio_answer']['name']
doe = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][5]['name']
doe_format = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][5]['classifications'][1]['name']
doe_format_number = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][5]['classifications'][1]['radio_answer']['name']
cardnumber=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['name']
card_minlen= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][0]['name']
card_minlen_val= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][0]['text_answer']['content']
card_maxlen= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][1]['name']
card_maxlen_val= data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][1]['text_answer']['content']
card_format=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][3]['name']
card_format_val=data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][13]['classifications'][3]['radio_answer']['name']

 

print(address_format)
print(classification_code)

 

#CREATE A DICTIONARY WITH THE EXTRACTED VALUE
conditions = {
    "givenName":{first_name_field: title_case},
    "familyName":{last_name_case:upper_case},
    licencenumber:{licno_name:licno_format,licno_minlength:licno_minlength_num,licno_maxlength:licno_maxlength_num},
    "addressLine":{address_format:address_case},cardnumber:{card_format:card_format_val,card_minlen:card_minlen_val,card_maxlen:card_maxlen_val},
    dob:{dob_format:dob_format_number}, doe:{doe_format:doe_format_number},
    "LICENSE CLASS":"upper"


 

}

 

#ADDED LICENSE CLASS TO VERIFY IF IT UPDATES NEW KEYS AND VALUES TO THE SAME DICTIONARY IF IT IS PRESENT 
print(conditions)

 

 

#DICT WITH ALL THE CLEANING PROCEDURES THAT NEEDS TO BE PERFORMED 
clean_data = {
    "givenName": "Exclude Numbers, special characters, whitespace between letters if present",
    "familyName": "Exclude Numbers, special characters, whitespace between the letters",
    licencenumber: "Exclude special characters, letters, anything after 10th position, whitespace between numbers",
    "addressLine": "Exclude special characters, anything after pincode, whitespace",
    dob: "Exclude all other special characters except / and -, whitespace",
    doe: "Exclude all other special characters except / and -, whitespace"
}

 

 

 

# Prepare DataFrame

 

excel_file = "C://Users//muppa//Desktop//Intership//Text-Format-Check-//on.xlsx"

 

 

existing_df = pd.DataFrame()
if os.path.isfile(excel_file):
    existing_df = pd.read_excel(excel_file)

 

# EMPTY DICTIONARY TO STORE CONDITIONS FOR CLASSIFICATION CODE 
conditions_dict = {}
clean_data_dict = {}

 

# CHECK IF SAME ENTRY EXISTS OR HAS MINOR CHANGES 
for index, row in existing_df.iterrows():
    if row['Classification_Code'] == classification_code:
        conditions_dict[classification_code] = row['Format Checks']
        clean_data_dict[classification_code] = row['Cleaning Required']
        break

 

if classification_code in conditions_dict:
    if conditions_dict[classification_code] == conditions and clean_data_dict[classification_code] == clean_data:
        print("Entry already exists with identical conditions and clean_data. Skipping...")
    else:

        #UPDATE THE DICTIONARY WITH THE NEW COLUMN FOR CLEANING PROCEDURE
        conditions_dict[classification_code] = conditions
        clean_data_dict[classification_code] = clean_data
        print("Updated existing entry with new conditions and clean_data.")
else:
    # ADD NEW ENTRY TO THE DICTIONARY 
    conditions_dict[classification_code] = conditions
    clean_data_dict[classification_code] = clean_data
    print("Added new entry to the dictionaries.")

 

# CONVERT CONDITIONS AND CLEAN DATA DICTIONARY BACK TO DATAFRAME 
new_rows = []
for code, conds in conditions_dict.items():
    new_rows.append({'Classification_Code': code, 'Format Checks': conds, 'Cleaning Required': clean_data_dict[code]})
new_df = pd.DataFrame(new_rows)

 

# COPY DATFRAME BACK TO EXCEL FILE 
try:
    new_df.to_excel(excel_file, index=False)
    print("Data has been extracted and added/updated in the Excel file.")
except Exception as e:
    print("An error occurred while writing to the Excel file:", e)

 

# TEST :ADD NEW CLASSIFICATION CODE 
new_classification_code = "DRIVER LICENSE"
new_conditions = {
    "givenName": {"fieldName": "Title Case"},
    "familyName": {"fieldName": "Upper Case"},
    "license Class":"UPPER"
}
new_clean_data = {
    "givenName": "Exclude Numbers, special characters, whitespace between letters if present",
    "familyName": "Exclude Numbers, special characters, whitespace between the letters",
    # Add more clean_data as needed
}

 

# Update the conditions and clean_data dictionaries with the new classification code and data
conditions_dict[new_classification_code] = new_conditions
clean_data_dict[new_classification_code] = new_clean_data

 

# Convert the conditions and clean_data dictionaries back to DataFrames
new_rows = []
for code, conds in conditions_dict.items():
    new_rows.append({'Classification_Code': code, 'Format Checks': conds, 'Cleaning Required': clean_data_dict[code]})
new_df = pd.DataFrame(new_rows)

 

# Write DataFrame to Excel file
try:
    new_df.to_excel(excel_file, index=False)
    print("Data has been extracted and added/updated in the Excel file.")
except Exception as e:
    print("An error occurred while writing to the Excel file:", e)