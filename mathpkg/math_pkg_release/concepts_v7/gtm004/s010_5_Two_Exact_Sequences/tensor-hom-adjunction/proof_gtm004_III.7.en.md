---
role: proof
locale: en
of_concept: tensor-hom-adjunction
source_book: gtm004
source_chapter: "III"
source_section: "7"
---

# Proof of Tensor-Hom Adjunction (Theorem 7.2)

For any right $\Lambda$-module $A$, the functor $A \otimes_\Lambda - : \mathfrak{M}_\Lambda^l \rightarrow \mathfrak{Ab}$ is left adjoint to the functor $\operatorname{Hom}_{\mathbb{Z}}(A, -) : \mathfrak{Ab} \rightarrow \mathfrak{M}_\Lambda^l$.

**Proof.** The left $\Lambda$-module structure of $\operatorname{Hom}_{\mathbb{Z}}(A, G)$ is induced by the right $\Lambda$-module structure of $A$: for $f \in \operatorname{Hom}_{\mathbb{Z}}(A, G)$ and $\lambda \in \Lambda$, define $(\lambda f)(a) = f(a\lambda)$. (See Section I.8.)

We construct a natural isomorphism

$$
\eta : \operatorname{Hom}_{\mathbb{Z}}(A \otimes_\Lambda B, G) \xrightarrow{\cong} \operatorname{Hom}_\Lambda(B, \operatorname{Hom}_{\mathbb{Z}}(A, G)).
$$

Given a $\mathbb{Z}$-homomorphism $\varphi : A \otimes_\Lambda B \rightarrow G$, define $\eta(\varphi) : B \rightarrow \operatorname{Hom}_{\mathbb{Z}}(A, G)$ by

$$
(\eta(\varphi)(b))(a) = \varphi(a \otimes b), \quad a \in A, \; b \in B.
$$

One verifies that $\eta(\varphi)$ is a $\Lambda$-module homomorphism: for $\lambda \in \Lambda$,

$$
(\eta(\varphi)(\lambda b))(a) = \varphi(a \otimes \lambda b) = \varphi(a\lambda \otimes b) = (\eta(\varphi)(b))(a\lambda) = (\lambda \cdot \eta(\varphi)(b))(a).
$$

Conversely, given a $\Lambda$-homomorphism $\psi : B \rightarrow \operatorname{Hom}_{\mathbb{Z}}(A, G)$, define $\eta^{-1}(\psi) : A \otimes_\Lambda B \rightarrow G$ by

$$
\eta^{-1}(\psi)(a \otimes b) = (\psi(b))(a),
$$

extended linearly. The $\Lambda$-linearity of $\psi$ ensures this is well-defined on the tensor product.

The maps $\eta$ and $\eta^{-1}$ are mutually inverse and natural in both $B$ and $G$, establishing the adjunction

$$
A \otimes_\Lambda - \dashv \operatorname{Hom}_{\mathbb{Z}}(A, -).
$$

Naturality means that for $\beta : B \rightarrow B'$ and $\gamma : G \rightarrow G'$, the appropriate diagrams commute.
