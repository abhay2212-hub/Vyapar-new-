import os, shutil, glob, re

source_logo = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/image/logo.png'
dest_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/image'
dest_logo = os.path.join(dest_dir, 'logo.png')

os.makedirs(dest_dir, exist_ok=True)
shutil.copy(source_logo, dest_logo)

print("Copied logo.png to vasroventures.com/image/logo.png successfully.")

html_files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

logo_css_snippet = """
<style id="custom-logo-preloader-styles">
.preloader-icon img {
    max-width: 130px !important;
    max-height: 130px !important;
    object-fit: contain !important;
    animation: preloader-pulse 1.5s infinite ease-in-out !important;
}
@keyframes preloader-pulse {
    0% { transform: scale(0.95); opacity: 0.85; }
    50% { transform: scale(1.08); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.85; }
}
.site-branding .logo img,
.mobile-logo .logo img {
    max-height: 55px !important;
    width: auto !important;
    object-fit: contain !important;
}
</style>
"""

old_logo_pattern = r'https://vasroventures\.com/wp-content/uploads/2025/11/Untitled-design-23[^\s"\']*'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace old logo URLs with image/logo.png
    content = re.sub(old_logo_pattern, 'image/logo.png', content)

    # Inject logo preloader CSS into head if not already present
    if 'custom-logo-preloader-styles' not in content:
        content = content.replace('</head>', logo_css_snippet + '\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all HTML files with new logo and preloader animation!")
