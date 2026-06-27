---
role: proof
locale: en
of_concept: injective-module-localization-surjectivity
source_book: gtm052
source_chapter: "III"
source_section: "§3 Cohomology of a Noetherian Affine Scheme"
---

For each $i > 0$, let $\mathfrak{b}_i$ be the annihilator of $f^i$ in $A$. Then $\mathfrak{b}_1 \subseteq \mathfrak{b}_2 \subseteq \cdots$, and since $A$ is noetherian, there is an $r$ such that $\mathfrak{b}_r = \mathfrak{b}_{r+1} = \cdots$.

Now let $x \in I_f$ be an arbitrary element. We can write $x = y/f^n$ for some $y \in I$ and $n \geq 0$. Define a map $\varphi: (f^{n+r}) \to I$ by sending $f^{n+r}$ to $f^r y$. This is well-defined because if $a f^{n+r} = 0$, then $a \in \mathfrak{b}_{n+r} = \mathfrak{b}_r$, so $a f^r = 0$, hence $a f^r y = 0$. Since $I$ is injective, the map $\varphi$ extends to a map $\psi: A \to I$. Let $z = \psi(1)$. Then $f^{n+r} z = f^r y$, so in $I_f$ we have $z = y/f^n = x$. Thus the natural map $I \to I_f$ is surjective.
