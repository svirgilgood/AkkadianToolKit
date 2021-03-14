# Building an Akkadian Parser


0. Generate Parsing possibilities from every root, and store it in a trie. 

where most consonants are replaceable except for morphologically significant. 

```
i:  C0:  a:  C1:    C1:     a:  C2:     '3ms, G Pres'
                                        u: '3mp, G pres'   
         t:   a:    C1:     a:  C2:     '3ms, G perf'
                                        u: '3mp, G perf'
u:   š:  a:   C0:   C1:     a:  C2:     '3ms, Š pret'     
```

1. Generate Possible Case Endings, and suffixes from every noun in dictionary, store this in the same trie

