---
role: proof
locale: en
of_concept: representation-ordered-lcs-normal-cone
source_book: gtm003
source_chapter: "V"
source_section: "4"
---

We note first from (3.3), Corollary 1, that the topology of $E$ is the topology of uniform convergence on the equicontinuous subsets of the dual cone $C' \subset E'$. Let $\{B_\alpha : \alpha \in A\}$ be a fundamental family of $\sigma(E', E)$-closed equicontinuous subsets of $C'$; under the topology induced by $\sigma(E', E)$, each $B_\alpha$ is a compact space. We define $X$ as follows: Endow $A$ with the discrete topology, $C'$ with the topology induced by $\sigma(E', E)$, and let $X_\alpha$ be the subspace $\{\alpha\} \times B_\alpha$ of the topological product $A \times C'$; then $X$ is defined to be the subspace $\bigcup_\alpha X_\alpha$ of $A \times C'$. The space $X$ is the topological sum of the family $\{B_\alpha : \alpha \in A\}$; clearly, $X$ is a locally compact space in which every $X_\alpha$ is open and compact, and hence every compact subset of $X$ is contained in the union of finitely many sets $X_\alpha$. For each $x \in E$, we define an element $f_x \in \mathcal{R}(X)$ by putting $f_x(t) = \langle x, x' \rangle$ for every $t = (\alpha, x') \in X$; it is clear that $x \to f_x$ is an algebraic and order isomorphism of $E$ into $\mathcal{R}(X)$. Finally, since a closed subset of $X$ is compact if and only if it is contained in a finite union $\bigcup_\alpha X_\alpha$, it is also evident that $x \to f_x$ is a homeomorphism. Moreover, $\mathcal{R}(X)$ is complete; hence the image of $E$ under $x \to f_x$ is closed in $\mathcal{R}(X)$ if and only if $E$ is complete. If $E$ is metrizable, then the family $\{B_\alpha : \alpha \in A\}$ can be assumed to be countable.
