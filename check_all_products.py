import glob, re

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

products = set()

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find product titles inside h2 or h3 with class woocommerce-loop-product__title
    titles = re.findall(r'<h[23][^>]*class="[^"]*woocommerce-loop-product__title[^"]*"[^>]*>([^<]+)</h[23]>', content)
    for t in titles:
        t_clean = t.strip()
        if t_clean:
            products.add(t_clean)

print(f"Found {len(products)} unique products:")
for p in sorted(products):
    print("-", p)
