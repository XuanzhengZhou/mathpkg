---
role: proof
locale: en
of_concept: orthosymmetric-iff-symmetric-or-skew-symmetric
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

If $\sigma$ is symmetric or skew-symmetric, then $\sigma(a,b) = 0$ is trivially equivalent to $\sigma(b,a) = 0$ (in the symmetric case $\sigma(a,b) = \sigma(b,a)$, and in the skew-symmetric case $\sigma(a,b) = -\sigma(b,a)$). Thus $\sigma$ is orthosymmetric.

Conversely, suppose $\sigma$ is orthosymmetric. Define $	au(a,b) = \sigma(b,a)$. Then $	au$ is a bilinear form on $V$ and the orthosymmetry condition implies $ot(\sigma) = ot(	au)$. By Lemma 4, there exists a non-zero scalar $z$ such that $\sigma = z	au$, i.e., $\sigma(a,b) = z\sigma(b,a)$ for all $a,b$ in $V$. Applying this relation twice gives $\sigma(a,b) = z\sigma(b,a) = z^2\sigma(a,b)$, so $(z^2 - 1)\sigma(a,b) = 0$ for all $a,b$. If $\sigma$ is not the zero form, then $z^2 = 1$, hence $z = \pm 1$. Therefore $\sigma(a,b) = \pm \sigma(b,a)$, i.e., $\sigma$ is symmetric (if $z = 1$) or skew-symmetric (if $z = -1$). If $\sigma$ is the zero form, it is both symmetric and skew-symmetric.
