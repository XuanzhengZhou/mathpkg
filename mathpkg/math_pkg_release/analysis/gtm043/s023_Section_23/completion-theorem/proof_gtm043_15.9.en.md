---
role: proof
locale: en
of_concept: completion-theorem-uniform-spaces
source_book: gtm043
source_chapter: "15"
source_section: "23"
---

We extend every pseudometric $d \in \mathcal{D}$ to a pseudometric $d^c$ on $\beta X$, in such a way that for each fixed $p \in \beta X$, the mapping $q \mapsto d^c(p, q)$ is continuous on $\beta X$ into $\mathbf{R}$.

Fix $y \in X$. The function $x \mapsto d(x, y)$ belongs to $C(X)$ (15.4(c)); hence, by Stone's theorem (6.5), it has a continuous extension $p \mapsto \bar{d}(p, y)$ from $\beta X$ into the one-point compactification $\mathbf{R}^*$ of $\mathbf{R}$. This extension actually maps into $\mathbf{R}$ itself. For, select $Z \in A^p$ such that $d\{Z\}$ is finite. The triangle inequality implies that $\{d(z, y) : z \in Z\}$ is a bounded set of real numbers. By continuity, $\bar{d}(p, y)$ belongs to the closure of this set.

Using the triangle inequality, one establishes that $d^c$ is a continuous extension to $\beta X \times \beta X$, and it defines a pseudometric on $\beta X$.

Define $p \equiv p'$ in $\beta X$ to mean that $d^c(p, p') = 0$ for all $d \in \mathcal{D}$. This is an equivalence relation. The equivalence classes $p^\gamma$ form the points of $\gamma X$. Setting $d^\gamma(p^\gamma, q^\gamma) = d^c(p, q)$ defines a pseudometric on $\gamma X$. The collection $\{d^\gamma : d \in \mathcal{D}\}$ generates a Hausdorff uniform structure on $\gamma X$.

Since the restriction of $d^c$ to $X \times X$ is $d$, and $X$ is Hausdorff, the mapping $x \mapsto x^\gamma$ is an embedding of $[X; \mathcal{D}]$ in $\gamma X$. One then verifies that $\gamma X$ is complete and that $X$ is dense in $\gamma X$, establishing that $\gamma X$ is a completion of $X$.
