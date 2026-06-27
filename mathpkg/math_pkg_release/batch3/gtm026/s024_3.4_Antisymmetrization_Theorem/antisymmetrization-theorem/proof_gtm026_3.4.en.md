---
role: proof
locale: en
of_concept: antisymmetrization-theorem
source_book: gtm026
source_chapter: "3"
source_section: "3.4"
---

**Proof.** Define the equivalence relation $A \sim B$ on the objects of $\mathcal{A}$ by $A \sim B$ if and only if $AU = K = BU$ and $\mathrm{id}_K : A \to B$, $\mathrm{id}_K : B \to A$ are admissible, and let $[A]$ denote the equivalence class of $A$. Extend $\sim$ to an equivalence relation on the class of all morphisms of $\mathcal{A}$ by $\psi : A \to B \sim \psi' : A' \to B'$ if and only if $[A] = [A']$, $[B] = [B']$ and $\psi U = \psi' U$. Define a category $[\mathcal{A}]$ with objects all $[A]$, morphisms

$$[\mathcal{A}]([A], [B]) = \{ [\psi] \mid \psi : A \to B \},$$

composition $[\psi_1][\psi_2] = [\psi_1 \psi_2]$, and identity $\mathrm{id}_{[A]} = [\mathrm{id}_A]$. It is routine to check that all this is well-defined, giving rise to the functor $\mathcal{A} \to [\mathcal{A}]$ which is full, faithful, and surjective on objects. There exists a unique functor $[U] : [\mathcal{A}] \to \mathcal{K}$ such that the obvious triangle commutes, and $([\mathcal{A}], [U])$ is an antisymmetric concrete category over $\mathcal{K}$.

If $H : (\mathcal{A}, U) \to (\mathcal{B}, V) \in \operatorname{Con}(\mathcal{K})$, and if $\psi : A \to B$ is admissible in $\mathcal{A}$, then $[H]([\psi]) = [H\psi]$ defines the unique functor $[H] : [\mathcal{A}] \to [\mathcal{B}]$ over $\mathcal{K}$ such that $[H] = H$ on the quotient. This establishes that the antisymmetric reflection $[\cdot]$ is a functor on $\operatorname{Con}(\mathcal{K})$, full, faithful, and surjective on objects, making "Antisymmetric" a full reflective replete subcategory of $\operatorname{Con}(\mathcal{K})$.

To complete the structural representation, consider $(\mathcal{C}, V)$ and $(\mathcal{C}', V')$ in $\operatorname{Struct}(\mathcal{K})$ with $\Phi : \mathcal{C} \to \mathcal{C}'$ full and representative. Let $C$ be a $\mathcal{C}$-object. By hypothesis, there exists an isomorphism $\bar{f} : A\Phi \to C$. Set $f = \bar{f}U$. Since $\mathcal{C}'$ satisfies "structure is abstract", there exists $C\Gamma$ such that $f : AH \to C\Gamma$ and its inverse are admissible. To see that $\Gamma$ is well-defined on objects, suppose also that $\bar{g} : A'\Phi \to C$ is an isomorphism and that $C'$ is unique such that $g : A'H \to C'$ and its inverse are admissible. Since $\Phi$ is full, $\bar{f} \cdot (\bar{g})^{-1} : A\Phi \to A'\Phi$ is admissible, so $f \cdot g^{-1}$ is admissible from $A$ to $A'$ and hence, via $H$, from $AH$ to $A'H$. It follows that $\mathrm{id}_{CV} = f^{-1} \cdot (f \cdot g^{-1}) \cdot g$ is admissible from $C\Gamma$ to $C'$; symmetrically, $\mathrm{id}_{CV}$ is admissible from $C'$ to $C\Gamma$, so they are equal.

By combining the antisymmetrization construction with the above, we have only to establish that if $(\mathcal{A}, U)$ is antisymmetric, then there exists $(\mathcal{C}, V)$ in $\operatorname{Struct}(\mathcal{K})$ representing it. Define objects of $\mathcal{C}$ as equivalence classes $[A, f]$ where $A \in \mathcal{A}$ and $f : K \xrightarrow{\cong} AU$ in $\mathcal{K}$, with $(A, f) \sim (A', f')$ if and only if $f \cdot (f')^{-1} : A \to A'$ and $f' \cdot f^{-1} : A' \to A$ are both admissible. For $[A, f] \in \mathcal{C}(K)$, $[B, g] \in \mathcal{C}(L)$, and $h : K \to L$ in $\mathcal{K}$, define $h$ to be admissible from $[A, f]$ to $[B, g]$ if and only if $f \cdot h \cdot g^{-1} : A \to B$ is admissible in $\mathcal{A}$. This is well-defined: if $(A, f) \sim (A', f')$ and $(B, g) \sim (B', g')$, then from $f \cdot h \cdot g^{-1} : A \to B$ and $(A, f) \leqslant (A', f')$, we deduce $f' \cdot h \cdot g^{-1} : A' \to B$; from $(B', g') \leqslant (B, g)$, we have $g \cdot (g')^{-1} : B \to B'$; therefore

$$(f' \cdot h \cdot g^{-1}) \cdot g \cdot (g')^{-1} = f' \cdot h \cdot (g')^{-1} : A' \to B'$$

is admissible. Define $A\Phi = [A, \mathrm{id}_{AU}]$. The numerous omitted verifications are left as an easy calculation. $\square$
