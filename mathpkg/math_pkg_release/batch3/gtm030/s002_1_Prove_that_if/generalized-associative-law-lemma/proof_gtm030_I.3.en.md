---
role: proof
locale: en
of_concept: generalized-associative-law-lemma
source_book: gtm030
source_chapter: "I"
source_section: "3. Generalized associative law. Powers."
---

By definition this holds if $m = 1$. Assume it true for $m = r$ and consider the case $m = r+1$. Here

$$\prod_{1}^{n} a_i \prod_{1}^{r+1} a_{n+j} = \prod_{1}^{n} a_i \left( \left( \prod_{1}^{r} a_{n+j} \right) a_{n+r+1} \right)$$

$$= \left( \prod_{1}^{n} a_i \prod_{1}^{r} a_{n+j} \right) a_{n+r+1}$$

$$= \left( \prod_{1}^{n+r} a_k \right) a_{n+r+1}$$

$$= \prod_{1}^{n+r+1} a_k.$$

The first equality uses the definition of the canonical product for $r+1$ factors. The second equality uses associativity of the binary composition. The third equality uses the induction hypothesis. The fourth equality uses the definition of the canonical product.
