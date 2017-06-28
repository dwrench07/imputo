from fuzzywuzzy import fuzz
from fuzzywuzzy import process


fuzz.ratio("lName", "Last Name")

choices = ["First Name", "Last Name", "Full Name", "Company Name"]

process.extract("l_name", choices, limit=2)

process.extractOne("l_name", choices)

