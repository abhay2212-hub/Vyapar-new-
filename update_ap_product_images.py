import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace image for Everyday Ultra Clean Toilet Cleaner 1L with image/ap/1.png
    content = re.sub(
        r'(<img\s+[^>]*src=["\'])image/shopping\s*\(1\)\.webp(["\'][^>]*alt=["\']Everyday Ultra Clean Toilet Cleaner 1L["\'])',
        r'\1image/ap/1.png\2',
        content
    )
    content = re.sub(
        r'(<img\s+[^>]*alt=["\']Everyday Ultra Clean Toilet Cleaner 1L["\'][^>]*src=["\'])image/shopping\s*\(1\)\.webp(["\'])',
        r'\1image/ap/1.png\2',
        content
    )

    # Replace image for Harpic Power Plus 10X Total Clean Toilet Cleaner with image/ap/2.png
    content = re.sub(
        r'(<img\s+[^>]*src=["\'])image/shopping\s*\(2\)\.webp(["\'][^>]*alt=["\']Harpic Power Plus 10X Total Clean Toilet Cleaner["\'])',
        r'\1image/ap/2.png\2',
        content
    )
    content = re.sub(
        r'(<img\s+[^>]*alt=["\']Harpic Power Plus 10X Total Clean Toilet Cleaner["\'][^>]*src=["\'])image/shopping\s*\(2\)\.webp(["\'])',
        r'\1image/ap/2.png\2',
        content
    )

    # General replacement for the product grid item images 2 and 3 if explicit alt match didn't trigger
    # Product 2 (Everyday Ultra Clean Toilet Cleaner 1L):
    content = content.replace('src="image/shopping (1).webp" alt="Everyday Ultra Clean Toilet Cleaner 1L"', 'src="image/ap/1.png" alt="Everyday Ultra Clean Toilet Cleaner 1L"')
    content = content.replace('alt="Everyday Ultra Clean Toilet Cleaner 1L" src="image/shopping (1).webp"', 'alt="Everyday Ultra Clean Toilet Cleaner 1L" src="image/ap/1.png"')

    # Product 3 (Harpic Power Plus 10X Total Clean Toilet Cleaner):
    content = content.replace('src="image/shopping (2).webp" alt="Harpic Power Plus 10X Total Clean Toilet Cleaner"', 'src="image/ap/2.png" alt="Harpic Power Plus 10X Total Clean Toilet Cleaner"')
    content = content.replace('alt="Harpic Power Plus 10X Total Clean Toilet Cleaner" src="image/shopping (2).webp"', 'alt="Harpic Power Plus 10X Total Clean Toilet Cleaner" src="image/ap/2.png"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated product 2 and product 3 images to image/ap/1.png and image/ap/2.png across all HTML files.")
