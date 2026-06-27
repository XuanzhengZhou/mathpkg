---
role: proof
locale: en
of_concept: lusin-theorem
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** Select open $U$ with $E \subset U$ and $\iota(U) < \iota(E) + \varepsilon/4$.
*Case I: $f = \xi_A$.* Find compact $F \subset A$ with $\iota(A \cap F') < \varepsilon/2$. Choose open $V$ with $F \subset V \subset U$, $V$ precompact, $\iota(V \cap F') < \varepsilon/2$. By Urysohn's lemma (6.80), get $g \in \mathfrak{C}_{00}(X)$ with $g = 1$ on $F$, $g = 0$ on $V'$. Then $\{f \neq g\} \subset (V \cap F') \cup (A \cap F')$, so $\iota(\{f \neq g\}) < \varepsilon$.
*Case II: Simple functions.* Linear combination of Case I.
*Case III: Bounded $f$.* Approximate uniformly by simple functions on a compact set, then use Tietze extension theorem (7.40).
*Case IV: General $f$.* Truncation argument. The norm bound is achieved by radial projection. $\square$
