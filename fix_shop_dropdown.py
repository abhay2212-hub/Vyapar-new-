import glob

# Fix Shop dropdown links on about-us, contact-us, and my-account pages
# These pages don't have #shop-section or filterCleanerProducts() function
pages_to_fix = [
    'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/about-us.html',
    'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/contact-us.html',
    'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/my-account.html',
]

for file_path in pages_to_fix:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace Shop dropdown links - point to shop.html instead of #shop-section
    # Main Shop link
    content = content.replace(
        '<a href="#shop-section">Shop <span style="font-size: 10px; margin-left: 3px;">▼</span></a>',
        '<a href="shop.html">Shop <span style="font-size: 10px; margin-left: 3px;">▼</span></a>'
    )
    
    # Sub-menu items - remove onclick and point to shop.html
    content = content.replace(
        '<a href="#shop-section" onclick="filterCleanerProducts(\'all\', event)">All Products</a>',
        '<a href="shop.html">All Products</a>'
    )
    content = content.replace(
        '<a href="#shop-section" onclick="filterCleanerProducts(\'bathroom\', event)">Bathroom Cleaner</a>',
        '<a href="shop.html#shop-section">Bathroom Cleaner</a>'
    )
    content = content.replace(
        '<a href="#shop-section" onclick="filterCleanerProducts(\'toilet\', event)">Toilet Cleaner</a>',
        '<a href="shop.html#shop-section">Toilet Cleaner</a>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Fixed: {file_path.split('/')[-1]}")

print("\nAll non-homepage Shop dropdown links fixed!")
