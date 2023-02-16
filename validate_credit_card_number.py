import re

n = int(input())
for _ in range(n):
    cc_num = input().strip()
    # Regex pattern to match valid credit card numbers
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    # Check if the credit card number matches the pattern
    if re.match(pattern, cc_num) and not re.search(r'(\d)\1\1\1', cc_num.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')
