import re, os

html_path = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all variations of vasroventures.com/shop and shop-2 links with #shop-section
html = re.sub(r'https://vasroventures\.com/shop-2/[^\s"]*', '#shop-section', html)
html = re.sub(r'https://vasroventures\.com/shop/[^\s"]*', '#shop-section', html)
html = re.sub(r'https://vasroventures\.com/shop[^\s"]*', '#shop-section', html)

# Replace testimonials with hygiene/cleaner product reviews
html = html.replace('Slim Tapered Jeans', 'urbanWipe Bathroom Cleaner')
html = html.replace('>Jeans<', '>Bathroom Cleaner<')
html = html.replace('Cotton print Dress', 'Harpic Power Plus 10X Toilet Cleaner')
html = html.replace('>Dresses <', '>Toilet Cleaner <')
html = html.replace('Oversized print T-shirt', 'Presto! Disinfectant Bathroom Cleaner')
html = html.replace('>T-shirts <', '>Bathroom Cleaner <')
html = html.replace('Slim Fit Shirt', 'Domex Disinfectant Toilet Cleaner')
html = html.replace('>Shirts <', '>Toilet Cleaner <')

# Replace deal carousel titles
html = html.replace('Get -50% From<br/> Summer Collection', 'Get -50% Off<br/> Bathroom Cleaners')
html = html.replace('Get -70% From<br/> Spring Collection', 'Get -70% Off<br/> Toilet Cleaners')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html all links & testimonials successfully.")

# Create shop/index.html and shop-2/index.html local routes so URL navigation works cleanly
shop_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/shop'
shop2_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/shop-2'

os.makedirs(shop_dir, exist_ok=True)
os.makedirs(shop2_dir, exist_ok=True)

redirect_html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=../index.html#shop-section" />
    <script>window.location.href = "../index.html#shop-section";</script>
</head>
<body>
    <p>Redirecting to <a href="../index.html#shop-section">Shop Cleaning Products</a>...</p>
</body>
</html>
"""

with open(os.path.join(shop_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(redirect_html)

with open(os.path.join(shop2_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(redirect_html)

with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/shop.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/shop-2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Created shop directories and local fallbacks successfully!")
