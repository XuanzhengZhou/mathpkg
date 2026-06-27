---
role: proof
locale: en
of_concept: colimits-in-reflective-subcategories
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* Let $(K, \psi)$ be a colimit of $D$ qua diagram in $\mathcal{K}$ and let $\eta: K \longrightarrow L$ be a reflection of $K$ in $\mathcal{L}$. Given any lower bound $(L', \Gamma)$ of $D$ with $L' \in \mathcal{L}$, there exists a unique $f: K \longrightarrow L'$ in $\mathcal{K}$ with $\psi_i f = \Gamma_i$ for all $i \in N(\Delta)$, by the universal property of the colimit in $\mathcal{K}$. Since $L' \in \mathcal{L}$, the universal property of the reflection $\eta$ yields a unique $g: L \longrightarrow L'$ in $\mathcal{L}$ with $\eta g = f$. Then $(\psi_i \eta) g = \psi_i f = \Gamma_i$, so $g$ is the required mediating morphism. Uniqueness follows from the uniqueness of $f$ and of $g$. Hence $(L, \psi \eta)$ is a colimit of $D$ in $\mathcal{L}$. $\square$
