import re

text = input("Enter the text: ")

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

file = open("emails.txt", "w")

if emails:
    print("\nEmail Addresses Found:\n")
    for email in emails:
        print(email)
        file.write(email + "\n")
else:
    print("No email addresses found.")
    file.write("No email addresses found.")

file.close()
print("\nEmails saved in emails.txt")