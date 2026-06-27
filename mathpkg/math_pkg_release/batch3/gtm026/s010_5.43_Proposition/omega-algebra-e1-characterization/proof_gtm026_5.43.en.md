---
role: proof
locale: en
of_concept: omega-algebra-e1-characterization
source_book: gtm026
source_chapter: "5"
source_section: "5.43"
---

If $\bar{x} \in XT$ then there exists $n \in \text{Law}(\mathbf{T})$, $f: n \longrightarrow X$ and $\alpha \in nT$ such that $\langle \alpha, fT \rangle = \bar{x}$, and we are forced to define $\bar{x}\xi = \langle f, \delta_\alpha \rangle$. Suppose now that $m \in \text{Law}(\mathbf{T})$, $g: m \longrightarrow X$ and $\beta \in mT$ are again such that $\langle \beta, gT \rangle = \bar{x}$. For $\xi$ to be well defined, we must be able to prove that $\langle f, \delta_\alpha \rangle = \langle g, \delta_\beta \rangle$.

Let $S \subset X$ be the union of the images of $f$ and $g$. There exists $p \in \text{Law}(\mathbf{T})$ and a bijection $\psi: p \longrightarrow S$. Define $a: n \longrightarrow p$ and $b: m \longrightarrow p$ by $a = \bar{f} \circ \psi^{-1}$ and $b = \bar{g} \circ \psi^{-1}$, where $\bar{f}: n \longrightarrow S$ and $\bar{g}: m \longrightarrow S$ are the maps induced by restricting the codomains. Define $h: p \longrightarrow X = \psi \circ \text{inc}$. Then $\langle \alpha, aT \rangle hT = \langle \alpha, fT \rangle = \langle \beta, gT \rangle = \langle \beta, bT \rangle hT$. Since $hT$ is injective by 5.42, $\langle \alpha, aT \rangle = \langle \beta, bT \rangle$. Therefore, there is an equation in $E_1$ forcing $\langle f, \delta_\alpha \rangle = \langle g, \delta_\beta \rangle$, so $\xi$ is well defined.
