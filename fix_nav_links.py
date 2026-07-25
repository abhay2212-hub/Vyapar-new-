import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)
# Only process main page files, not JS-extra fragments
main_files = [f for f in html_files if any(f.endswith(x) for x in ['index.html', 'shop.html', 'shop-2.html'])]

# Navigation link replacements - map external URLs to local files
nav_replacements = {
    # Main navigation links
    'href="https://vasroventures.com/"': 'href="index.html"',
    'href="https://vasroventures.com"': 'href="index.html"',
    "href='https://vasroventures.com/'": "href='index.html'",
    "href='https://vasroventures.com'": "href='index.html'",
    
    # About Us
    'href="https://vasroventures.com/about-us/"': 'href="about-us.html"',
    "href='https://vasroventures.com/about-us/'": "href='about-us.html'",
    
    # Contact Us
    'href="https://vasroventures.com/contact-us/"': 'href="contact-us.html"',
    "href='https://vasroventures.com/contact-us/'": "href='contact-us.html'",
    
    # My Account
    'href="https://vasroventures.com/my-account/"': 'href="my-account.html"',
    "href='https://vasroventures.com/my-account/'": "href='my-account.html'",
    
    # Shop pages
    'href="https://vasroventures.com/product-hover-style/"': 'href="shop.html"',
    "href='https://vasroventures.com/product-hover-style/'": "href='shop.html'",
    'href="https://vasroventures.com/shop/"': 'href="shop.html"',
    "href='https://vasroventures.com/shop/'": "href='shop.html'",
    
    # Cart
    'href="https://vasroventures.com/cart/"': 'href="#"',
    "href='https://vasroventures.com/cart/'": "href='#'",
    
    # Wishlist
    'href="https://vasroventures.com/wishlist/"': 'href="#"',
    "href='https://vasroventures.com/wishlist/'": "href='#'",
    
    # Policy pages - point to contact for now
    'href="https://vasroventures.com/privacy-policy/"': 'href="contact-us.html"',
    'href="https://vasroventures.com/terms-and-conditions/"': 'href="contact-us.html"',
    'href="https://vasroventures.com/returns-and-refunds/"': 'href="contact-us.html"',
    'href="https://vasroventures.com/shipping-policy/"': 'href="contact-us.html"',
}

count = 0
for file_path in main_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    for old, new in nav_replacements.items():
        content = content.replace(old, new)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"  Fixed links in: {file_path}")

print(f"\nFixed navigation links in {count} HTML files.")
