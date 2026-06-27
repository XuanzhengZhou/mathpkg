---
role: proof
locale: en
of_concept: hilbert-left-invertible
source_book: gtm015
source_chapter: "57"
source_section: "57.19"
---

# Proof of Left invertibility in Hilbert space

**Proof.** (a) $\Rightarrow$ (b): If $ST = I$, then for any $x$, $\|x\| = \|STx\| \le \|S\|\|Tx\|$, so $\|Tx\| \ge \|S\|^{-1}\|x\|$, i.e., $T$ is bounded below.

(b) $\Rightarrow$ (c): If $T$ is bounded below, then by (57.4), $T$ is not a left TDZ, and by (57.1), $T$ is not a left divisor of zero.

(c) $\Rightarrow$ (a): If $T$ is not a left TDZ and not a left divisor of zero, then $T$ is injective and $T$ is bounded below (57.4). Since $H$ is a Hilbert space, $T^*T$ is invertible (its spectrum is contained in $[M^2, \infty)$ for some $M > 0$). Then $(T^*T)^{-1}T^*$ is a left inverse of $T$.
