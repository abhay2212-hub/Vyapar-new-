import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Replace right hero carousel banner image with image/ap/5.png
    content = content.replace('src="image/shopping (1).webp" class="attachment-full size-full wp-image-5837"', 'src="image/ap/5.png" class="attachment-full size-full wp-image-5837"')

    # 2. Replace "Vasro Ventures" and "Vasto ventures" with "Vyapar Vault"
    content = content.replace('<title>Vasro Ventures</title>', '<title>Vyapar Vault</title>')
    content = content.replace('<title>Vasro Ventures', '<title>Vyapar Vault')
    content = content.replace('Vasro Ventures', 'Vyapar Vault')
    content = content.replace('Vasto ventures', 'Vyapar Vault')
    content = content.replace('vasro ventures', 'Vyapar Vault')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated right hero banner image to image/ap/5.png and changed all title/text references to Vyapar Vault across all HTML files.")
