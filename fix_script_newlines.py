file_path = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/contact-us.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

correct_js_body = """            var emailBody = "Customer Name: " + name + "\\n" +
                            "Customer Email: " + email + "\\n" +
                            "Category: " + subjectCategory + "\\n\\n" +
                            "Message:\\n" + message;"""

# Replace any broken newline version in contact-us.html
broken_pattern = r'var emailBody = "Customer Name: " \+ name \+ "\s*\n\s*" \+\s*\n\s*"Customer Email: " \+ email \+ "\s*\n\s*" \+\s*\n\s*"Category: " \+ subjectCategory \+ "\s*\n\s*\n\s*" \+\s*\n\s*"Message:\s*\n\s*" \+ message;'

import re
content = re.sub(broken_pattern, correct_js_body, content, flags=re.MULTILINE)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed JavaScript multiline string formatting in contact-us.html")
