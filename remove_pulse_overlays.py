import re
import sys

def remove_pulse_overlays(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to match the animate-pulse div
        # <div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 animate-pulse"></div>
        # It might vary slightly in spacing or attributes order, but the class string is quite specific.
        
        pattern = r'<div class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800 animate-pulse"></div>'
        
        # Remove all occurrences
        new_content = re.sub(pattern, '', content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully removed pulse overlays from {file_path}")
        else:
            print(f"No pulse overlays found in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_pulse_overlays.py <file_path>")
    else:
        remove_pulse_overlays(sys.argv[1])
