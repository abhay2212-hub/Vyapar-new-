import glob

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Product "Domex Disinfectant Toilet Expert Cleaner": Replace image with image/ap/6.png
    content = content.replace('src="image/shopping (12).webp" alt="Domex Disinfectant Toilet Expert Cleaner"', 'src="image/ap/6.png" alt="Domex Disinfectant Toilet Expert Cleaner"')
    content = content.replace('alt="Domex Disinfectant Toilet Expert Cleaner" src="image/shopping (12).webp"', 'alt="Domex Disinfectant Toilet Expert Cleaner" src="image/ap/6.png"')

    # Product "Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon": Replace image with image/ap/7.png
    content = content.replace('src="image/shopping (13).webp" alt="Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon"', 'src="image/ap/7.png" alt="Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon"')
    content = content.replace('alt="Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon" src="image/shopping (13).webp"', 'alt="Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon" src="image/ap/7.png"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated Domex Disinfectant Toilet Expert Cleaner to image/ap/6.png and Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon to image/ap/7.png across all HTML files.")
