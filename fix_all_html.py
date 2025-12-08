import re
import os
import glob

# Find all HTML files in the current directory and subdirectories
html_files = glob.glob('**/*.html', recursive=True)

def remove_opacity_0(match):
    class_attr = match.group(1)
    if 'invisible' in class_attr or 'pointer-events-none' in class_attr:
        return f'class="{class_attr}"'
    
    # Remove opacity-0
    new_class_attr = class_attr.replace('opacity-0', '').strip()
    # Clean up double spaces
    new_class_attr = re.sub(r'\s+', ' ', new_class_attr)
    return f'class="{new_class_attr}"'

for file_path in html_files:
    print(f"Processing {file_path}...")
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Remove animate-spin divs
    # This regex removes the div containing animate-spin. 
    # Note: This assumes the div is self-contained or empty like <div ...></div> which was the case for the loaders.
    # If animate-spin is on a container with content, this might be dangerous if it matches too much.
    # The loaders seen so far were: <div ... animate-spin ...></div>
    # So I'll use a regex that matches <div ... animate-spin ...></div>
    
    content = re.sub(r'<div[^>]*animate-spin[^>]*></div>', '', content)

    # 2. Remove opacity-0 from visible elements
    content = re.sub(r'class="([^"]*)"', remove_opacity_0, content)

    with open(file_path, 'w') as f:
        f.write(content)

print("Fixed all HTML files.")
