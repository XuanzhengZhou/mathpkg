---
role: proof
locale: en
of_concept: classification-of-principal-g-bundles-over-cw-complexes
source_book: gtm020
source_chapter: "4"
source_section: "13"
---

First, we prove that $\phi_\omega(B)$ is surjective. Let $\xi$ be a locally trivial principal $G$-bundle over $B$. By Theorem 2 (7.1) under hypothesis (H1), the fibre bundle $\xi[X_0]$ has a cross section. By Theorem (8.2) we have a principal bundle morphism $(u, f): \xi \rightarrow \omega$, and by Theorem (4.2) we have $\{\xi\} = \{f^*(\omega)\} = \phi_\omega(B)([f])$.

Second, we prove that $\phi_\omega(B)$ is injective. Let $f, g: B \rightarrow B_0$ be maps such that $\{f^*(\omega)\} = \{g^*(\omega)\}$. By (8.2) the fibre bundle $(f^*(\omega) \times I)[X_0]$ has a cross section $s$ over $B \times \{0, 1\}$, resulting from the principal bundle morphisms which are the compositions of $(f^*(\omega) \times I)|(B \times 0) \rightarrow f^*(\omega) \rightarrow \omega$ and $(f^*(\omega) \times I)|(B \times 1) \rightarrow g^*(\omega) \rightarrow \omega$. By Theorem 2 (7.1) under hypothesis (H1), this cross section $s$ prolongs to a cross section $s^*$ of $(f^*(\omega) \times I)[X_0]$ over $B \times I$. By (8.2), we have a principal bundle morphism $(w, h): f^*(\omega) \times I \rightarrow \omega$, where $h: B \times I \rightarrow B_0$ provides the required homotopy between $f$ and $g$.
