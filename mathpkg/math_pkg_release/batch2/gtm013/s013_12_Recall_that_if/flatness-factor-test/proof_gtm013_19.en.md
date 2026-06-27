---
role: proof
locale: en
of_concept: flatness-factor-test
source_book: gtm013
source_chapter: "5"
source_section: "19"
---

Consider the commutative diagram with exact rows obtained by tensoring the exact sequence $0 \to K \to V \to V \to 0$ with a left ideal $I$:
$$K \otimes_R I \to V \otimes_R I \to V \otimes_R I \to 0$$
$$\downarrow \quad\quad \downarrow \quad\quad \downarrow$$
$$K \to V \to V \to 0$$
Since $V$ is flat, the middle vertical map $V \otimes_R I \to V$ (identified with $V \otimes_R R$) is monic, with image $VI$. The map $K \otimes_R I \to K$ has image $KI$. By the Flat Test Lemma, $V$ is flat iff $V \otimes_R I \to V$ is monic for all $I$. A diagram chase shows this holds iff the image of $K \otimes_R I$ in $V$ equals $K \cap VI$, i.e., $KI = K \cap VI$.
