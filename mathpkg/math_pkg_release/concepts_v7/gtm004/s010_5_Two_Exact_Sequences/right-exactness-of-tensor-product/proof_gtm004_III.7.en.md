---
role: proof
locale: en
of_concept: right-exactness-of-tensor-product
source_book: gtm004
source_chapter: "III"
source_section: "7"
---

# Proof of Right Exactness of the Tensor Product (Proposition 7.3)

For any right $\Lambda$-module $A$, the functor $A \otimes_\Lambda - : \mathfrak{M}_\Lambda^l \rightarrow \mathfrak{Ab}$ is right exact. That is, for any short exact sequence

$$
B' \xrightarrow{\beta'} B \xrightarrow{\beta''} B'' \rightarrow 0,
$$

the induced sequence

$$
A \otimes_\Lambda B' \xrightarrow{1 \otimes \beta'} A \otimes_\Lambda B \xrightarrow{1 \otimes \beta''} A \otimes_\Lambda B'' \rightarrow 0
$$

is exact.

**Proof.** By Theorem 7.2, the functor $A \otimes_\Lambda -$ is left adjoint to $\operatorname{Hom}_{\mathbb{Z}}(A, -)$. By the dual of Theorem II.7.7, any functor that is a left adjoint preserves colimits. In particular, it preserves cokernels and coproducts. Since right exactness is equivalent to preserving cokernels (and the zero object), $A \otimes_\Lambda -$ is right exact.

More concretely, right exactness means:
(i) $1 \otimes \beta''$ is epimorphic: every generator $a \otimes b'' \in A \otimes_\Lambda B''$ lifts to $a \otimes b$ where $\beta''(b) = b''$ (since $\beta''$ is epimorphic).
(ii) $\operatorname{Im}(1 \otimes \beta') = \operatorname{Ker}(1 \otimes \beta'')$: this follows from the universal property of the tensor product.

The reader should note that, even if $\beta'$ is monomorphic, $1 \otimes \beta'$ will not be monomorphic in general. For example, let $\Lambda = \mathbb{Z}$, $A = \mathbb{Z}_2$, and consider the exact sequence $\mathbb{Z} \xrightarrow{\mu} \mathbb{Z} \twoheadrightarrow \mathbb{Z}_2$ where $\mu$ is multiplication by 2. Then

$$
\mu_*(n \otimes m) = n \otimes 2m = 2n \otimes m = 0 \otimes m = 0,
$$

$n \in \mathbb{Z}_2$, $m \in \mathbb{Z}$. Hence $\mu_* : \mathbb{Z}_2 \otimes \mathbb{Z} \rightarrow \mathbb{Z}_2 \otimes \mathbb{Z}$ is the zero map, while $\mathbb{Z}_2 \otimes \mathbb{Z} \cong \mathbb{Z}_2 \neq 0$. This failure of left exactness motivates the definition of the Tor functor.
