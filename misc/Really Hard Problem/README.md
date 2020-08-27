## Really Hard Problem

The main idea to find the flag is to use Python3 and feed the altered DNA sequence as a parameter to the function.

#### Step-1:
After I downloaded `dee_en_aee.txt`, I opened it and had a look at it.
It had this:
```
ACTCACGAATATAGTGAGCTCTTAGTAGAGCGCTACAACATTTGCGAATTCTTGGCAGGGTCGGCGAATGATAGCCACGAATTACTGTCG
```

#### Step-2:
I was searching for scripting and decoding it, and I found this very interesting post on GeeksforGeeks.
https://www.geeksforgeeks.org/dna-protein-python-3/

#### Step-3:
Now, I got the script `Exploit.py` and wrote it to get the flag.

```py
#!/usr/bin/env python3

def translate(seq):
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""

    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein


with open('dee_en_aee.txt') as f:
  data = f.read().strip()
  print("Flag: " + 'flag{' + translate(data) + '}')
```
#### Step-4:
I ran it as `python3 Exploit.py` and got this as output:

```
Flag: flag{THEYSELLVERYNICEFLAGSANDSHELLS}
```

#### Step-5:
Finally, the flag becomes:
`flag{THEYSELLVERYNICEFLAGSANDSHELLS}`