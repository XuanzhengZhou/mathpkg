---
role: proof
locale: en
of_concept: regular-measure-equality-by-integrals
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

Let $F$ be a nonvoid compact subset of $X$. Use (12.39.ii) to find decreasing sequences of open sets $(U_n)$ and $(V_n)$ containing $F$ with $\mu(U_n) \to \mu(F)$ and $\nu(V_n) \to \nu(F)$. Set $W_n = \bigcap_{k=1}^n (U_k \cap V_k)$; then $W_n$ are open, decreasing to $F$, with $\mu(W_n) \to \mu(F)$ and $\nu(W_n) \to \nu(F)$. For each $n$, use Urysohn's lemma to get $f_n \in \mathfrak{C}_{00}^+(X)$ with $\xi_F \leq f_n \leq \xi_{W_n}$. Then $\mu(F) \leq \int f_n d\mu = \int f_n d\nu \leq \nu(W_n)$, so $\mu(F) \leq \nu(F)$. By symmetry, $\mu(F) = \nu(F)$ for all compact $F$. By regularity, $\mu$ and $\nu$ agree on all measurable sets.
