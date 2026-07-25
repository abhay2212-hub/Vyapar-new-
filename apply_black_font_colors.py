import glob, re

# 1. Update post-1350.css
css_file = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/wp-content/uploads/elementor/css/post-1350.css'

with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
    css_content = f.read()

# Replace #FFFFFF color rules for elementor banner titles and buttons in CSS
css_content = re.sub(
    r'(\.elementor-element-(?:14c2608|9d0417c|5099ff3|1a84e99)\s+\.(?:razzi-banner-content__title|razzi-banner-content__button|razzi-banner-content__sub-title)\s*\{\s*color:\s*)#[fF]{3,6}(;)',
    r'\1#000000\2',
    css_content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated post-1350.css banner title/button font colors to #000000.")

# 2. Inject comprehensive black font style override into all HTML files
black_fonts_style = """<style id="custom-all-black-fonts">
/* Force black font color for text, titles, subtitles, links, headings, nav items, and banner content */
body, p, span, h1, h2, h3, h4, h5, h6, a, li, div, 
.razzi-banner-content__title, 
.razzi-banner-content__button, 
.razzi-banner-content__sub-title,
.banner-title, 
.banner-subtitle, 
.button-text, 
.woocommerce-loop-product__title, 
.product-title,
.entry-title, 
.widget-title,
.nav-menu a,
.main-navigation a,
.site-header a,
.footer-widgets a,
.testi-title,
.testi-desc {
    color: #000000 !important;
}

/* Keep text white on filled dark buttons & promotional banner for contrast */
.button.razzi-button, 
a.button.razzi-button,
button.button,
button.search-submit,
.category-filter-btn.active,
.campaign-bar .razzi-promotion,
.elementor-button,
.fkcart-checkout-btn {
    color: #ffffff !important;
}
.button.razzi-button *, 
a.button.razzi-button *,
.category-filter-btn.active * {
    color: #ffffff !important;
}

/* Ensure banner Shop Now links and underlines remain black */
.razzi-banner-content__button,
.razzi-banner-content__button *,
.button-underline,
.button-underline * {
    color: #000000 !important;
}
</style>"""

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'id="custom-all-black-fonts"' in content:
        content = re.sub(r'<style id="custom-all-black-fonts">.*?</style>', black_fonts_style, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', black_fonts_style + '\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected black fonts style override into all HTML files.")
