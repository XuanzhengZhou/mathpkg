---
role: proof
locale: en
of_concept: characterization-of-bidual
source_book: gtm003
source_chapter: "IV"
source_section: "5"
---

By definition, $E''$ is the dual of $E'_\beta$, i.e., the space of all linear forms on $E'$ that are continuous for the strong topology $\beta(E', E)$. A linear form $x''$ on $E'$ is $\beta(E', E)$-continuous if and only if there exists a bounded subset $B \subset E$ such that $|x''(x')| \leq \sup_{x \in B} |\langle x, x' \rangle|$ for all $x' \in E'$.

The condition that $x''$ is continuous on every equicontinuous subset $H \subset E'$ endowed with $\sigma(E', E)|_H$ is equivalent to this, because:
- Equicontinuous subsets $H \subset E'$ are precisely the subsets of polars of neighborhoods of $0$ in $E$, and by the Alaoglu-Bourbaki theorem, they are $\sigma(E', E)$-compact.
- The strong topology $\beta(E', E)$ is the topology of uniform convergence on bounded subsets of $E$, which coincides with $\sigma(E', E)$ on each equicontinuous set (a consequence of the fact that on equicontinuous sets, $\sigma(E', E)$ is the only uniform structure compatible with the duality).

Thus $x'' \in E''$ if and only if $x''|_{H}$ is $\sigma(E', E)|_H$-continuous for every equicontinuous $H \subset E'$.
