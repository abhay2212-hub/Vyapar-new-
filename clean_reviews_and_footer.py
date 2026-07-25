import glob

files = glob.glob('c:/Users/hp/OneDrive/Desktop/vasroventures.com/vasroventures.com/**/*.html', recursive=True)

for file_path in files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    content = content.replace('Value for money fashion brand', 'Value for money cleaning essentials')
    content = content.replace('online clothing stores, pricing is competitive while maintaining solid fabric quality', 'online hygiene stores, pricing is competitive while maintaining exceptional cleaning power')
    content = content.replace('Impressive women’s wear designs', 'Impressive disinfectant & stain removal range')
    content = content.replace('fashion brand', 'hygiene brand')
    content = content.replace('women’s wear', 'bathroom & toilet cleaning')
    content = content.replace('casual office looks', 'bathroom and tile cleaning')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated review texts across all HTML files successfully.")
