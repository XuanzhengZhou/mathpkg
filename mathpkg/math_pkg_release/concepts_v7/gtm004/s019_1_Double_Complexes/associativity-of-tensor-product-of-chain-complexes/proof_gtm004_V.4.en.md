---
role: proof
locale: en
of_concept: associativity-of-tensor-product-of-chain-complexes
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof of Associativity of the Tensor Product of Chain Complexes

**Proposition 4.1.** Let $C'$, $C$, $C''$ be chain complexes over $\mathbb{Z}$ (or more generally over a commutative ring $\Lambda$) that are free. Then there is a natural isomorphism of chain complexes
$$(C' \otimes_\mathbb{Z} C) \otimes_\mathbb{Z} C'' \cong C' \otimes_\mathbb{Z} (C \otimes_\mathbb{Z} C'').$$

**Proof.** Both sides are defined as the total complex (Tot) of a triple tensor product. On the level of graded modules, associativity of the ordinary tensor product gives a degreewise isomorphism:
$$((C' \otimes C) \otimes C'')_n = \bigoplus_{p+q+r=n} (C'_p \otimes C_q) \otimes C''_r \cong \bigoplus_{p+q+r=n} C'_p \otimes (C_q \otimes C''_r) = (C' \otimes (C \otimes C''))_n.$$

It remains to verify that this identification is compatible with the differentials.

On the left-hand side, the differential on $C' \otimes C$ is
$$\partial^{\otimes}_{C' \otimes C}(c' \otimes c) = \partial c' \otimes c + (-1)^p c' \otimes \partial c, \quad c' \in C'_p, \; c \in C_q.$$
Then the differential on $(C' \otimes C) \otimes C''$ is
$$\partial^{\otimes}_{(C' \otimes C) \otimes C''}((c' \otimes c) \otimes c'') = \partial^{\otimes}_{C' \otimes C}(c' \otimes c) \otimes c'' + (-1)^{p+q} (c' \otimes c) \otimes \partial c''$$
$$= (\partial c' \otimes c) \otimes c'' + (-1)^p (c' \otimes \partial c) \otimes c'' + (-1)^{p+q} (c' \otimes c) \otimes \partial c''.$$

On the right-hand side, the differential on $C \otimes C''$ is
$$\partial^{\otimes}_{C \otimes C''}(c \otimes c'') = \partial c \otimes c'' + (-1)^q c \otimes \partial c'', \quad c \in C_q, \; c'' \in C''_r.$$
Then the differential on $C' \otimes (C \otimes C'')$ is
$$\partial^{\otimes}_{C' \otimes (C \otimes C'')}(c' \otimes (c \otimes c'')) = \partial c' \otimes (c \otimes c'') + (-1)^p c' \otimes \partial^{\otimes}_{C \otimes C''}(c \otimes c'')$$
$$= \partial c' \otimes (c \otimes c'') + (-1)^p c' \otimes (\partial c \otimes c'' + (-1)^q c \otimes \partial c'')$$
$$= \partial c' \otimes (c \otimes c'') + (-1)^p c' \otimes \partial c \otimes c'' + (-1)^{p+q} c' \otimes c \otimes \partial c''.$$

Under the associativity isomorphism $(c' \otimes c) \otimes c'' \leftrightarrow c' \otimes (c \otimes c'')$, the two differential formulas match exactly. Hence the isomorphism is an isomorphism of chain complexes.

**Naturality.** The isomorphism is natural in $C'$, $C$, and $C''$, as it is built from the natural associativity isomorphisms of the ordinary tensor product applied degreewise.

When the complexes are not free but the homology groups are finitely generated, one can replace them by free resolutions (using Proposition 2.2) and the associativity holds up to homotopy equivalence.
