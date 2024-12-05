import re

# Sample variable containing multiple strings
variable = """
NAME="Amazon Linux"
VERSION="2023"
ID="amzn"
ID_LIKE="fedora"
VERSION_ID="2023"
PLATFORM_ID="platform:al2023"
PRETTY_NAME="Amazon Linux 2023"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2023"
HOME_URL="https://aws.amazon.com/linux/"
BUG_REPORT_URL="https://github.com/amazonlinux/amazon-linux-2023"
SUPPORT_END="2028-03-15"
"""

# Define regex pattern to match "Amazon Linux 2023" or "Amazon Linux 2"
pattern_2023 = re.compile(r'Amazon Linux 2023')
pattern_2 = re.compile(r'Amazon Linux 2')

# Check if pattern is found in the variable
if pattern_2.search(variable):
    print("Variable contains 'Amazon Linux 2'. Returning 2.")
    result = 2
elif pattern_2023.search(variable):
    print("Variable contains 'Amazon Linux 2023'. Returning 1.")
    result = 1
else:
    print("Variable does not contain 'Amazon Linux 2023' or 'Amazon Linux 2'.")
    result = None

print("Result:", result)
