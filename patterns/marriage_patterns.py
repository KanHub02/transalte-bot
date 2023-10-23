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


def extract_information(text: str) -> dict:
    information = {
        'ФИО': extract_name(text),
        'Дата рождения': extract_dob(text),
        'Место рождения': extract_place_of_birth(text),
        'Гражданство': extract_citizenship(text),
    }
    return information

text = """ваш текст с данными о браке"""

info = extract_information(text)
print(info)
