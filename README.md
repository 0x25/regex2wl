# regex2wl
Powerful Python-based utility designed to generate worldlist from a set of predefined regular expressions. These regular expressions are stored in a file, allowing for easy customization.

# Requirement
pip install exrex

# Usage
```usage: regex2wl.py [-h] [-i PFILE] [-p PATTERN] [-v] [-o OUTPUT]

 Generate Worldlist from regex

options:
  -h, --help            show this help message and exit
  -i PFILE, --pfile PFILE
                        File with one pattern line by line
  -p PATTERN, --pattern PATTERN
                        regex pattern based on exrex lib
  -v, --verbose         verbose mode
  -o OUTPUT, --output OUTPUT
                        file to save result
```

# Example
python3 regex2wl.py -i patterns.example.txt

administrator  
administrator!  
administrator*  
administrator;  
administrator?  
administrator@  
administrat0r  
administrat0r!  
administrat0r*  
administrat0r;  
administrat0r?  
administrat0r@  
administr@tor  
administr@tor!  
administr@tor*  
administr@tor;  
administr@tor?  
...  

python3 regex2wl.py -p "T[a@]rg[e3]t[cC][o0O]mp[a@]gny20[12]{1}[0-9]{1}[!\*;?@]{0,1}"
Targetcompagny2010  
Targetcompagny2010!  
Targetcompagny2010*  
Targetcompagny2010;  
Targetcompagny2010?  
Targetcompagny2010@  
Targetcompagny2011  
Targetcompagny2011!  
Targetcompagny2011*  
Targetcompagny2011;  
Targetcompagny2011?  
Targetcompagny2011@  
Targetcompagny2012  
Targetcompagny2012!  
Targetcompagny2012*  
Targetcompagny2012;  
...  




Enjoy  
