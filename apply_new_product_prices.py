import glob, re, random

# Allowed prices from user
ALLOWED_PRICES = [200, 300, 500, 800, 1000, 1500, 2000]

# Fix seed for reproducible random selection
random.seed(42)

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/**/*.html', recursive=True)

# Build a consistent mapping for all product titles
product_price_map = {}

def get_price_for_product(title):
    clean_title = ' '.join(title.split())
    if clean_title not in product_price_map:
        product_price_map[clean_title] = random.choice(ALLOWED_PRICES)
    return product_price_map[clean_title]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern for product items (cards)
    def replace_price_in_block(match):
        block = match.group(0)
        
        # Find title inside block
        title_match = re.search(r'<h[23][^>]*class="[^"]*woocommerce-loop-product__title[^"]*"[^>]*>(.*?)</h[23]>', block, re.DOTALL)
        if not title_match:
            title_match = re.search(r'alt="([^"]+)"', block)
            
        if title_match:
            raw_title = title_match.group(1)
            raw_title = re.sub(r'<[^>]+>', '', raw_title) # strip inner tags
            new_price = get_price_for_product(raw_title)
            
            # Format as decimal with comma if >= 1000 or plain
            price_str = f"{new_price:,.2f}" if new_price >= 1000 else f"{new_price}.00"
            
            # Replace single price or ins price
            block = re.sub(
                r'(<span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">(?:[&#\d;₹]+|&#8377;)</span>)([\d,.]+)(</bdi></span>)',
                rf'\g<1>{price_str}\g<3>',
                block
            )
        return block

    # Process cleaner-product-item and standard li.product blocks
    content = re.sub(r'<li[^>]*class="[^"]*product[^"]*"[^>]*>.*?</li>', replace_price_in_block, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Product Price Mapping:")
for title, price in sorted(product_price_map.items()):
    print(f"  - {title}: Rs. {price}.00")

print("\nUpdated all product prices across all HTML files successfully.")
