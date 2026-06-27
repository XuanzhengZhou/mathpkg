---
role: proof
locale: en
of_concept: universal-arrow-representation
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Given a natural isomorphism $\varphi: D(r, -) \cong C(c, S -)$, the identity $1_r \in D(r, r)$ goes by $\varphi_r$ to an arrow $u = \varphi_r(1_r): c \to Sr$ in $C$. For any $f': r \to d$, the naturality diagram

\[
\begin{CD}
D(r, r) @>{\varphi_r}>> C(c, Sr) \\
@V{D(r, f')}VV @VV{C(c, Sf')}V \\
D(r, d) @>{\varphi_d}>> C(c, Sd)
\end{CD}
\]

commutes. Following $1_r$ through this diagram: the top-right path sends $1_r$ to $Sf' \circ u$, while the left-bottom path sends $1_r$ to $\varphi_d(f')$. Since $\varphi_d$ is a bijection, this states precisely that each arrow $f: c \to Sd$ has the form $f = Sf' \circ u$ for a unique $f'$. This is exactly the condition that $\langle r, u \rangle$ is a universal arrow from $c$ to $S$.

Conversely, given a universal arrow $\langle r, u: c \to Sr \rangle$, define $\varphi_d: D(r, d) \to C(c, Sd)$ by $\varphi_d(f') = Sf' \circ u$. The universal property ensures this is a bijection, and naturality in $d$ follows from functoriality of $S$: for any $g: d \to d'$, $S(g \circ f') \circ u = Sg \circ (Sf' \circ u)$.
