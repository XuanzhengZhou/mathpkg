---
role: proof
locale: en
of_concept: tensor-hom-adjunction-for-chain-complexes
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "1. Double Complexes"
---

# Proof of Tensor-Hom Adjunction for Chain Complexes

Let $C$, $D$, $E$ be chain complexes over a commutative ring $\Lambda$. We have the tensor product $C \otimes_\Lambda D$ (using Tot) and the Hom complex $\operatorname{Hom}_\Lambda(D, E)$ (using Tot'). The adjunction is:

$$\operatorname{Hom}_\Lambda(C \otimes_\Lambda D, E) \cong \operatorname{Hom}_\Lambda(C, \operatorname{Hom}_\Lambda(D, E)).$$

**Construction of the isomorphism.** An element $f \in \operatorname{Hom}_\Lambda(C \otimes_\Lambda D, E)_n$ is a family
$$f = \{f_{(p,q),r}\}, \quad f_{(p,q),r}: C_{-p} \otimes D_{-q} \to E_r, \quad r - (p+q) = n.$$
Under the standard adjunction for $\Lambda$-modules,
$$\operatorname{Hom}_\Lambda(C_{-p} \otimes D_{-q}, E_r) \cong \operatorname{Hom}_\Lambda(C_{-p}, \operatorname{Hom}_\Lambda(D_{-q}, E_r)),$$
each $f_{(p,q),r}$ corresponds to an element $f'_{p,(q,r)}$, where
$$f'_{p,(q,r)}: C_{-p} \to \operatorname{Hom}_\Lambda(D_{-q}, E_r).$$
Let $f' = \{f'_{p,(q,r)}\}$, so that $f$ corresponds to $f'$ under the isomorphisms
$$\prod_{r-p-q=n} \operatorname{Hom}(C_{-p} \otimes D_{-q}, E_r) \cong \prod_{r-p-q=n} \operatorname{Hom}(C_{-p}, \operatorname{Hom}(D_{-q}, E_r)).$$

**Compatibility with differentials.** The differential in the tensor product complex is
$$\partial^{\otimes}(c \otimes d) = \partial c \otimes d + (-1)^p c \otimes \partial d, \quad c \in C_{-p}, \; d \in D_{-q}.$$
The differential in $\operatorname{Hom}_\Lambda(C \otimes_\Lambda D, E)$ is
$$(\partial^H f)_{(p,q),r}(c \otimes d) = (-1)^{p+q+r} \Big( f_{(p+1,q),r}(\partial c \otimes d) + (-1)^p f_{(p,q+1),r}(c \otimes \partial d) \Big) + \partial f_{(p,q),r+1}(c \otimes d).$$

On the other hand, the differential in $\operatorname{Hom}_\Lambda(C, \operatorname{Hom}_\Lambda(D, E))$ acts by
$$(\partial^H f')_{p,(q,r)}(c)(d) = (-1)^{p+q+r} \Big( f'_{p+1,(q,r)}(\partial c)(d) + (-1)^{q+r} f'_{p,(q+1),r}(c)(\partial d) + \partial f'_{p,(q),r+1}(c)(d) \Big).$$

A direct calculation shows that $\partial^H f$ corresponds to $\partial^H f'$ under the isomorphism, so the isomorphism of graded modules commutes with the differentials and thus defines an isomorphism of chain complexes.

**Naturality.** The isomorphism is natural in $C$, $D$, and $E$, as it is built from the natural Hom-tensor adjunction for $\Lambda$-modules applied degreewise.
