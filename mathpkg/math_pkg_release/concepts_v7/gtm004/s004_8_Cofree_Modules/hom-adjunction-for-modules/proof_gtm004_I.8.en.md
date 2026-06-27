---
role: proof
locale: en
of_concept: hom-adjunction-for-modules
source_book: gtm004
source_chapter: "I. Modules"
source_section: "8. Cofree Modules"
---

# Proof of Proposition 8.1: Adjoint Isomorphism for Hom and Co-Hom

We construct the natural isomorphism

$$\eta = \eta_A : \operatorname{Hom}_{\Lambda}(A, \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)) \xrightarrow{\cong} \operatorname{Hom}_{\mathbb{Z}}(A, G).$$

**Construction of $\eta$.** Given a $\Lambda$-module homomorphism $\varphi : A \rightarrow \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$, define $\eta_A(\varphi) : A \rightarrow G$ by evaluation at the identity:

$$\eta_A(\varphi)(a) = \varphi(a)(1), \quad a \in A,$$

where $1 \in \Lambda$ is the identity element. Since $\varphi(a) \in \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$, the value $\varphi(a)(1)$ is a well-defined element of $G$. The map $\eta_A(\varphi)$ is a homomorphism of abelian groups because $\varphi$ is additive in $a$.

**Inverse map.** Conversely, given an abelian group homomorphism $\psi : A \rightarrow G$, define $\eta_A^{-1}(\psi) : A \rightarrow \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ by

$$\eta_A^{-1}(\psi)(a)(\lambda) = \psi(\lambda a), \quad a \in A, \; \lambda \in \Lambda.$$

Note that $\lambda a$ uses the left $\Lambda$-module structure of $A$. For each fixed $a$, the map $\lambda \mapsto \psi(\lambda a)$ is a $\mathbb{Z}$-module homomorphism (since $\psi$ is additive), so $\eta_A^{-1}(\psi)(a) \in \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$. Moreover, $\eta_A^{-1}(\psi)$ is a $\Lambda$-module homomorphism because the left $\Lambda$-module structure on $\operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ (coming from the right $\Lambda$-module structure of $\Lambda$) satisfies

$$(\lambda \cdot \eta_A^{-1}(\psi)(a))(\mu) = \eta_A^{-1}(\psi)(a)(\mu \lambda) = \psi(\mu \lambda a) = \eta_A^{-1}(\psi)(\lambda a)(\mu).$$

**Naturality.** For every $\Lambda$-module homomorphism $\alpha : A \rightarrow B$, the diagram

$$\begin{CD}
\operatorname{Hom}_{\Lambda}(B, \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)) @>{\eta_B}>{\cong}> \operatorname{Hom}_{\mathbb{Z}}(B, G) \\
@V{\alpha^*}VV @VV{\alpha^*}V \\
\operatorname{Hom}_{\Lambda}(A, \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)) @>{\eta_A}>{\cong}> \operatorname{Hom}_{\mathbb{Z}}(A, G)
\end{CD}$$

commutes. Indeed, for $\varphi \in \operatorname{Hom}_{\Lambda}(B, \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G))$ and $a \in A$,

$$(\alpha^* \circ \eta_B)(\varphi)(a) = \eta_B(\varphi)(\alpha(a)) = \varphi(\alpha(a))(1),$$

$$(\eta_A \circ \alpha^*)(\varphi)(a) = \eta_A(\varphi \circ \alpha)(a) = (\varphi \circ \alpha)(a)(1) = \varphi(\alpha(a))(1).$$

Thus $\eta$ is a natural isomorphism of contravariant functors. $\square$
