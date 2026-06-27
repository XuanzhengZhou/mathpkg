---
role: proof
locale: en
of_concept: translation-invariance-subgroup-closed
source_book: gtm018
source_chapter: "63"
source_section: "Weil Topology"
---

**Theorem G.** The fact that $Y$ is a subgroup of $X$ is trivial: if $\mu(y_1E) = \mu(E)$ and $\mu(y_2E) = \mu(E)$ for all Baire sets $E$, then $\mu(y_1y_2E) = \mu(y_2E) = \mu(E)$ and $\mu(y_1^{-1}E) = \mu(y_1^{-1}y_1E) = \mu(E)$, the last equality using the invariance of $\mu$ under $y_1$ applied to the Baire set $y_1^{-1}E$.

To prove that $Y$ is closed, let $y_0$ be any fixed element of $\overline{Y}$ and let $C$ be any compact Baire set. If $U$ is any open Baire set such that $y_0C \subset U$, then there exists a neighborhood $V$ of $e$ such that $Vy_0C \subset U$. Since $Vy_0$ is a neighborhood of $y_0$, it follows that there exists an element $y$ in $Y$ such that $y \in Vy_0$. Since $yC \subset Vy_0C \subset U$, it follows that

$$\mu(C) = \mu(yC) \leq \mu(U),$$

and hence, by the regularity of $\mu$, that $\mu(C) \leq \mu(y_0C)$. Applying this conclusion to $y_0^{-1}$ and $y_0C$ in place of $y_0$ and $C$ we obtain the reverse inequality

$$\mu(y_0C) \leq \mu(y_0^{-1}(y_0C)) = \mu(C),$$

and hence the identity $\mu(C) = \mu(y_0C)$ for all compact Baire sets $C$. By regularity of Baire measures, it follows that $\mu(E) = \mu(y_0E)$ for every Baire set $E$ and hence that $y_0 \in Y$. $\blacksquare$
