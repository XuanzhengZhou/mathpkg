---
role: proof
locale: en
of_concept: invariant-measure-subgroup-closed
source_book: gtm018
source_chapter: "XII"
source_section: "62"
---

The fact that $Y$ is a subgroup of $X$ is trivial: if $y_1, y_2 \in Y$, then $\mu(y_1 y_2 E) = \mu(y_2 E) = \mu(E)$ for all Baire sets $E$, and $\mu(y_1^{-1} E) = \mu(y_1(y_1^{-1} E)) = \mu(E)$. To prove that $Y$ is closed, let $y_0$ be any fixed element of $\overline{Y}$ and let $C$ be any compact Baire set. If $U$ is any open Baire set such that $y_0 C \subset U$, then there exists a neighborhood $V$ of $e$ such that $V y_0 C \subset U$. Since $V y_0$ is a neighborhood of $y_0$, there exists an element $y$ in $Y$ such that $y \in V y_0$. Since $y C \subset V y_0 C \subset U$, it follows that

$$\mu(C) = \mu(y C) \leq \mu(U),$$

and hence, by the regularity of $\mu$, that $\mu(C) \leq \mu(y_0 C)$. Applying this conclusion to $y_0^{-1}$ and $y_0 C$ in place of $y_0$ and $C$, we obtain

$$\mu(y_0 C) \leq \mu(y_0^{-1}(y_0 C)) = \mu(C).$$

Thus $\mu(C) = \mu(y_0 C)$ for all compact Baire sets $C$. By the regularity of Baire measures, it follows that $\mu(E) = \mu(y_0 E)$ for every Baire set $E$, and hence $y_0 \in Y$. Therefore $Y$ is closed.
