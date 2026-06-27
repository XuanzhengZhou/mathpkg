---
locale: en
of_concept: let-b-be-a-cw-complex-and-let-omega-x-0-p-0-b-0-be-a-locally
role: proof
source_book: gtm020
source_chapter: 4. General Fibre Bundles
source_section: '3'
---

First, we prove that $\phi_\omega(B)$ is surjective. Let $\xi$ be a locally trivial principal $G$-bundle over $B$. By Theorem 2 (7.1) under hypothesis (H1), the fibre bundle $\xi[X_0]$ has a cross section. By Theorem (8.2) we have a principal bundle morphism $(u, f)$: $\xi \rightarrow \omega$, and by Theorem (4.2) we have $\{\xi\} = \{f^*(\omega)\} = \phi_\omega(B)([f])$.

Second, we prove that $\phi_\omega(B)$ is injective. Let $f, g: B \rightarrow B_0$ be maps such that $\{f^*(\omega)\} = \{g^*(\omega)\}$. By (8.2) the fibre bundle $(f^*(\omega) \times I)[X_0]$ has a cross section $s$ over $B \times \{0, 1\}$, resulting from the principal bundle morphisms which are the compositions of $(f^*(\omega) \times I)|(B \times 0) \rightarrow f^*(\omega) \rightarrow \omega$ and $(f^*(\omega) \times I)|(B \times 1) \rightarrow g^*(\omega) \rightarrow \omega$. By Theorem 2 (7.1) under hypothesis (H1), this cross section $s$ prolongs to a cross section $s^*$ of $(f^*(\omega) \times I)[X_0]$ over $B \times I$. By (8.2), we have a principal bundle morphism $(w, h): f^*(\omega) \times I \rightarrow \

10. Let $\xi_i = (X_i, p_i, B_i)$ be a principal $G_i$-bundle, $i = 1, 2$. Then $\xi_1 \times \xi_2 = (X_1 \times X_2, p_1 \times p_2, B_1 \times B_2)$ has the structure of a principal $G_1 \times G_2$-bundle. If $\xi_i$ is a universal $G_i$-bundle, $i = 1, 2$, then $\xi_1 \times \xi_2$ is a universal $G_1 \times G_2$-bundle.

Apply this theorem to prove the existence of a universal bundle with a CW-complex as classifying space for each finitely generated abelian group (finite direct sum of cyclic groups).

11. If $u: G \rightarrow H$ is a continuous group morphism, define a map $B(u): B_G \rightarrow B_H$. Under what circumstances do you have a functor?

12. If $X$ is an $n$-connected CW-complex and if $Y$ is an $m$-connected CW-complex, prove that $X * Y$ is $(n + m + 1)$-connected.

13. Let $\xi = (X, p, B)$ be a numerable principal $G$-bundle. Prove that $\xi$ is universal if and only if $X$ is contractible.

Hint: See the article of Dold on partitions of unity, Theorem (7.5).
