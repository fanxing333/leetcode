import sys
import os

def create_files(filename):
    # Define the file names
    py_filename = f"hot100/{filename}.py"
    md_filename = f"hot100/{filename}.md"
    
    # Define the default templates
    py_template = '''from typing import List

class Solution:
    def func(self, nums: List[int]) -> List[List[int]]:
        pass

if __name__ == "__main__":
    input = []

    s = Solution()
    print(s.func(input))
'''
    
    md_template = f'''# {filename}

This is a markdown file for {filename}.
'''
    
    # Write the templates to the respective files
    with open(py_filename, 'w') as py_file:
        py_file.write(py_template.format(base_filename=filename))
    
    with open(md_filename, 'w') as md_file:
        md_file.write(md_template)
    
    print(f"Created {py_filename} and {md_filename} with default templates.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_files.py <filename>")
    else:
        create_files(sys.argv[1])