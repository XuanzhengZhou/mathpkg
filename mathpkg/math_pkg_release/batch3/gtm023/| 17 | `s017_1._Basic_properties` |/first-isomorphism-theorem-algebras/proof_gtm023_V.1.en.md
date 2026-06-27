---
role: proof
locale: en
of_concept: first-isomorphism-theorem-algebras
source_book: gtm023
source_chapter: "V"
source_section: "1. Basic properties"
---

Let $\bar{\varphi} : A/\ker \varphi \rightarrow B$ be the induced injective linear mapping. We have the commutative diagram

$$A \xrightarrow{\varphi} B$$
$$\pi \downarrow \nearrow \bar{\varphi}$$
$$A/\ker \varphi$$

Since $\pi$ is a homomorphism, it follows that

$$\bar{\varphi}(\pi x \cdot \pi y) = \bar{\varphi} \pi(x y) = \varphi(x y) = \varphi(x) \cdot \varphi(y) = \bar{\varphi}(\pi x) \cdot \bar{\varphi}(\pi y).$$

This relation shows that $\bar{\varphi}$ is a homomorphism and hence a monomorphism. In particular, the induced mapping

$$\bar{\varphi} : A/\ker \varphi \xrightarrow{\cong} \operatorname{Im} \varphi$$

is an isomorphism.
