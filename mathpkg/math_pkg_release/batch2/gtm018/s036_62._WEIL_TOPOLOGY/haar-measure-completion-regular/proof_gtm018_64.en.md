---
role: proof
locale: en
of_concept: haar-measure-completion-regular
source_book: gtm018
source_chapter: "64"
source_section: "Weil Topology"
---

**Theorem H.** It is sufficient to prove that if $U$ is any bounded open set, then there exists a Baire set $E$ contained in $U$ such that $U - E$ may be covered by a Baire set of measure zero. Given $U$, we select the Baire set $E \subset U$ so that $\mu(E)$ is maximal; by Theorem G there exists a compact invariant subgroup $Y$ of $X$ such that $E$ is a union of cosets of $Y$ and such that the quotient group $\hat{X} = X/Y$ is separable.

Let $\pi$ be the projection from $X$ onto $\hat{X}$, and write $F = \pi^{-1}\pi(U - E)$; we shall prove that $F$ is a Baire set of measure zero.

Since $\pi(U - E) = \pi(U) - \pi(E)$, we have that $\pi(U - E)$ is open in $\hat{X}$ and therefore is a countable union of compact sets. Using the maximality of $\mu(E)$ and the properties of the Haar measure on the quotient, one shows that $\mu(F) = 0$. Specifically:

If $V$ is a Baire open set contained in $U$, then it follows from the maximal property of $E$ that $\mu(V - E) = 0$. If $\nu$ is a Haar measure in $Y$ such that $\nu(Y) = 1$, and if we write $\hat{\mu} = \mu\pi^{-1}$ and $g(x) = \nu(x^{-1}(V - E) \cap Y)$, then by 63.G there exists a nonnegative Baire measurable function $\hat{g}$ on $\hat{X}$ such that $g = \hat{g}\pi$ and

$$0 = \mu(V - E) = \int \hat{g} d\hat{\mu} = \int g d\mu \geq \int_{\pi^{-1}\pi(V - E)} \nu(x^{-1}(V - E) \cap Y) d\mu(x) \geq 0.$$

For $x \in V - E$, the set $x^{-1}(V - E) \cap Y$ is a nonempty open subset of $Y$, hence has positive $\nu$-measure. This forces $\mu(\pi^{-1}\pi(V - E)) = 0$, and by a covering argument, $\mu(F) = 0$.

Thus $U - E \subset F$ and $\mu(F) = 0$, establishing completion regularity. $\blacksquare$
