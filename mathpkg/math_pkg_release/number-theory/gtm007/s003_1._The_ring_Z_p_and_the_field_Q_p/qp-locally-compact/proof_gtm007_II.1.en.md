---
role: proof
locale: en
of_concept: qp-locally-compact
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "1. The ring Z_p and the field Q_p"
---

*Proof.* The topology on $\mathbb{Q}_p$ is defined by the metric $d(x, y) = e^{-v_p(x-y)}$. Since $\mathbb{Z}_p$ is a compact topological ring (as a closed subset of the product of the finite discrete rings $A_n = \mathbb{Z}/p^n\mathbb{Z}$) and $\mathbb{Q}_p = \bigcup_{n \geq 0} p^{-n}\mathbb{Z}_p$, each $p^{-n}\mathbb{Z}_p$ is compact (it is homeomorphic to $\mathbb{Z}_p$ via multiplication by $p^n$). Moreover, $\mathbb{Z}_p$ is the open ball of radius $1$ centered at $0$ in $\mathbb{Q}_p$, hence $\mathbb{Z}_p$ is an open subring of $\mathbb{Q}_p$. Since every point has a compact neighborhood (specifically, a translate of $\mathbb{Z}_p$), $\mathbb{Q}_p$ is locally compact. Finally, $\mathbb{Q}$ is dense in $\mathbb{Q}_p$ because $\mathbb{Q}_p$ is the completion of $\mathbb{Q}$ with respect to the $p$-adic metric; equivalently, every $p$-adic integer is a limit of ordinary integers. $\square$
