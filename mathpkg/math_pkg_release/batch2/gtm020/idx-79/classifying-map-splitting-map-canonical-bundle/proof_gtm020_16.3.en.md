---
role: proof
locale: en
of_concept: classifying-map-splitting-map-canonical-bundle
source_book: gtm020
source_chapter: "16"
source_section: "3"
---

Since $h_n^*(\gamma_n)$ is isomorphic to $\gamma \times \dots \times \gamma$, it suffices to show that $h_n^*: H^*(G_n(C^\infty)) \rightarrow H^*(CP^\infty \times \dots \times CP^\infty)$ is a monomorphism.

For this, let $f: X \rightarrow G_n(C^\infty)$ be any splitting map of $\gamma_n$, where $f^*(\gamma_n) = \lambda_1 \oplus \dots \oplus \lambda_n$. Let $g_i: X \rightarrow CP^\infty$ be a classifying map for $\lambda_i$, where $\lambda_i$ is isomorphic to $g_i^*(\gamma)$. Then for $g = (g_1, \dots, g_n)$ the bundle $\lambda_1 \oplus \dots \oplus \lambda_n$ is isomorphic to $g^*(\gamma \times \dots \times \gamma)$. Therefore, by 3(6.2) the maps $f$ and $h_n g$ are homotopic. Then as morphisms of cohomology we have $f^* = (h_n g)^* = g^*h_n^*$. Since $f^*$ is a monomorphism, $h_n^*$ is a monomorphism.
