import os
import re

root_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com'

def update_product_onclicks(file_name):
    file_path = os.path.join(root_dir, file_name)
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern matching a cleaner product item li card
    item_pattern = re.compile(
        r'(<li class="cleaner-product-item.*?'
        r'<img src="([^"]+)".*?'
        r'<h2 class="woocommerce-loop-product__title"[^>]*>([^<]+)</h2>.*?'
        r'<span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">₹</span>([^<]+)</bdi></span>.*?'
        r'<a href="#shop-section"[^>]*>)(Add to Cart|Add\s+to\s+Cart)(</a>)',
        re.DOTALL
    )

    def replace_item(m):
        full_prefix = m.group(1)
        img_src = m.group(2)
        title = m.group(3).strip()
        price_num = m.group(4).strip()
        btn_text = m.group(5)
        btn_close = m.group(6)

        price_str = f"₹{price_num}"
        safe_title = title.replace("'", "\\'")

        # Replace existing onclick in full_prefix if any, or inject new onclick
        if 'onclick="' in full_prefix:
            prefix_replaced = re.sub(
                r'onclick="[^"]*"',
                f'onclick="addToVyaparCart(event, \'{safe_title}\', \'{price_str}\', \'{img_src}\'); return false;"',
                full_prefix
            )
        else:
            prefix_replaced = full_prefix.replace(
                'class="button razzi-button"',
                f'onclick="addToVyaparCart(event, \'{safe_title}\', \'{price_str}\', \'{img_src}\'); return false;" class="button razzi-button"'
            )

        return f"{prefix_replaced}{btn_text}{btn_close}"

    updated_content = item_pattern.sub(replace_item, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated product price & image bindings in {file_name}")

for fn in ['index.html', 'shop.html', 'shop-2.html']:
    update_product_onclicks(fn)

print("Exact price and image matching updated!")
