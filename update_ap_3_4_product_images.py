import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Product 4 (Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)): Replace with image/ap/3.png
    content = content.replace('src="image/shopping (3).webp" alt="Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)"', 'src="image/ap/3.png" alt="Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)"')
    content = content.replace('alt="Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)" src="image/shopping (3).webp"', 'alt="Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)" src="image/ap/3.png"')

    # Product 5 (Harpic Fresh Organic Active Citrus Toilet Cleaner): Replace with image/ap/4.png
    content = content.replace('src="image/shopping (4).webp" alt="Harpic Fresh Organic Active Citrus Toilet Cleaner"', 'src="image/ap/4.png" alt="Harpic Fresh Organic Active Citrus Toilet Cleaner"')
    content = content.replace('alt="Harpic Fresh Organic Active Citrus Toilet Cleaner" src="image/shopping (4).webp"', 'alt="Harpic Fresh Organic Active Citrus Toilet Cleaner" src="image/ap/4.png"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated Product 4 and Product 5 images to image/ap/3.png and image/ap/4.png across all HTML files.")
