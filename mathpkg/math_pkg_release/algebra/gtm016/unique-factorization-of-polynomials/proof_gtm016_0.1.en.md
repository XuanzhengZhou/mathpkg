---
role: proof
locale: en
of_concept: unique-factorization-of-polynomials
source_book: gtm016
source_chapter: "0.1"
source_section: "0.1"
---

Existence: By induction on $\operatorname{Deg} f(X)$. If $f(X)$ is irreducible, done. Otherwise $f(X) = g(X)h(X)$ with strictly smaller degrees. By induction, $g(X)$ and $h(X)$ factor into irreducibles, giving a factorization of $f(X)$. Uniqueness: Follows from Lemma 0.1.4 (Euclid's Lemma) by standard unique factorization argument: if $\prod g_i = \prod h_j$, then each $g_i$ must divide some $h_j$, and by irreducibility they are associates.
