---
role: proof
locale: en
of_concept: universal-property-of-tensor-algebra
source_book: gtm009
source_chapter: "V"
source_section: "17.1"
---
The homomorphism $\psi$ is constructed by defining it on the homogeneous components. For a decomposable tensor $v_1 \otimes \dots \otimes v_k \in T^kV$, set $\psi(v_1 \otimes \dots \otimes v_k) = \phi(v_1)\phi(v_2)\dots\phi(v_k)$. This is well-defined because the tensor product is multilinear and the product in $A$ is associative. On $T^0V = F$, set $\psi(c \cdot 1) = c \cdot 1_A$. Extending linearly to all of $\mathfrak{T}(V)$ yields an algebra homomorphism. The condition $\psi|_V = \phi$ holds by construction on $T^1V = V$, and uniqueness follows because $\mathfrak{T}(V)$ is generated as an algebra by $V$ and $1$, so any two homomorphisms agreeing on $V$ and sending $1$ to $1$ must be equal.
