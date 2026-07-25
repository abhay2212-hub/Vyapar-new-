import glob, re

ALLOWED_PRICES = {"200.00", "300.00", "500.00", "800.00", "1,000.00", "1,500.00", "2,000.00", "1000.00", "1500.00", "2000.00"}

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

unmatched_prices = set()

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all price amounts in HTML
    prices = re.findall(r'<span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">(?:[&#\d;₹]+|&#8377;)</span>([\d,.]+)</bdi></span>', content)
    for p in prices:
        if p not in ALLOWED_PRICES:
            unmatched_prices.add((file_path, p))

print("Verification Result:")
if unmatched_prices:
    print(f"Found {len(unmatched_prices)} unmatched prices:")
    for f, p in unmatched_prices:
        print(f"  File: {f} -> Price: {p}")
else:
    print("ALL product prices across all HTML files strictly belong to [200, 300, 500, 800, 1000, 1500, 2000]!")
