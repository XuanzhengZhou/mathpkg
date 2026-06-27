---
role: proof
locale: en
of_concept: universality-via-hom-sets
source_book: gtm005
source_chapter: "III"
source_section: "1. Universal Arrows"
---

If $\langle r, u \rangle$ is universal, then the correspondence $f' \mapsto Sf' \circ u$ gives a bijection $\varphi_d \colon D(r, d) \to C(c, Sd)$ for each $d \in D$. Naturality is verified by the commutativity of

$$
\begin{array}{c}
D(r, r) \xrightarrow{\varphi_r} C(c, Sr) \\
D(r, f') \downarrow \phantom{D(r,f')} \downarrow C(c, Sf') \\
D(r, d) \xrightarrow{\varphi_d} C(c, Sd)
\end{array}
$$

which follows because both paths send an arrow $g \colon r \to r$ to $S(f' \circ g) \circ u = Sf' \circ Sg \circ u$.

Conversely, suppose $\varphi \colon D(r, -) \cong C(c, S-)$ is a natural isomorphism. Define $u = \varphi_r(1_r)$. For any $f \colon c \to Sd$, there is a unique $f' \colon r \to d$ with $\varphi_d(f') = f$. Naturality applied to $f'$ yields $\varphi_d(f') = Sf' \circ \varphi_r(1_r) = Sf' \circ u$, so $f = Sf' \circ u$. The uniqueness of $f'$ follows from the injectivity of $\varphi_d$. Thus $\langle r, u \rangle$ is universal.
