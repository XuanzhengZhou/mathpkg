---
role: proof
locale: en
of_concept: b-e-e-equals-l-e-e-finite-dim
source_book: gtm023
source_chapter: "VII"
source_section: "5 (unnumbered)"
---

Since every linear transformation $\varphi$ of a finite-dimensional space $E$ is continuous (cf. sec. 1.22), and continuity implies boundedness (by the bounded-iff-continuous proposition, 7.21), it follows that $\varphi$ is bounded. Hence $B(E;E) = L(E;E)$.

For the second assertion, the closed unit sphere $S = \{x \in E : \|x\| = 1\}$ is compact (since $E$ is finite-dimensional and all norms are equivalent). The function $x \mapsto \|\varphi x\|$ is continuous (as the composition of the continuous map $\varphi$ with the continuous norm), so by the extreme value theorem it attains its supremum on the compact set $S$. Thus $\sup$ can be replaced by $\max$.
