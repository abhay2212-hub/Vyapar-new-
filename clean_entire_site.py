import re, os, glob

base_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com'

# List of files to update
files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Replace Footer text
    content = content.replace(
        'stylish, affordable, and high-quality clothing for Men, Women. Discover the latest trends, timeless pieces',
        'powerful, high-quality Bathroom & Toilet Cleaners. Discover top-rated hygiene, stain removal, and disinfectant solutions'
    )
    content = content.replace(
        'clothing for Men, Women',
        'Bathroom & Toilet Cleaning Products'
    )

    # 2. Replace Review text
    content = content.replace(
        'These jeans fit true to size with stretch for comfort, ideal for daily wear in Indian climates. Some users note color fading after 10-15 washes, but the quality holds up better than budget alternatives. Perfect for casual office looks, priced around ₹2,000-3,000 on sale.',
        'This bathroom cleaner works exceptionally well on tough lime scale and hard water stains! Leaves tiles sparkling clean and smelling fresh.'
    )
    content = content.replace(
        'Slim Tapered Jeans',
        'urbanWipe Bathroom Cleaner 500ml'
    )

    # 3. Replace all external domain links
    content = re.sub(
        r'href=["\']https://vasroventures\.com/shop-2/\?wpf_filter_cat_0=84&amp;wpf_fbv=1["\']',
        'href="#shop-section" onclick="filterCleanerProducts(\'bathroom\', event)"',
        content
    )
    content = re.sub(
        r'href=["\']https://vasroventures\.com/shop-2/\?wpf_filter_cat_0=84&wpf_fbv=1["\']',
        'href="#shop-section" onclick="filterCleanerProducts(\'bathroom\', event)"',
        content
    )
    content = re.sub(
        r'href=["\']https://vasroventures\.com/shop-2/\?wpf_fbv=1&amp;wpf_filter_cat_0=62["\']',
        'href="#shop-section" onclick="filterCleanerProducts(\'toilet\', event)"',
        content
    )
    content = re.sub(
        r'href=["\']https://vasroventures\.com/shop-2/\?wpf_fbv=1&wpf_filter_cat_0=62["\']',
        'href="#shop-section" onclick="filterCleanerProducts(\'toilet\', event)"',
        content
    )

    # Catch-all for any vasroventures.com/shop-2 or shop links
    content = re.sub(r'href=["\']https://vasroventures\.com/shop-2/[^"\']*["\']', 'href="#shop-section"', content)
    content = re.sub(r'href=["\']https://vasroventures\.com/shop/[^"\']*["\']', 'href="#shop-section"', content)
    content = re.sub(r'href=["\']https://vasroventures\.com/shop[^"\']*["\']', 'href="#shop-section"', content)
    content = re.sub(r'href=["\']https://vasroventures\.com/["\']', 'href="index.html"', content)
    content = re.sub(r'href=["\']https://vasroventures\.com["\']', 'href="index.html"', content)

    # Replace category names in dropdowns / selects
    content = content.replace('<option class="level-0" value="mens">Mens</option>', '<option class="level-0" value="bathroom">Bathroom Cleaner</option>')
    content = content.replace('<option class="level-0" value="womens">Womens</option>', '<option class="level-0" value="toilet">Toilet Cleaner</option>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleaned all html files in vasroventures.com successfully!")
