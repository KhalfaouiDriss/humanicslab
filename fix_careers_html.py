
import re

file_path = 'careers.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove translate classes that might hide content
content = re.sub(r'\btranslate-y-10\b', '', content)
content = re.sub(r'\btranslate-y-4\b', '', content)
content = re.sub(r'\btranslate-x-10\b', '', content)
content = re.sub(r'\b-translate-x-10\b', '', content)
content = re.sub(r'\bscale-95\b', '', content)

# Remove opacity-0 if it's not part of the dropdown (which has invisible)
# The dropdown has "opacity-0 invisible". We want to keep that.
# But other opacity-0 might be for entry animations.
# My previous global script removed opacity-0 generally.
# Let's check if there are any opacity-0 left that are NOT invisible.
# But for now, removing translate classes is the main thing for "content shifted/hidden".

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {file_path}")
