import re
import sys

def fix_html_classes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove translate-y-10
        content = re.sub(r'translate-y-10', '', content)
        # Remove translate-x-10
        content = re.sub(r'translate-x-10', '', content)
        # Remove -translate-x-10
        content = re.sub(r'-translate-x-10', '', content)
        # Remove scale-95
        content = re.sub(r'scale-95', '', content)
        # Remove opacity-0
        content = re.sub(r'opacity-0', '', content)
        
        # Also remove the transition classes that might cause issues if they are waiting for a trigger
        # content = re.sub(r'transition-all duration-1000', '', content) 
        # content = re.sub(r'transition-all duration-700', '', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully processed {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_html_classes.py <file_path>")
    else:
        fix_html_classes(sys.argv[1])
