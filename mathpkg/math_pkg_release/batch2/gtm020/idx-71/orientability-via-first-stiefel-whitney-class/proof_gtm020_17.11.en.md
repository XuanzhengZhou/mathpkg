---
role: proof
locale: en
of_concept: orientability-via-first-stiefel-whitney-class
source_book: gtm020
source_chapter: "17. Chern Classes and Stiefel-Whitney Classes"
source_section: "11"
---

A vector bundle $\xi$ is orientable if and only if $\Lambda^n \xi$ is trivial, that is, $w_1(\Lambda^n \xi) = 0$. But $w_1(\Lambda^n \xi) = w_1(\lambda_1 \otimes \cdots \otimes \lambda_n) = w_1(\lambda_1) + \cdots + w_1(\lambda_n) = w_1(\xi)$ by 5(6.10). Therefore, $\xi$ is orientable if and only if $w_1(\xi) = 0$.

For the general case, let $f: B_1 \to B$ be a splitting map for $\xi$. Then $\xi$ is orientable if and only if $f^*(\xi)$ is orientable, because $f^*(w_1(\Lambda^n \xi)) = w_1(\Lambda^n f^*(\xi))$ holds and $f^*$ is a monomorphism. Finally, we have $w_1(\xi) = 0$ if and only if $w_1(f^*(\xi)) = 0$. This proves the theorem.
