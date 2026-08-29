
import re

# Sample text
text = """
Hello everyone!

You can contact Omkar Solanke at:
omkar@gmail.com
omkar123@college.edu
support@example.org
invalid-email@com
omkar.solanke@domain.co.in

Thank you!
"""

# Regular expression pattern for email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all email addresses
emails = re.findall(email_pattern, text)

# Display results
print("Email addresses found:")

if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

# Display total number of emails
print("\nTotal emails found:", len(emails))