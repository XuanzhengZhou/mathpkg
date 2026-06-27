---
role: proof
locale: en
of_concept: eigenvalue-of-orthogonal-automorphism
source_book: gtm049
source_chapter: "VI"
source_section: "6.4"
---
Let $$c = a + ib$$ be an eigenvector of $$f$$ with eigenvalue $$x$$, so $$cf = xc$$. Then the conjugate satisfies $$\bar{c}f = \bar{x}\bar{c}$$. Hence
$$\sigma(\bar{c}f, cf) = \sigma(\bar{x}\bar{c}, xc) = \bar{x}x\sigma(\bar{c}, c).$$
On the other hand, since $$f$$ preserves $$\sigma$$,
$$\sigma(\bar{c}f, cf) = \sigma(\bar{c}, c).$$
Since $$c \neq 0$$, $$\sigma(\bar{c}, c) = \sigma(a,a) + \sigma(b,b) > 0$$. Therefore $$\bar{x}x = 1$$, so $$x = e^{i\theta}$$ for some real $$\theta$$ which may be chosen to satisfy $$-\pi < \theta \leq \pi$$.
