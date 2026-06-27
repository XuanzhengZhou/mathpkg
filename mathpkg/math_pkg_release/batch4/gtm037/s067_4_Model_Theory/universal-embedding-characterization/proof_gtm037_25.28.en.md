---
role: proof
locale: en
of_concept: universal-embedding-characterization
source_book: gtm037
source_chapter: "25"
source_section: "25.28"
---
The proof of Theorem 25.28 appears in the surrounding text of Chapter 25 of Monk's *Mathematical Logic*. The direction (1) $\Rightarrow$ (2) follows from the fact that universal sentences are preserved under substructures: if $\mathfrak{A}$ embeds into $\mathfrak{B} \upharpoonright \mathcal{L}$ and $\mathfrak{B} \models \Gamma$, then $\mathfrak{B} \models \varphi$ for any $\varphi$ with $\Gamma \models \varphi$, and since $\varphi$ is universal, its truth transfers down to the embedded copy of $\mathfrak{A}$, hence $\mathfrak{A} \models \varphi$.

The converse direction (2) $\Rightarrow$ (1) is the nontrivial part. It uses the method of diagrams and compactness: one forms the $\mathcal{L}'$-diagram of $\mathfrak{A}$ enriched with constants for elements of the domain, together with $\Gamma$, and shows that if no embedding exists, a universal sentence witnessing this can be extracted, contradicting condition (2). The proof generalizes the technique used in the characterization of universal classes (Theorem 25.5 and subsequent results in the chapter).
