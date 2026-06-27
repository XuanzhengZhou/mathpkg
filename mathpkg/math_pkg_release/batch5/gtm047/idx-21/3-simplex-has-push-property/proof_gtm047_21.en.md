---
role: proof
locale: en
of_concept: 3-simplex-has-push-property
source_book: gtm047
source_chapter: ""
source_section: "21"
---

**Proof.** Let $D_1$ be a polyhedral 2-cell in $\operatorname{Bd} \sigma^3$, let

$$D_2 = \operatorname{Cl}\left( \operatorname{Bd} \sigma^3 - D_1 \right),$$

let $J = \operatorname{Bd} D_1 = \operatorname{Bd} D_2$, and let $N$ be a closed polyhedral neighborhood of $\sigma^3 - J$. By the preceding theorem (Theorem 5), take a PLH

$$f_1 : \mathbb{R}^3 \leftrightarrow \mathbb{R}^3, \quad \sigma^3 \leftrightarrow \sigma^3, \quad D_1 \leftrightarrow \sigma^2,$$

where $\sigma^2$ is a 2-face of $\sigma^3$. Then $f_1(N)$ is a closed polyhedral neighborhood of $\sigma^3 - f_1(J) = \sigma^3 - \operatorname{Bd} \sigma^2$. By Theorem 3 (which provides a push across a face), take a PLH

$$f_2 : \mathbb{R}^3 \leftrightarrow \mathbb{R}^3, \quad f_1(D_1) \leftrightarrow f_1(D_2),$$

such that $f_2|(\mathbb{R}^3 - f_1(N))$ is the identity. Let

$$f = f_1^{-1}f_2f_1.$$

Then $f$ is a PLH $\mathbb{R}^3 \leftrightarrow \mathbb{R}^3$, $D_1 \leftrightarrow D_2$, and $f|(\mathbb{R}^3 - N) = \text{identity}$. Thus $\sigma^3$ has the push property.
