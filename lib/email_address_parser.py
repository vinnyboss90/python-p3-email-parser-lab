# your code goes here!
import re

class EmailAddressParser:
    
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        matches = pattern.findall(self.email_addresses)
        return sorted(matches)