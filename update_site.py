import re

html_path = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

products = [
    {
        "id": 1,
        "title": "urbanWipe Bathroom Cleaner 500ml",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹299.00",
        "image": "image/shopping.webp",
        "badge": "Popular"
    },
    {
        "id": 2,
        "title": "Everyday Ultra Clean Toilet Cleaner 1L",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹199.00",
        "image": "image/shopping (1).webp",
        "badge": "Best Seller"
    },
    {
        "id": 3,
        "title": "Harpic Power Plus 10X Total Clean Toilet Cleaner",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹249.00",
        "image": "image/shopping (2).webp",
        "badge": "10X Power"
    },
    {
        "id": 4,
        "title": "Presto! Disinfectant Bathroom Cleaner Lemon (Pack of 2)",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹399.00",
        "image": "image/shopping (3).webp",
        "badge": "Value Pack"
    },
    {
        "id": 5,
        "title": "Harpic Fresh Organic Active Citrus Toilet Cleaner",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹229.00",
        "image": "image/shopping (4).webp",
        "badge": "Organic Active"
    },
    {
        "id": 6,
        "title": "Presto! Disinfectant Toilet Cleaner 5L Can",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹599.00",
        "image": "image/shopping (5).webp",
        "badge": "5 Litre Jumbo"
    },
    {
        "id": 7,
        "title": "Harpic Hygienic Toilet Rim Block Lavender",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹149.00",
        "image": "image/shopping (6).webp",
        "badge": "Fresh Fragrance"
    },
    {
        "id": 8,
        "title": "Godrej Spic Toilet Cleaner Shiny & Stain-Free",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹189.00",
        "image": "image/shopping (7).webp",
        "badge": "Stain Block"
    },
    {
        "id": 9,
        "title": "Harpic Disinfectant Bathroom Cleaner Lemon",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹219.00",
        "image": "image/shopping (8).webp",
        "badge": "Lemon Fresh"
    },
    {
        "id": 10,
        "title": "Harpic Bathroom Ultra 10X Tough Stain Remover",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹279.00",
        "image": "image/shopping (9).webp",
        "badge": "Tough Stain"
    },
    {
        "id": 11,
        "title": "Klenzmo Tile & Bathroom Cleaner + Tap Cleaner Combo",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹499.00",
        "image": "image/shopping (10).webp",
        "badge": "Combo Pack"
    },
    {
        "id": 12,
        "title": "Harpic Germ & Stain Blaster Toilet Cleaner Floral",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹239.00",
        "image": "image/shopping (11).webp",
        "badge": "Germ Blaster"
    },
    {
        "id": 13,
        "title": "Domex Disinfectant Toilet Expert Cleaner",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹199.00",
        "image": "image/shopping (12).webp",
        "badge": "Expert Clean"
    },
    {
        "id": 14,
        "title": "Harpic Power Plus 10X Toilet Cleaner Sparkling Lemon",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹249.00",
        "image": "image/shopping (13).webp",
        "badge": "Sparkling Lemon"
    },
    {
        "id": 15,
        "title": "Lizol Fresh & Clean Bathroom Cleaner Pine Forest",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹259.00",
        "image": "image/shopping (14).webp",
        "badge": "Pine Forest"
    },
    {
        "id": 16,
        "title": "Lizol Fresh & Clean Bathroom Cleaner Floral",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹259.00",
        "image": "image/shopping (15).webp",
        "badge": "12hr Fragrance"
    },
    {
        "id": 17,
        "title": "Harpic White & Shine Bleach Toilet Cleaner",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹269.00",
        "image": "image/shopping (16).webp",
        "badge": "White & Shine"
    },
    {
        "id": 18,
        "title": "Lizol Bathroom Cleaner Pine Forest 1L",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹329.00",
        "image": "image/shopping (17).webp",
        "badge": "1 Litre"
    },
    {
        "id": 19,
        "title": "Born Good Industrial Grade Toilet Bowl Cleaner 5L",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹699.00",
        "image": "image/shopping (18).webp",
        "badge": "Eco Industrial"
    },
    {
        "id": 20,
        "title": "Vooki Bathroom Spray & Toilet Bowl Cleaner Combo",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹449.00",
        "image": "image/shopping (19).webp",
        "badge": "Spray & Wipe"
    },
    {
        "id": 21,
        "title": "Vooki Toilet Bowl & Bathroom Surface Cleaner Pack",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹549.00",
        "image": "image/shopping (20).webp",
        "badge": "Triple Pack"
    },
    {
        "id": 22,
        "title": "Ecover Triple Action Eco Toilet Cleaner Pine Fresh",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹349.00",
        "image": "image/shopping (21).webp",
        "badge": "Eco Friendly"
    },
    {
        "id": 23,
        "title": "Vooki Stain Resistant Toilet Bowl Cleaner (Pack of 2)",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹419.00",
        "image": "image/shopping (22).webp",
        "badge": "100 Flush Guard"
    },
    {
        "id": 24,
        "title": "DOT Extra Power Ceramic & Toilet Cleaner",
        "category": "bathroom",
        "category_label": "Bathroom Cleaner",
        "price": "₹179.00",
        "image": "image/shopping (23).webp",
        "badge": "Ceramic Shine"
    },
    {
        "id": 25,
        "title": "Harpic Power Plus Max 10 Actions Toilet Cleaner",
        "category": "toilet",
        "category_label": "Toilet Cleaner",
        "price": "₹259.00",
        "image": "image/shopping (24).webp",
        "badge": "Max 10 Action"
    }
]

# 1. Add Custom CSS and JS into <head>
custom_head_code = """
<style id="custom-cleaner-styles">
/* Custom Dropdown Styling for Navbar */
.main-navigation .menu-item-has-children {
    position: relative !important;
}
.main-navigation .menu-item-has-children:hover > .sub-menu,
.main-navigation .menu-item-has-children:focus-within > .sub-menu {
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: translateY(0) !important;
}
.main-navigation .sub-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background: #ffffff;
    min-width: 220px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    border-radius: 8px;
    padding: 10px 0;
    margin: 0;
    list-style: none;
    z-index: 9999;
    transition: all 0.2s ease-in-out;
}
.main-navigation .sub-menu li {
    padding: 0;
    margin: 0;
    border-bottom: 1px solid #f2f2f2;
}
.main-navigation .sub-menu li:last-child {
    border-bottom: none;
}
.main-navigation .sub-menu li a {
    display: block;
    padding: 10px 20px;
    color: #1f1f1f;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    transition: background 0.2s, color 0.2s;
}
.main-navigation .sub-menu li a:hover {
    background: #f8f9fa;
    color: #0066cc;
}

/* Category Filter Buttons */
.cleaner-filter-container {
    text-align: center;
    margin: 25px 0 35px 0;
}
.cleaner-filter-tabs {
    display: inline-flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    background: #f8f9fa;
    padding: 6px;
    border-radius: 40px;
    border: 1px solid #e9ecef;
}
.cleaner-filter-btn {
    background: transparent;
    border: none;
    padding: 10px 26px;
    border-radius: 30px;
    font-size: 15px;
    font-weight: 600;
    color: #495057;
    cursor: pointer;
    transition: all 0.3s ease;
}
.cleaner-filter-btn:hover {
    color: #1f1f1f;
}
.cleaner-filter-btn.active {
    background: #1f1f1f;
    color: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Product Card Improvements */
.cleaner-product-item {
    transition: transform 0.3s ease;
}
.cleaner-product-item:hover {
    transform: translateY(-4px);
}
.cleaner-img-box {
    position: relative;
    background: #ffffff;
    border-radius: 12px;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    height: 320px;
    border: 1px solid #eef2f5;
}
.cleaner-img-box img {
    max-height: 100%;
    max-width: 100%;
    object-fit: contain;
    transition: transform 0.4s ease;
}
.cleaner-product-item:hover .cleaner-img-box img {
    transform: scale(1.06);
}
.cleaner-badge {
    position: absolute;
    top: 12px;
    left: 12px;
    background: #1f1f1f;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    z-index: 2;
}
.cleaner-cat-badge {
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 12px;
    margin-bottom: 4px;
}
.cleaner-cat-bathroom {
    color: #0288d1;
}
.cleaner-cat-toilet {
    color: #7b1fa2;
}
</style>

<script>
function filterCleanerProducts(category, event) {
    if (event) event.preventDefault();
    
    var buttons = document.querySelectorAll('.cleaner-filter-btn');
    buttons.forEach(function(btn) {
        btn.classList.remove('active');
        if (btn.getAttribute('data-filter') === category) {
            btn.classList.add('active');
        }
    });

    var items = document.querySelectorAll('.cleaner-product-item');
    items.forEach(function(item) {
        if (category === 'all' || item.getAttribute('data-category') === category) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });

    var shopSec = document.getElementById('shop-section');
    if (shopSec) {
        shopSec.scrollIntoView({ behavior: 'smooth' });
    }
}
</script>
"""

html = html.replace('</head>', custom_head_code + '\n</head>')

# 2. Update Primary Navbar Menu
navbar_old = """<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-13801"><a href="https://vasroventures.com/shop-2/">Shop</a></li>"""

navbar_new = """<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-13801">
    <a href="#shop-section">Shop <span style="font-size: 10px; margin-left: 3px;">▼</span></a>
    <ul class="sub-menu">
        <li class="menu-item"><a href="#shop-section" onclick="filterCleanerProducts('all', event)">All Products</a></li>
        <li class="menu-item"><a href="#shop-section" onclick="filterCleanerProducts('bathroom', event)">Bathroom Cleaner</a></li>
        <li class="menu-item"><a href="#shop-section" onclick="filterCleanerProducts('toilet', event)">Toilet Cleaner</a></li>
    </ul>
</li>"""

html = html.replace(navbar_old, navbar_new)

# 3. Update Hero Banners (Women's / Men's -> Bathroom Cleaner / Toilet Cleaner)
html = html.replace('<h2 class="banner-title">Women\'s</h2>', '<h2 class="banner-title">Bathroom Cleaner</h2>')
html = html.replace('Shop Women\'s', 'Shop Bathroom Cleaners')
html = html.replace('https://vasroventures.com/wp-content/uploads/2021/09/home1-banner-carousels-1.jpg', 'image/shopping.webp')

html = html.replace('<h2 class="banner-title">Men\'s</h2>', '<h2 class="banner-title">Toilet Cleaner</h2>')
html = html.replace('Shop Men\'s', 'Shop Toilet Cleaners')
html = html.replace('https://vasroventures.com/wp-content/uploads/2020/12/home1-banner-carousels-2.jpg', 'image/shopping (1).webp')

# 4. Update Sub-category banners
html = html.replace('Men\'s Jacket Collection', 'Disinfectant Bathroom Cleaner')
html = html.replace('Men’s Shirts', 'Power Toilet Cleaner')
html = html.replace('Women’s Tops', 'Bathroom Stain Remover')
html = html.replace('Women\'s Jeans Collection', 'Eco-Friendly Toilet Cleaner')

# 5. Update Section Heading & Add Filter Tabs
heading_old = '<h3 class="razzi-heading-title"> Top Month Sellers</h3>'
heading_new = """<div id="shop-section">
    <h3 class="razzi-heading-title">Our Premium Cleaning Products</h3>
    <p style="text-align:center; color:#6c757d; margin-top:5px;">Powerful Hygiene & Deep Stain Removal Solutions</p>
    <div class="cleaner-filter-container">
        <div class="cleaner-filter-tabs">
            <button class="cleaner-filter-btn active" data-filter="all" onclick="filterCleanerProducts('all', event)">All Cleaning Products</button>
            <button class="cleaner-filter-btn" data-filter="bathroom" onclick="filterCleanerProducts('bathroom', event)">Bathroom Cleaner</button>
            <button class="cleaner-filter-btn" data-filter="toilet" onclick="filterCleanerProducts('toilet', event)">Toilet Cleaner</button>
        </div>
    </div>
</div>"""

html = html.replace(heading_old, heading_new)

# 6. Build HTML for 25 Products
products_html_list = []
for p in products:
    cat_class = "cleaner-cat-bathroom" if p["category"] == "bathroom" else "cleaner-cat-toilet"
    item_html = f"""
    <li class="cleaner-product-item post-{1000 + p['id']} product instock shipping-taxable purchasable" data-category="{p['category']}" style="margin-bottom: 30px;">
        <div class="premium-woo-product-wrapper">
            <div class="cleaner-img-box">
                <span class="cleaner-badge">{p['badge']}</span>
                <a href="#shop-section" onclick="filterCleanerProducts('{p['category']}', event)">
                    <img src="{p['image']}" alt="{p['title']}">
                </a>
            </div>
            <div class="premium-woo-products-details-wrap" style="padding-top: 15px; text-align: center;">
                <span class="cleaner-cat-badge {cat_class}">{p['category_label']}</span>
                <a href="#shop-section" class="premium-woo-product__link">
                    <h2 class="woocommerce-loop-product__title" style="font-size: 16px; font-weight: 600; line-height: 1.4; height: 44px; overflow: hidden; margin-top: 5px; color: #1f1f1f;">{p['title']}</h2>
                </a>
                <div style="margin: 8px 0; color: #ffb400; font-size: 14px;">
                    ★★★★★ <span style="color: #888; font-size: 12px;">(5.0)</span>
                </div>
                <span class="price" style="font-size: 18px; font-weight: 700; color: #1f1f1f;">
                    <span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">₹</span>{p['price'].replace('₹','')}</bdi></span>
                </span>
                <div style="margin-top: 12px;">
                    <a href="#shop-section" onclick="addToVyaparCart(event, '{p['title']}', '{p['price']}', '{p['image']}'); return false;" class="button razzi-button" style="padding: 8px 20px; font-size: 13px; border-radius: 4px; background: #1f1f1f; color: #fff; text-decoration: none; display: inline-block;">Add to Cart</a>
                </div>
            </div>
        </div>
    </li>"""
    products_html_list.append(item_html)

all_products_html = '\n'.join(products_html_list)

# Replace the product grid UL list
# Find start of products UL and end of products UL
grid_pattern = re.compile(r'<ul class="products product-loop-layout-1.*?</ul>', re.DOTALL)

replacement_ul = f"""<ul class="products product-loop-layout-1 columns-3 mobile-pl-col-3 mobile-pp-col-2 mobile-show-atc mobile-show-featured-icons">
{all_products_html}
</ul>"""

html = grid_pattern.sub(replacement_ul, html)

# 7. Update Search Modal Categories
search_cat_old = """<option value='0' selected='selected'>All Categories</option>
                                <option class="level-0" value="mens">Mens</option>
                                <option class="level-1" value="hoodies">&nbsp;&nbsp;&nbsp;Hoodies</option>
                                <option class="level-1" value="jackets-mens">&nbsp;&nbsp;&nbsp;Jackets</option>
                                <option class="level-1" value="jeans-mens">&nbsp;&nbsp;&nbsp;Jeans</option>
                                <option class="level-1" value="pants-mens">&nbsp;&nbsp;&nbsp;Pants</option>
                                <option class="level-1" value="shirts">&nbsp;&nbsp;&nbsp;Shirts</option>
                                <option class="level-1" value="shorts">&nbsp;&nbsp;&nbsp;Shorts</option>
                                <option class="level-1" value="t-shirts-mens">&nbsp;&nbsp;&nbsp;T-Shirts</option>
                                <option class="level-0" value="womens">Womens</option>
                                <option class="level-1" value="dresses">&nbsp;&nbsp;&nbsp;Dresses</option>
                                <option class="level-1" value="dupatta">&nbsp;&nbsp;&nbsp;Dupatta</option>
                                <option class="level-1" value="jackets">&nbsp;&nbsp;&nbsp;Jackets</option>
                                <option class="level-1" value="jeans">&nbsp;&nbsp;&nbsp;Jeans</option>
                                <option class="level-1" value="pants">&nbsp;&nbsp;&nbsp;Pants</option>
                                <option class="level-1" value="sarees">&nbsp;&nbsp;&nbsp;Sarees</option>
                                <option class="level-1" value="shirts-womens">&nbsp;&nbsp;&nbsp;Shirts</option>
                                <option class="level-1" value="shorts-womens">&nbsp;&nbsp;&nbsp;Shorts</option>
                                <option class="level-1" value="skirts">&nbsp;&nbsp;&nbsp;Skirts</option>
                                <option class="level-1" value="t-shirts">&nbsp;&nbsp;&nbsp;T-Shirts</option>
                                <option class="level-1" value="tops">&nbsp;&nbsp;&nbsp;Tops</option>"""

search_cat_new = """<option value='0' selected='selected'>All Categories</option>
                                <option class="level-0" value="bathroom">Bathroom Cleaner</option>
                                <option class="level-0" value="toilet">Toilet Cleaner</option>"""

html = html.replace(search_cat_old, search_cat_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully updated index.html with 25 cleaner products, dropdown navbar, and interactive tab filtering!')
