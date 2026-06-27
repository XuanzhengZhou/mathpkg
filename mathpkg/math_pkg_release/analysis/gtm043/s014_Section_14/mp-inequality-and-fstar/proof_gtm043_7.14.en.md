---
role: proof
locale: en
of_concept: mp-inequality-and-fstar
source_book: gtm043
source_chapter: "7"
source_section: "14 (7.8)"
---

The implication $M^p(f) \leq r \implies f^*(p) \leq r$ follows from the definition of $f^*(p)$ as the real number determined by the Dedekind cut: if $M^p(f) \leq r$, then $r \in B$, so $\inf B \leq r$, i.e., $f^*(p) \leq r$. The dual implication $f^*(p) < r \implies M^p(f) < r$ follows similarly.

For the counterexample: take $f = r + g$ where $M^p(g)$ is infinitely small and positive. Then $M^p(f) = r + M^p(g) > r$, yet $f^*(p) = r$. Thus $f^*(p) \leq r$ holds but $M^p(f) \leq r$ fails, showing the converse is false.
