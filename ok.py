import json
import pandas as pd
import re

file_path = "NSWHEAVYFRONT.ndjson"
with open(file_path, 'r') as file:
    json_data = file.read()

data = json.loads(json_data)


title_case = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][0]['radio_answer']['name']
first_name_case = data['projects']['clj6fmxu8046q07zb7loafftz']['labels'][0]['annotations']['objects'][0]['classifications'][0]['name']
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

 
print("licencenumber:",licencenumber )
print("LICENSE FORMAT",licno_name)
print("License format",licno_format)
print("Min lenth",licno_minlength)
print("MIn length value",licno_minlength_num)
print("Max length name",licno_maxlength)
print("Max Length number",licno_maxlength_num)
print("Address",address)
print("Address case",address_case)
print("DOB",dob)
print("DOB format",dob_format)
print("DOB format number",dob_format_number)
print("DOE",doe)
print("DOE format", doe_format)
print("DOE format number", doe_format_number)
print("Card Number",cardnumber)
print("Min legh card",card_minlen)
print("Min length card value",card_minlen_val)
print("Max legh card",card_maxlen)
print("Max length card value",card_maxlen_val)
print("card format",card_format)
print("Card format value",card_format_val)
print("lastNameCase:", last_name_case)
print("UPPER CASE:", upper_case)
#print(licenceclass)
#print(last_name_pos)

conditions = {
    first_name_case: {title_case},
    last_name_case:{upper_case},
    licencenumber:{licno_name:licno_format,licno_minlength:licno_minlength_num,licno_maxlength:licno_maxlength_num},
    address:{address_case},cardnumber:{card_format:card_format_val,card_minlen:card_minlen_val,card_maxlen:card_maxlen_val},
    dob:{dob_format:dob_format_number},
    doe:{doe_format:doe_format_number}
}
print(conditions)

df = pd.read_csv('extract_data.csv', dtype={'cardnumber': str})
#df['Last name'] = df['Last name'].fillna('Unknown')
#df['First name'].fillna('Unknown', inplace=True)

check_counters = {
    'first_name_case_count': {'valid': 0, 'invalid': 0},
    'last_name_case_count': {'valid': 0, 'invalid': 0},
    'licence_number_count ': {'valid': 0, 'invalid': 0},
    'address_case_count': {'valid': 0, 'invalid': 0},
    'dob_format_count': {'valid': 0, 'invalid': 0},
    'doe_format_count': {'valid': 0, 'invalid': 0},
    'card_number_count': {'valid': 0, 'invalid': 0}}

#Function to verify if the first name is in title case
def is_title_case(name):
    return name.istitle()

# Function to check if a last name is in upper case
def is_upper_case(name):
    return name.isupper()

# Function to check if a license number and card number is numeric
def is_numeric(value):
    return str(value).replace(" ", "").isdigit()

# Function to check if a value has a minimum length
def has_min_length(value, min_length):
    return len(str(value)) >= int(min_length)

# Function to check if a value has a maximum length
def has_max_length(value, max_length):
    return len(str(value)) <= int(max_length)

def is_valid_dob_format(dob):
        dob_pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$'
        return re.match(dob_pattern, dob) is not None

def is_valid_dob(dob):
    try:
        dob_day, dob_month, dob_year = map(int, dob.split('/'))
        if 1 <= dob_day <= 31 and 1 <= dob_month <= 12:
            return True
        else:
            return False
    except (ValueError, IndexError):
        return False
    
def is_valid_doe_format(doe):
        doe_pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$'
        return re.match(doe_pattern, doe) is not None

def is_valid_doe(doe):
    try:
        doe_day, doe_month, doe_year = map(int, doe.split('/'))
        if 1 <= doe_day <= 31 and 1 <= doe_month <= 12:
            return True
        else:
            return False
    except (ValueError, IndexError):
        return False

 
for index, row in df.iterrows():
    first_name = row['First name']
    middle_name = row['Middle name']
    last_name = row['Last name']
    licence_number = row['LicenceNumber']
    address = row['CLEAN ADDRESS']
    card_number = row['cardnumber']
    dob = row['DOB']
    doe=row['DOE']
    #print(card_number)
    #print(last_name)
    #print(first_name)
    #print(doe)

    #Check for blank values in first name 
    if pd.isnull(first_name) or first_name.strip() == '':
        print(f"Record {index + 1}: First name cannot be left blank.")
        check_counters['first_name_case_count']['invalid'] += 1
        print("check_counters",check_counters['first_name_case_count']['invalid'])
        continue

    # Check if last name is blank
    if pd.isnull(last_name) or last_name.strip() == '':
        print(f"Record {index + 1}: Last name cannot be left blank.")
        check_counters['last_name_case_count']['invalid'] += 1
        print("check_counters_last_name",check_counters['last_name_case_count']['invalid'])
        continue

    if pd.isnull(dob) or dob.strip() == '':
        print(f"Record {index + 1}: Date of Birth (DOB) cannot be left empty.")
        check_counters['dob_format_count']['invalid'] += 1
        print("check_counters_dob_format_count",check_counters['dob_format_count']['invalid'])
        continue  # Skip rest of the checks for this record

    if pd.isnull(doe) or doe.strip() == '':
        print(f"Record {index + 1}: Date of Expiry (DOE) cannot be left empty.")
        check_counters['doe_format_count']['invalid'] += 1
        print("check_counters_doe_format_count",check_counters['doe_format_count']['invalid'])
        continue  # Skip rest of the checks for this record

    if pd.isnull(card_number) or card_number.strip() == '':
        print(f"Record {index + 1}: Card number cannot be left empty.")
        continue 

    if pd.isnull(address) or address.strip() == '':
        print(f"Record {index + 1}: Address cannot be left empty.")
        continue

    
    # Check conditions for first name
    if 'firstNameCase' in conditions and not is_title_case(first_name):
        print(f"Record {index + 1}: First name should be in title case.")

    # Check conditions for last name
    if 'lastNameCase' in conditions and not is_upper_case(last_name):
        print(f"Record {index + 1}: Last name should be in upper case.")

    # Check conditions for licence number
    licno_conditions = conditions.get('licenceNumber', {})
    if licno_conditions.get('dataType') == 'NUMERIC':
        if not is_numeric(licence_number):
            print(f"Record {index + 1}: Licence number should be numeric.")
        if licno_conditions.get('minLength') and not has_min_length(licence_number, licno_conditions['minLength']):
            print(f"Record {index + 1}: Licence number should have a minimum length of {licno_conditions['minLength']}.")
        if licno_conditions.get('maxLength') and not has_max_length(licence_number, licno_conditions['maxLength']):
            print(f"Record {index + 1}: Licence number should have a maximum length of {licno_conditions['maxLength']}.")

    # Check conditions for address
    if 'address' in conditions:
        address_conditions = conditions['address']
        if address_conditions == 'UPPER CASE' and not is_upper_case(address):
            print(f"Record {index + 1}: Address should be in upper case.")

    # Check for card number 
    card_conditions = conditions.get('cardNumber', {})
    #print(card_conditions)
    if card_conditions.get('dataType') == 'NUMERIC':
        if not is_numeric(card_number):
            print(f"Record {index + 1}: Card number should be numeric.")
        if card_conditions.get('minLength') and not has_min_length(card_number, card_conditions['minLength']):
            print(f"Record {index + 1}: Card number should have a minimum length of {card_conditions['minLength']}.")
        if card_conditions.get('maxLength') and not has_max_length(card_number, card_conditions['maxLength']):
            print(f"Record {index + 1}: Card number should have a maximum length of {card_conditions['maxLength']}.")

    if not is_valid_dob_format(dob):
        print(f"Record {index + 1}:Invalid DOB format. It should be in 'd/mm/yyyy' or 'dd/mm/yyyy' format.")      

    if not is_valid_dob(dob):
        print(f"Record {index + 1}: Invalid DOB. Day should be between 1 and 31, and month should be between 1 and 12.")

    # check for DOE
    if not is_valid_doe_format(doe):
        print(f"Record {index + 1}:Invalid DOB format. It should be in 'd/mm/yyyy' or 'dd/mm/yyyy' format.")      

    if not is_valid_doe(doe):
        print(f"Record {index + 1}: Invalid DOB. Day should be between 1 and 31, and month should be between 1 and 12.")
