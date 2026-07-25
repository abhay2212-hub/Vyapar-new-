import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

srcset_pattern = re.compile(r'srcset="[^"]*https://vasroventures\.com/wp-content/uploads/[^"]*"')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = srcset_pattern.sub('srcset=""', content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Cleaned all old srcset attributes in HTML files.")
