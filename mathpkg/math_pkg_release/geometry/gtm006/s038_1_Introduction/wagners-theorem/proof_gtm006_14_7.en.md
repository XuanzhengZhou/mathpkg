---
role: proof
locale: en
of_concept: wagners-theorem
source_book: gtm006
source_chapter: "XIV"
source_section: "7"
---
**Proof of Wagner's Theorem (Theorem 14.11).** Let $\mathcal{A}$ be a finite affine plane of order $n$ with a collineation group $\Pi$ transitive on its affine lines.

If $n$ is even or a prime power, Lemma 14.8 gives the result directly.

Assume $n$ is odd and not a prime power. We derive a contradiction. Throughout:
- $\mathcal{Q}$ is a minimal 2-subplane with respect to $\Pi$, and $\mathcal{B} = \mathcal{Q}^{l_{\infty}}$. (Since $\Pi$ fixes $l_{\infty}$, $l_{\infty}$ is in $\mathcal{Q}$.)
- $\Gamma$ is a maximal 2-subgroup of $\Pi$ whose fixed elements are the points and lines of $\mathcal{Q}$.
- $\Sigma$ is the subgroup of $\Pi$ leaving $\mathcal{Q}$ invariant.

By Lemma 14.12, $\Sigma$ acting on $\mathcal{B}$ satisfies:
(i) For every affine flag in $\mathcal{B}$, there is an involutory homology in $\Sigma$ fixing that flag.
(ii) A propagation property for involutory homologies holds.

By Lemma 14.13, $\mathcal{B}$ is either a translation plane, the dual of a translation plane, or of type $\mathcal{H}(1)$. A detailed case analysis (not fully reproduced in the OCR text) eliminates the latter two possibilities, forcing $\mathcal{B}$ to be a translation plane.

By Theorem 14.10, $n = m^{2^g}$ where $m$ is the order of $\mathcal{Q}$. Since $\mathcal{B}$ is a translation plane, the structure forces $m$ to be a prime power. But then $n = m^{2^g}$ is also a prime power, contradicting the assumption that $n$ is not a prime power.

Thus $n$ must be a prime power, and by Lemma 14.8, $\mathcal{A}$ is a translation plane. $\square$
