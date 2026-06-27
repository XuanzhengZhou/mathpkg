---
role: proof
locale: en
of_concept: t-algebra-cooptimal-morphism
source_book: gtm026
source_chapter: "3"
source_section: "1"
---

To prove $(K, \xi)$ is a $\mathbf{T}$-algebra, we must verify the two algebra axioms: $K\eta \cdot \xi = \mathrm{id}_K$ and $K\mu \cdot \xi = \xi T \cdot \xi$.

For the first axiom, we have $h \cdot K\eta \cdot \xi = L\eta \cdot hT \cdot \xi = L\eta \cdot \gamma \cdot h = \mathrm{id}_L \cdot h = h$. Since $h$ is epi, $K\eta \cdot \xi = \mathrm{id}_K$. (We use naturality of $\eta$: $L\eta \cdot h = hT \cdot K\eta$, and the axiom $L\eta \cdot \gamma = \mathrm{id}_L$ for the $\mathbf{T}$-algebra $(L, \gamma)$.)

For the second axiom, we use "$hTT$ is epi" to deduce $K\mu \cdot \xi = \xi T \cdot \xi$ from the analogous equality for $(L, \gamma)$ transported along $h$. The full diagram chase uses the naturality of $\mu$ and the given commutative square.

To show $h$ is co-optimal in $\mathcal{K}^{\mathbf{T}}$: since $hT$ is epi, the argument in 2.1.56 applies, establishing that any $\mathbf{T}$-algebra structure on $K$ making $h$ a $\mathbf{T}$-homomorphism must be $\xi$, and that any factorization of $h$ through a $\mathbf{T}$-homomorphism yields a unique lift.
