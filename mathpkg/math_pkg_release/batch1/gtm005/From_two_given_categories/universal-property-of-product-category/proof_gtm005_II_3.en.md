---
role: proof
locale: en
of_concept: universal-property-of-product-category
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

The two conditions $PF = R$ and $QF = T$ require that for any arrow $h: d \to d'$ in $D$, the image $Fh = \langle f, g \rangle$ must satisfy $Pf = Rh$ and $Qg = Th$, hence $Fh = \langle Rh, Th \rangle$. This determines $F$ uniquely on both objects and arrows.

Conversely, define $F$ by $Fd = \langle Rd, Td \rangle$ on objects and $Fh = \langle Rh, Th \rangle$ on arrows. Then $F$ is a functor:
\begin{itemize}
\item $F(1_d) = \langle R(1_d), T(1_d) \rangle = \langle 1_{Rd}, 1_{Td} \rangle = 1_{\langle Rd, Td \rangle} = 1_{Fd}$,
\item $F(h' \circ h) = \langle R(h' \circ h), T(h' \circ h) \rangle = \langle Rh' \circ Rh, Th' \circ Th \rangle = \langle Rh', Th' \rangle \circ \langle Rh, Th \rangle = Fh' \circ Fh$.
\end{itemize}
Thus $F$ is a functor satisfying $PF = R$ and $QF = T$, proving both existence and uniqueness.
