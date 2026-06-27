---
role: proof
locale: en
of_concept: spectral-sequence-morphism-extension
source_book: gtm004
source_chapter: "VIII"
source_section: "8"
---

# Proof of Extension of Spectral Sequence Morphisms

Recall from (5.11) that the terms of a spectral sequence are defined recursively by

$$E_{n+1} = H(E_n, d_n),$$

where $d_n$ is the differential on the $n$-th page. In particular, the term $E_{m,n}$ for $m, n \geq k$ depends only on the part of the spectral sequence $E$ beginning with $E_k$.

Now suppose we are given a morphism of spectral sequences at the $k$-th page:

$$\varphi_* : E_k \to E_k'.$$

By the definition of a morphism of spectral sequences, $\varphi_*$ commutes with the differential $d_k$, i.e., $\varphi_* d_k = d_k' \varphi_*$. Hence $\varphi_*$ induces a well-defined morphism on homology:

$$\varphi_* : H(E_k, d_k) = E_{k+1} \to E_{k+1}' = H(E_k', d_k').$$

The induced morphism automatically commutes with $d_{k+1}$, so the same argument applies inductively. By induction on $n$, we obtain

$$\varphi_* : E_n \to E_n'$$

for all $n$ with $k \leq n < \infty$. Passage to the limit (or the explicit description of $E_\infty$ in terms of the $E_n$) yields the extension to $n = \infty$ as well. Thus

$$\varphi_* : E_n \to E_n', \quad k \leq n \leq \infty,$$

as claimed. $\square$
