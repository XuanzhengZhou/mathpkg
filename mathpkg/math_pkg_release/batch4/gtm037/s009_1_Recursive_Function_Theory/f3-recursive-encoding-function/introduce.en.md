---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition introduces the family of functions $f_3^m$ that recursively encode $m$-tuples of natural numbers into a single G\"{o}del number. The base case $f_3^1$ concatenates the code for $2$ (representing a separator) with $f_2 x$ (a block of $x+1$ ones). For higher arities, $f_3^m$ recursively concatenates the encoding of the first $m-1$ arguments with the $m$-th argument. These functions provide the machinery for encoding multiple inputs to a Turing machine as a single number.
