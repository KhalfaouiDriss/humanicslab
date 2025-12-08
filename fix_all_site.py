import os
import re

def fix_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Remove visibility/animation classes that hide content
        # These classes are often added by JS for entrance animations but need to be removed for static viewing
        classes_to_remove = [
            r'opacity-0',
            r'translate-y-10',
            r'translate-x-10',
            r'-translate-x-10',
            r'scale-95',
            r'scale-0',
            r'rotate-90', # Sometimes used for mobile menu icons, might be risky, but let's see
            r'animate-fade-in' # Sets opacity: 0 initially
        ]
        
        for class_name in classes_to_remove:
            # Replace " class_name" with "" (space before)
            content = re.sub(r'\s+' + class_name, '', content)
            # Replace "class_name " with "" (space after)
            content = re.sub(class_name + r'\s+', '', content)
            # Replace "class_name" (at end of string or only class)
            content = re.sub(class_name, '', content)

        # 2. Remove the animate-pulse loading overlays
        # <div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 animate-pulse"></div>
        pulse_overlay_pattern = r'<div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 animate-pulse"></div>'
        content = re.sub(pulse_overlay_pattern, '', content)

        # 3. Fix inline styles for animations
        # Many elements have inline styles like style="opacity:0;transform:translateY(20px)"
        
        # Replace opacity:0 with opacity:1
        content = content.replace('opacity:0', 'opacity:1')
        
        # Remove transform translations and scales that hide content
        # transform:translateY(20px)
        content = re.sub(r'transform:translate[XY]\(-?\d+px\)', '', content)
        # transform:scale(0)
        content = re.sub(r'transform:scale\(0\)', '', content)
        
        # Clean up any double semicolons or empty styles resulting from removals
        content = content.replace('style=";"', '')
        content = content.replace(';;', ';')

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {file_path}")
        else:
            print(f"No changes needed for {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    # Walk through the current directory and all subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                fix_file(file_path)

if __name__ == "__main__":
    main()
