---
role: proof
locale: en
of_concept: product-is-a-functor-on-cat
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

Define $\times: \text{Cat} \times \text{Cat} \to \text{Cat}$ as follows. On objects, $\times(B, C) = B \times C$. On arrows, for functors $U: B \to B'$ and $V: C \to C'$, define $\times(U, V) = U \times V: B \times C \to B' \times C'$.

\textbf{Preservation of identities.} For the identity functors $I_B$, $I_C$:
$$(I_B \times I_C)\langle b, c \rangle = \langle I_B b, I_C c \rangle = \langle b, c \rangle, \quad (I_B \times I_C)\langle f, g \rangle = \langle I_B f, I_C g \rangle = \langle f, g \rangle,$$
so $I_B \times I_C = I_{B \times C}$.

\textbf{Preservation of composition.} Given $U: B \to B'$, $U': B' \to B''$, $V: C \to C'$, $V': C' \to C''$, we have from the previous proposition:
$$(U' \times V') \circ (U \times V) = U'U \times V'V.$$

This is exactly $\times((U', V') \circ (U, V)) = \times(U', V') \circ \times(U, V)$, where composition in $\text{Cat} \times \text{Cat}$ is componentwise. Thus $\times$ is a functor.
