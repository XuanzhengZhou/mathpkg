---
role: proof
locale: en
of_concept: bidual-characterization
source_book: gtm003
source_chapter: "IV"
source_section: "5"
---

**Proof.** Consider the canonical inclusions $E \subset E'' \subset E'^*$, where $E'^*$ denotes the algebraic dual of $E'$. The canonical imbedding $E \hookrightarrow E''$ is given by the evaluation map $x \mapsto f_x$ with $f_x(x') = \langle x, x' \rangle$.

An element $f \in E'^*$ belongs to $E''$ if and only if $f$ is continuous on $E'_\beta$. Since $\beta(E', E)$ is the topology of uniform convergence on all $\sigma(E, E')$-bounded subsets of $E$, continuity of $f$ on $E'_\beta$ is equivalent to $f$ being bounded on every strongly bounded subset of $E'$. By the definition of the polar topology, this is equivalent to $f$ being continuous on every equicontinuous subset of $E'$ when equipped with the weak topology $\sigma(E', E)$. Thus $f \in E''$ if and only if $f$ is $\sigma(E', E)$-continuous on each equicontinuous subset of $E'$. $\square$
