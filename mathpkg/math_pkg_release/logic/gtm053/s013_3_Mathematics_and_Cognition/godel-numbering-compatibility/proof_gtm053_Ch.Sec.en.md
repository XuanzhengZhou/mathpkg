---
role: proof
locale: en
of_concept: godel-numbering-compatibility
source_book: gtm053
source_chapter: "VII"
source_section: "1"
---

The construction uses prime factorization: $N(a_1 a_2 \cdots a_m) = 2^{N_0(a_1)+1} \cdot 3^{N_0(a_2)+1} \cdots p_m^{N_0(a_m)+1}$. This makes the length function $l(n)$ (number of prime divisors) recursive: $l(n) = \sum_{i=1}^n s(v_i(n)) - n$. Juxtaposition is $m * n = m \prod_{j=1}^{l(n)} p_{l(m)+j}^{v_j(n)-1}$. The image is decidable because it is characterized by a bounded universal quantifier condition.
