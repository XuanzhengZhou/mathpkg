---
role: proof
locale: en
of_concept: decomposition-for-relatively-prime-factors
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

The statement follows by induction on $r$. The base case $r = 2$ is exactly Corollary I. Assume the statement holds for $r-1$ factors. Write $f = (f_1 \cdots f_{r-1}) \cdot f_r$. Since the $f_i$ are pairwise relatively prime, $f_1 \cdots f_{r-1}$ is relatively prime to $f_r$. By Corollary I,

$$K(f) = K(f_1 \cdots f_{r-1}) \oplus K(f_r).$$

By the induction hypothesis, $K(f_1 \cdots f_{r-1}) = K(f_1) \oplus \cdots \oplus K(f_{r-1})$. The result follows.
