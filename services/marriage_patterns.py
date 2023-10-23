import re

def extract_name(text: str) -> str:
    name_pattern = re.compile(r'01, Jaran/Citizen:\n(.*?)\n', re.DOTALL)
    name_match = name_pattern.search(text)
    if name_match:
        return name_match.group(1).strip()
    return ""

def extract_dob(text: str) -> str:
    dob_pattern = re.compile(r'02. Tuulgan/ Born:(.*?)\n', re.DOTALL)
    dob_match = dob_pattern.search(text)
    if dob_match:
        return dob_match.group(1).strip()
    return ""

def extract_place_of_birth(text: str) -> str:
    place_of_birth_pattern = re.compile(r'03. Tuulgan Jery/ Place of birth:(.*?)\n', re.DOTALL)
    place_of_birth_match = place_of_birth_pattern.search(text)
    if place_of_birth_match:
        return place_of_birth_match.group(1).strip()
    return ""

def extract_citizenship(text: str) -> str:
    citizenship_pattern = re.compile(r'04. Zharandygy/Citizenship:\n(.*?)\n', re.DOTALL)
    citizenship_match = citizenship_pattern.search(text)
    if citizenship_match:
        return citizenship_match.group(1).strip()
    return ""


def extract_spouse_name(text: str) -> str:
    spouse_name_pattern = re.compile(r'06. zhana jaran/ and citizen:(.*?)\n', re.DOTALL)
    spouse_match = spouse_name_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""

def extract_spouse_dob(text: str) -> str:
    spouse_dob_pattern = re.compile(r'07. Tuulgan/Born:(.*?)\n', re.DOTALL)
    spouse_match = spouse_dob_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""


def extract_spouse_birth_place(text: str) -> str:
    spouse_place_of_birth_pattern = re.compile(r'08. Tuulgan Jery/Place of birth:(.*?)\n', re.DOTALL)
    spouse_match = spouse_place_of_birth_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""

def extract_spouse_citizen(text: str) -> str:
    spouse_citizenship_pattern = re.compile(r'09. Zharandygy/Citizenship:\n(.*?)\n', re.DOTALL)
    spouse_match = spouse_citizenship_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""

def extract_spouse_nationality(text: str) -> str:
    spouse_nationality_pattern = re.compile(r'10. Ulutu/ Nationality:(.*?)\n', re.DOTALL)
    spouse_match = spouse_nationality_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""


def extract_spouse_marry_date(text:str) -> str:
    marriage_date_pattern = re.compile(r'marriage:(.*?)\n', re.DOTALL)
    spouse_match = marriage_date_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""


def extract_spouse_marry_place(text: str) -> str:
    place_of_marriage_pattern = re.compile(r'Kattalgan Jery/ Place of registration:(.*?)\n', re.DOTALL)
    spouse_match = place_of_marriage_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""

def extract_spouse_certificate_date(text: str) -> str:
    marriage_certificate_date_pattern = re.compile(r'Beryagen Kunu/ Issue Date:(.*?)\n', re.DOTALL)
    spouse_match = marriage_certificate_date_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""

def extract_registry_office_head_pattern(text: str) -> str:
    registry_office_head_pattern = re.compile(r'REGISTRY OFFICE:(.*?)\n', re.DOTALL)
    spouse_match = registry_office_head_pattern.search(text)
    if spouse_match:
        return spouse_match.group(1).strip()
    
    return ""
    


def extract_information(text: str) -> dict:
    information = {
        'ФИО': extract_name(text),
        'Дата рождения': extract_dob(text),
        'Место рождения': extract_place_of_birth(text),
        'Гражданство': extract_citizenship(text),
        "Супруга": extract_spouse_name(text),
        "Дата брака": extract_spouse_marry_date(text),
        "Место брака": extract_spouse_marry_place(text),
        "Глава отдела": extract_registry_office_head_pattern(text),

    }
    return information
