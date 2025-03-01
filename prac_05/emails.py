"""
Emails
Estimate: 15 minutes
Actual: 15 minutes
"""
ACCEPT_PROMPT = ["Y", ""]
email_to_name = {}

email = input("Email: ").strip()
while email != "":
    name = " ".join(email.split("@")[0].split(".")).title() # Extract the name from the email address
    check_prompt = input(f"Is your name {name}? (Y/n) ").upper().strip()
    if check_prompt not in ACCEPT_PROMPT:
        name = input("Name: ").strip().title()
    email_to_name[email] = name
    email = input("Email: ").strip()
print()

for email, name in email_to_name.items():
    print(f"{name} ({email})")
