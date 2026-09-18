import subprocess

with open('requirements.txt', 'w', encoding='utf-8') as f:
    subprocess.run(['pip', 'freeze'], stdout=f, text=True, encoding='utf-8')

with open('requirements.txt', 'a', encoding='utf-8') as f:
    f.write('\nwhitenoise\n')
