---
role: proof
locale: en
of_concept: orthosymmetric-iff-symmetric-or-skew-symmetric
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** If $\sigma$ is orthosymmetric, then $\bot(\sigma) = \top(\sigma)$. Define $\tau(a,b) = \sigma(b,a)$. Then $\tau$ is a bilinear form on $V$ and $\bot(\sigma) = \bot(\tau)$. By Lemma 4, $\sigma = z\tau$ for some non-zero scalar $z$, i.e., $\sigma(a,b) = z\sigma(b,a)$ for all $a,b$. Interchanging $a$ and $b$ yields $\sigma(b,a) = z\sigma(a,b)$, so $\sigma(a,b) = z^2\sigma(a,b)$ for all $a,b$. Since $\sigma$ is not identically zero (otherwise it is trivially both symmetric and skew-symmetric), we have $z^2 = 1$, hence $z = \pm 1$. Thus either $\sigma(a,b) = \sigma(b,a)$ (symmetric) or $\sigma(a,b) = -\sigma(b,a)$ (skew-symmetric). Conversely, both symmetric and skew-symmetric forms are clearly orthosymmetric.
