---
role: proof
locale: en
of_concept: functoriality-of-tensor-and-hom-under-homotopy
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "1. Double Complexes"
---

# Proof of Functoriality of Tensor Product and Hom under Chain Homotopy

**Proposition 1.2.** Chain maps $\varphi: C \to C'$, $\psi: D \to D'$ induce chain maps

$$\varphi \otimes \psi: C \otimes_\Lambda D \to C' \otimes_\Lambda D',$$

$$\operatorname{Hom}(\varphi, \psi): \operatorname{Hom}_\Lambda(C', D) \to \operatorname{Hom}_\Lambda(C, D').$$

Moreover, if $\varphi \simeq \varphi'$ and $\psi \simeq \psi'$, then $\varphi \otimes \psi \simeq \varphi' \otimes \psi'$ and $\operatorname{Hom}(\varphi, \psi) \simeq \operatorname{Hom}(\varphi', \psi')$.

**Proof of the induced chain maps.** Given chain maps $\varphi: C \to C'$ and $\psi: D \to D'$, define $\varphi \otimes \psi$ degreewise by
$$(\varphi \otimes \psi)_{p+q}(c_p \otimes d_q) = \varphi_p(c_p) \otimes \psi_q(d_q).$$
Since $\varphi$ and $\psi$ commute with the differentials, we verify:
$$\partial^{\otimes}(\varphi \otimes \psi)(c \otimes d) = \partial^{\otimes}(\varphi(c) \otimes \psi(d)) = \partial\varphi(c) \otimes \psi(d) + (-1)^p \varphi(c) \otimes \partial\psi(d)$$
$$= \varphi(\partial c) \otimes \psi(d) + (-1)^p \varphi(c) \otimes \psi(\partial d) = (\varphi \otimes \psi)(\partial c \otimes d + (-1)^p c \otimes \partial d) = (\varphi \otimes \psi)\partial^{\otimes}(c \otimes d).$$
Thus $\varphi \otimes \psi$ is a chain map.

For the Hom complex, define $\operatorname{Hom}(\varphi, \psi)$ by
$$\operatorname{Hom}(\varphi, \psi)(f) = \psi \circ f \circ \varphi,$$
where $f: C'_{-p} \to D_q$, so $\operatorname{Hom}(\varphi, \psi)(f): C_{-p} \to D'_q$. A straightforward verification using the differential formula (1.6) shows this commutes with $\partial^H$.

**Proof of homotopy invariance.** Suppose $\Sigma: \varphi \simeq \varphi'$ is a chain homotopy, i.e., $\varphi - \varphi' = \partial \Sigma + \Sigma \partial$. Define
$$\Sigma^{\otimes}: C \otimes_\Lambda D \to C' \otimes_\Lambda D'$$
by $\Sigma^{\otimes}(c \otimes d) = \Sigma(c) \otimes \psi(d)$ for $c \in C_p$, $d \in D_q$. One checks that
$$\partial^{\otimes}\Sigma^{\otimes} + \Sigma^{\otimes}\partial^{\otimes} = (\partial\Sigma + \Sigma\partial) \otimes \psi = (\varphi - \varphi') \otimes \psi = \varphi \otimes \psi - \varphi' \otimes \psi.$$
Thus $\varphi \otimes \psi \simeq \varphi' \otimes \psi$.

Similarly, if $\Gamma: \psi \simeq \psi'$ is a chain homotopy for the $D$ side, define $\Gamma^{\otimes}$ by $\Gamma^{\otimes}(c \otimes d) = (-1)^p \varphi'(c) \otimes \Gamma(d)$. Then one shows that $\varphi' \otimes \psi \simeq \varphi' \otimes \psi'$.

Combining the two homotopies $\Sigma^{\otimes}$ and $\Gamma^{\otimes}$ yields a chain homotopy between $\varphi \otimes \psi$ and $\varphi' \otimes \psi'$.

For Hom, one symmetrically constructs homotopies $\operatorname{Hom}(\Sigma, \psi)$ and $\operatorname{Hom}(\varphi', \Gamma)$ and combines them to get $\operatorname{Hom}(\varphi, \psi) \simeq \operatorname{Hom}(\varphi', \psi')$.
