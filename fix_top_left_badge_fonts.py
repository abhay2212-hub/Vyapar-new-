import glob, re

# Update global black fonts style block to explicitly keep .cleaner-badge font color white
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

/* Keep text white on filled dark buttons, top-left badges & promotional banners */
.button.razzi-button, 
a.button.razzi-button,
button.button,
button.search-submit,
.category-filter-btn.active,
.campaign-bar .razzi-promotion,
.elementor-button,
.fkcart-checkout-btn,
.cleaner-badge,
.cleaner-badge *,
.onsale,
.onsale * {
    color: #ffffff !important;
}
.button.razzi-button *, 
a.button.razzi-button *,
.category-filter-btn.active *,
.cleaner-badge,
.cleaner-badge * {
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

print("Updated top-left badge font colors to white in all HTML files.")
