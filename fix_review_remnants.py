import glob, re

files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

replacements = {
    # Review subtitle category remnants
    '<span class="subtitle">Dress</span>': '<span class="subtitle">Bathroom Cleaner</span>',
    '<span class="subtitle">Men</span>': '<span class="subtitle">Toilet Cleaner</span>',
    '<span class="subtitle">Women</span>': '<span class="subtitle">Bathroom Cleaner</span>',
    "Women's": "Bathroom Cleaner",
    
    # Review title remnants
    'Trendy collection with good comfort.': 'Effective deep cleaning formula.',
    'Smooth online shopping experience.': 'Fast delivery, excellent results.',
    'Value for money cleaning essentials': 'Value for money cleaning essentials',
    
    # First review text with old clothing wording
    'ideal for daily wear in Indian climates. Some users note color fading after 10-15 washes, but the quality holds up better than budget alternatives. Perfect': 'ideal for daily bathroom hygiene. Removes hard water stains and limescale effortlessly. Quality holds up better than budget alternatives. Perfect',
}

count = 0
for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed clothing remnants in {count} HTML files.")
