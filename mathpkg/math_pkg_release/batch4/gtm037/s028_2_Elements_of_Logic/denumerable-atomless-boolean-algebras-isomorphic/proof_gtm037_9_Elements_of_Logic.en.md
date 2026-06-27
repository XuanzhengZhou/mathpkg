---
role: proof
locale: en
of_concept: denumerable-atomless-boolean-algebras-isomorphic
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

Let $R = \{(\mathfrak{A}, \mathfrak{B}) : |A| = |B| = 1 \text{ or } \mathfrak{A} \text{ and } \mathfrak{B} \text{ are denumerable and atomless}\}$. Let $\mathfrak{A}$ and $\mathfrak{B}$ be denumerable atomless Boolean algebras. Then $(\mathfrak{A}, \mathfrak{B}) \in R$ by definition. The hypothesis of Theorem 9.47 must be verified for this relation $R$:

(i) If $(\mathfrak{A}, \mathfrak{B}) \in R$ and $A$ is finite, then $|A| = |B| = 1$, so $\mathfrak{A} \cong \mathfrak{B}$.

(ii) If $(\mathfrak{A}, \mathfrak{B}) \in R$ and $\mathfrak{A}, \mathfrak{B}$ are denumerable and atomless (the infinite case), then for any $a \in A$ there exists $b \in B$ such that $(\mathfrak{A} \upharpoonright a, \mathfrak{B} \upharpoonright b) \in R$ and $(\mathfrak{A} \upharpoonright -a, \mathfrak{B} \upharpoonright -b) \in R$. Since $\mathfrak{A}$ is atomless and denumerable, the relativized algebras $\mathfrak{A} \upharpoonright a$ and $\mathfrak{A} \upharpoonright -a$ are also either trivial or denumerable and atomless, and similarly for $\mathfrak{B}$. The back-and-forth construction of Theorem 9.47 then produces the desired isomorphism.
