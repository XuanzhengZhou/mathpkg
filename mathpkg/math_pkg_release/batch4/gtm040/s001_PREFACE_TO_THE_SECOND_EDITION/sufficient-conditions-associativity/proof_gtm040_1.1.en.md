---
role: proof
locale: en
of_concept: sufficient-conditions-associativity
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

Each of the three conditions ensures that the product $|A|\,|B|\,|C|$ has all finite entries:

(1) If $A$ is row-finite, then for each fixed row $i$, the sum $\sum_{m} |A_{im}|$ is a finite sum of finite terms. Combined with the entries of $|B|$ and $|C|$, the iterated sum for each entry of $(|A|\,|B|)\,|C|$ is finite.

(2) If $C$ is column-finite, a symmetric argument applies by working with columns instead of rows.

(3) If $B$ has finite entries and both $A$ and $C$ are bounded (by $M_A$ and $M_C$ respectively), then $|A_{im}| \leq M_A$ and $|C_{nj}| \leq M_C$ for all indices, so the triple product entries are bounded by $M_A \cdot (\sup_{m,n} |B_{mn}|) \cdot M_C$ times well-defined sums.

In each case, Corollary 1-5 applies, yielding associativity. Additionally, Proposition 1-2 (distributivity) and Corollary 1-5 together imply that distributivity and associativity may be freely used under these conditions.
