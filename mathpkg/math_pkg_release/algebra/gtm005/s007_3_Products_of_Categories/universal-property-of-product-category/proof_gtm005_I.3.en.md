---
role: proof
locale: en
of_concept: universal-property-of-product-category
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

Define $F: D \to B \times C$ on objects by $Fd = \langle Rd, Td \rangle$ for each $d \in \operatorname{Obj}(D)$, and on arrows by $Fh = \langle Rh, Th \rangle$ for each arrow $h$ in $D$. We verify:

\textbf{Functoriality.} For any arrow $h: d \to d'$ in $D$, $Fh = \langle Rh, Th \rangle: \langle Rd, Td \rangle \to \langle Rd', Td' \rangle = Fd \to Fd'$, so $F$ respects domains and codomains. For identities:
$$F(1_d) = \langle R(1_d), T(1_d) \rangle = \langle 1_{Rd}, 1_{Td} \rangle = 1_{\langle Rd, Td \rangle} = 1_{Fd}.$$
For composition, given $h: d \to d'$ and $h': d' \to d''$:
$$F(h' \circ h) = \langle R(h' \circ h), T(h' \circ h) \rangle = \langle Rh' \circ Rh, Th' \circ Th \rangle = \langle Rh', Th' \rangle \circ \langle Rh, Th \rangle = Fh' \circ Fh.$$
Thus $F$ is a functor.

\textbf{Projection condition.} For any arrow $h$ in $D$,
$$P(Fh) = P\langle Rh, Th \rangle = Rh, \quad Q(Fh) = Q\langle Rh, Th \rangle = Th,$$
so $PF = R$ and $QF = T$.

\textbf{Uniqueness.} Suppose $F': D \to B \times C$ is any functor with $PF' = R$ and $QF' = T$. Then for any arrow $h$ in $D$, we have $F'h = \langle f, g \rangle$ for some $f, g$, and $PF'h = f = Rh$, $QF'h = g = Th$. Hence $F'h = \langle Rh, Th \rangle = Fh$, so $F' = F$.
