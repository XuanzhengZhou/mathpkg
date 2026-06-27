---
role: proof
locale: en
of_concept: fitting-decomposition-properties
source_book: gtm023
source_chapter: "13"
source_section: "13.7"
---
$F_0$ is the generalized eigenspace corresponding to the irreducible polynomial $t$, and $F_1$ is the direct sum of the remaining generalized eigenspaces. Since each generalized eigenspace is stable under $\varphi$, both $F_0$ and $F_1$ are stable.

If the minimum polynomial of $\varphi$ does not contain the factor $t$, then $F_0 = 0$ and $\varphi_0 = 0$ is trivially nilpotent. Otherwise, $F_0 = K(t^l) = \ker(\varphi^l)$ for some $l$, so $\varphi_0^l = 0$, establishing nilpotence of $\varphi_0$.

For $F_1$, since the minimum polynomial of $\varphi_1$ consists of irreducible factors none of which is $t$, $0$ is not a root of the minimum polynomial of $\varphi_1$. Hence $\varphi_1$ is injective (otherwise $0$ would be an eigenvalue, implying $t$ divides the minimum polynomial). Since $F_1$ is finite-dimensional (being a subspace of $E$), injectivity implies bijectivity, so $\varphi_1$ is an isomorphism.

The projection operators for this decomposition are $\pi_0 = \sum_{i: f_i = t} \pi_i$ and $\pi_1 = \sum_{i: f_i \neq t} \pi_i$. Since each $\pi_i$ is a polynomial in $\varphi$ (Theorem 13.5), their sums $\pi_0$ and $\pi_1$ are also polynomials in $\varphi$.
