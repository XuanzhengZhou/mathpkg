---
role: proof
locale: en
of_concept: lemma-real-eigenvalue
source_book: gtm049
source_chapter: "6"
source_section: "6.4"
---

Let $f$ be extended to the complexification $V_{(C)}$ of $V$ by the rule $(u + iv)f = uf + i(vf)$. Clearly the extended $f$ is a linear mapping of $V_{(C)}$ into $V_{(C)}$.

By Proposition 3 (every linear mapping of a finite-dimensional complex vector space has an eigenvector), there exists an eigenvector $c = a + ib$ in $V_{(C)}$ with eigenvalue $x \in \mathbb{C}$. We must show that $x$ is real.

Consider the extended bilinear form $\sigma'$ on $V_{(C)}$ as defined in $\S$5.6 (p. 113). The equation

$$\sigma'(wf, w') = \sigma'(w, w'f)$$

holds for all $w, w'$ in $V_{(C)}$ (since $f$ is $\sigma$-symmetric). Hence, in particular,

$$\sigma'(\bar{c}f, c) = \sigma'(\bar{c}, cf)$$

where $\bar{c} = a - ib$. But $cf = xc$ and so $\bar{c}f = \bar{x}\bar{c}$ (where $\bar{x}$ denotes the complex conjugate of $x$). Therefore

$$\bar{x}\sigma'(\bar{c}, c) = x\sigma'(\bar{c}, c),$$

where $\sigma'(\bar{c}, c) = \sigma(a, a) + \sigma(b, b) > 0$ since $\sigma$ is positive definite and $c \neq 0$. Thus $\bar{x} = x$, so $x$ is real.
