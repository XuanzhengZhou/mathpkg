---
role: proof
locale: en
of_concept: characterization-of-ring-isomorphism
source_book: gtm013
source_chapter: "1"
source_section: "1.1"
---

If $\phi$ is an isomorphism, its inverse $\phi^{-1}$ serves as both $\psi$ and $\psi'$. Conversely, suppose functions $\psi, \psi': S \to R$ exist with $\psi \circ \phi = 1_R$ and $\phi \circ \psi' = 1_S$. Then $\psi = \psi \circ 1_S = \psi \circ (\phi \circ \psi') = (\psi \circ \phi) \circ \psi' = 1_R \circ \psi' = \psi'$, so $\psi = \psi'$. It follows that $\phi$ is bijective with inverse $\psi$.

It remains to show $\psi$ is a ring homomorphism. For $s, s' \in S$:
\begin{align*}
\phi(\psi(ss')) &= 1_S(ss') = ss' = 1_S(s)1_S(s') \\
&= \phi(\psi(s))\phi(\psi(s')) = \phi(\psi(s)\psi(s')),
\end{align*}
and since $\phi$ is injective, $\psi(ss') = \psi(s)\psi(s')$. Similarly, one checks that $\psi$ preserves addition and $\psi(1_S) = 1_R$. Thus $\psi$ is a ring isomorphism.
