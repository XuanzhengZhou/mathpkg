---
role: proof
locale: en
of_concept: real-symmetric-mapping-real-eigenvalue
source_book: gtm049
source_chapter: "VI"
source_section: "6.3"
---
Extend $$f$$ to the complexification $$V_{(C)}$$ of $$V$$ by the rule $$(u + iv)f = uf + i(vf)$$. The extended $$f$$ is a linear mapping of $$V_{(C)}$$ into $$V_{(C)}$$. By Proposition 3, there exists an eigenvector $$c = a + ib$$ with eigenvalue $$x$$. We must show that $$x$$ is real.

Consider the extended bilinear form $$\sigma$$ on $$V_{(C)}$$ (as in §5.6). The $$\sigma$$-symmetry equation
$$\sigma(wf, w) = \sigma(w, wf)$$
holds for all $$w, w$$ in $$V_{(C)}$$. Hence, with $$\bar{c} = a - ib$$,
$$\sigma(\bar{c}f, c) = \sigma(\bar{c}, cf).$$
But $$cf = xc$$ and so $$\bar{c}f = \bar{x}\bar{c}$$. Therefore
$$\bar{x}\sigma(\bar{c}, c) = x\sigma(\bar{c}, c).$$
Since $$\sigma(\bar{c}, c) = \sigma(a,a) + \sigma(b,b) > 0$$ (by positive definiteness of $$\sigma$$), we deduce $$\bar{x} = x$$, so $$x$$ is real.
