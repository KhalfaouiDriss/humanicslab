import re

file_path = 'who-we-are.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Remove animate-spin divs
# Pattern to find divs with animate-spin and remove the whole div or just the class?
# In index.html I removed the whole div if it was just a loader.
# Let's look at the context in who-we-are.html:
# <div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 animate-pulse"><div class="w-10 h-10 border-4 border-primary border-t-transparent rounded-full animate-spin"></div></div>
# It seems to be a loader overlay.
# I will remove the inner div with animate-spin.

content = re.sub(r'<div[^>]*animate-spin[^>]*></div>', '', content)

# 2. Remove opacity-0 from visible elements
# We want to remove 'opacity-0' from class lists UNLESS the class list also contains 'invisible' or 'pointer-events-none'.

def remove_opacity_0(match):
    class_attr = match.group(1)
    if 'invisible' in class_attr or 'pointer-events-none' in class_attr:
        return f'class="{class_attr}"'
    
    # Remove opacity-0
    new_class_attr = class_attr.replace('opacity-0', '').strip()
    # Clean up double spaces
    new_class_attr = re.sub(r'\s+', ' ', new_class_attr)
    return f'class="{new_class_attr}"'

content = re.sub(r'class="([^"]*)"', remove_opacity_0, content)

with open(file_path, 'w') as f:
    f.write(content)

print("Fixed who-we-are.html")
