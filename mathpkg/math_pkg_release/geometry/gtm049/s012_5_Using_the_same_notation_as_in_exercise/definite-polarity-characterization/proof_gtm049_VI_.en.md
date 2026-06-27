---
role: proof
locale: en
of_concept: definite-polarity-characterization
source_book: gtm049
source_chapter: "VI"
source_section: "6.2"
---
The "if" part is obvious: if $$\sigma$$ is positive or negative definite, then $$\sigma(v,v) \neq 0$$ for all non-zero $$v$$, so the quadric is empty.

For the converse, assume that $$\sigma(v,v) \neq 0$$ for all non-zero $$v$$. If there exist vectors $$a$$ and $$b$$ such that $$\sigma(a,a) > 0$$ and $$\sigma(b,b) < 0$$, then consider the quadratic equation in $$X$$:
$$\sigma(Xa - b, Xa - b) = 0,$$
which expands to
$$\sigma(a,a)X^2 - 2\sigma(a,b)X + \sigma(b,b) = 0.$$
Since $$\sigma(a,a)\sigma(b,b) < 0$$, the discriminant
$$\sigma(a,b)^2 - \sigma(a,a)\sigma(b,b) > 0,$$
so the equation has a real root $$x$$. Then $$\sigma(xa - b, xa - b) = 0$$, contradicting the assumption that $$\sigma(v,v) \neq 0$$ for all non-zero $$v$$. Hence all non-zero vectors must give $$\sigma(v,v)$$ of the same sign, so $$\sigma$$ is either positive definite or negative definite.
