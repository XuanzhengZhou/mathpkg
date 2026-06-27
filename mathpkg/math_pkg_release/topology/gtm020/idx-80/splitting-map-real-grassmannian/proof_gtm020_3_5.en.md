---
role: proof
locale: en
of_concept: splitting-map-real-grassmannian
source_book: gtm020
source_chapter: "3"
source_section: "5"
---

The proof parallels that of Proposition 3.1, replacing $CP^\infty$ with $RP^\infty$ and working with $\mathbb{Z}_2$ coefficients throughout. Since $h_n^*(\gamma_n)$ is isomorphic to $\gamma \times \dots \times \gamma$, it suffices to show that $h_n^*$ is a monomorphism on $\mathbb{Z}_2$ cohomology. For any splitting map $f: X \rightarrow G_n(R^\infty)$ of $\gamma_n$ with $f^*(\gamma_n) = \lambda_1 \oplus \dots \oplus \lambda_n$, each line bundle $\lambda_i$ is classified by $g_i: X \rightarrow RP^\infty$ with $\lambda_i \cong g_i^*(\gamma)$. Then $g = (g_1, \dots, g_n)$ satisfies $f^*(\gamma_n) \cong g^*(\gamma \times \dots \times \gamma)$, so $f$ and $h_n \circ g$ are homotopic by the classifying property. Hence $f^* = g^* \circ h_n^*$, and since $f^*$ is a monomorphism, $h_n^*$ is also a monomorphism.
