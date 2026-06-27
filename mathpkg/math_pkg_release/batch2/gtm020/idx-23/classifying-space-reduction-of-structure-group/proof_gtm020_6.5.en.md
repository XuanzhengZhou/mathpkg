---
role: proof
locale: en
of_concept: classifying-space-reduction-of-structure-group
source_book: gtm020
source_chapter: "6"
source_section: "5"
---

Let $\eta$ be a restriction of $\xi$. Then there is a unique homotopy class determined by a map $g: B \rightarrow B_H$ such that $g^*(\omega_H)$ and $\eta$ are isomorphic. Consequently, $\eta[G]$ and $g^*(\omega_H[G])$ are isomorphic. From the above discussion we know that $\eta[G]$ is $B$-isomorphic to $g^*(f_0^*(\omega_G))$, and $\xi$ is $B$-isomorphic to $f^*(\omega_G)$. Since, by Corollary (3.2), $\eta[G]$ is $B$-isomorphic to $\xi$, we have
$$
g^*(f_0^*(\omega_G)) \cong f^*(\omega_G)
$$
as bundles over $B$. By the classification theorem, this implies that $f_0 \circ g$ is homotopic to $f$.

Conversely, given a map $g: B \rightarrow B_H$ such that $f_0 \circ g \simeq f$, we have $g^*(f_0^*(\omega_G)) \cong f^*(\omega_G) \cong \xi$. But $g^*(f_0^*(\omega_G)) \cong g^*(\omega_H[G])$, and $g^*(\omega_H)$ is a principal $H$-bundle $\eta$ over $B$. By Corollary (3.2), $\eta[G] \cong g^*(\omega_H[G]) \cong \xi$, and thus $\eta$ is a restriction of $\xi$.

This establishes the bijective correspondence between restrictions of $\xi$ and homotopy classes of maps $g: B \rightarrow B_H$ with $f_0 \circ g \simeq f$.
