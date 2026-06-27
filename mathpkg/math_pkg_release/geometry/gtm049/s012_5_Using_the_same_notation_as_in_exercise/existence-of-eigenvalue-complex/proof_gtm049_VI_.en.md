---
role: proof
locale: en
of_concept: existence-of-eigenvalue-complex
source_book: gtm049
source_chapter: "VI"
source_section: "6.3"
---
Let $$m(X)$$ be the minimum polynomial of $$f$$. By the fundamental theorem of algebra, $$m(X) = 0$$ always has a complex root $$x$$, giving the factorization
$$m(X) = (X - x)n(X)$$
in $$\mathbf{C}[X]$$. Substituting $$f$$ yields
$$(f - x1)n(f) = 0.$$
Now $$f - x1$$ cannot be an isomorphism, for otherwise $$n(f) = 0$$, contradicting the minimality of the degree of $$m(X)$$. Hence $$f - x1$$ has a non-trivial kernel, so there exists a non-zero vector $$c$$ such that $$cf = xc$$.
