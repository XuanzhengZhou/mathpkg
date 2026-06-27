---
role: proof
locale: en
of_concept: cohomology-base-change-theorem
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

As above, we may assume that $Y$ is affine, say $Y = \operatorname{Spec} A$ with $A$ noetherian. Using the expression for $h^i(y, \mathcal{F})$ from the proof of the Semicontinuity Theorem (12.8), we have

$$h^i(y, \mathcal{F}) = \dim_{k(y)} \ker(W^i \otimes k(y) \to L^{i+1} \otimes k(y)).$$

Since $h^i(y, \mathcal{F})$ is constant by hypothesis, both the functions $\dim W^i \otimes k(y)$ and $\dim W^{i+1} \otimes k(y)$ must be constant (by the upper semicontinuity argument from the proof of Theorem 12.8, the constancy of the kernel dimension forces the constancy of the source dimension, and since the dimension of $W^{i+1}$ affects the kernel for the next index, it too must be constant).

But this implies (by standard facts about coherent sheaves on affine schemes, specifically that a coherent sheaf whose fibre dimension is constant is locally free) that $\widetilde{W}^i$ and $\widetilde{W}^{i+1}$ are both locally free sheaves on $Y$.

Now by Proposition 12.4, the condition that $W^i$ is flat (equivalently, locally free) implies that $T^i$ and $T^{i+1}$ are both left exact. Since $T^i$ is always exact in the middle (Proposition 12.1), it follows that $T^i$ is exact. Then by Corollary 12.6, $T^i(A)$ is a projective $A$-module. But $R^i f_*(\mathcal{F})$ is precisely $\widetilde{T^i(A)}$, so it is a locally free sheaf.

Finally, by Proposition 12.5, since $T^i$ is right exact (being exact), we have the isomorphism

$$T^i(M) \cong T^i(A) \otimes_A M$$

for all $A$-modules $M$. Taking $M = k(y)$ and sheafifying, we obtain

$$R^i f_*(\mathcal{F}) \otimes k(y) \cong H^i(X_y, \mathcal{F}_y)$$

for all $y \in Y$. The naturality of this isomorphism follows from the naturality of the map $\varphi$ in Proposition 12.5.

The statement about $i-1$ follows by the same argument, noting that constancy of $h^{i-1}(y, \mathcal{F})$ ensures $W^{i-1}$ and $W^i$ are locally free, which implies $T^{i-1}$ is left exact, hence exact, etc.
