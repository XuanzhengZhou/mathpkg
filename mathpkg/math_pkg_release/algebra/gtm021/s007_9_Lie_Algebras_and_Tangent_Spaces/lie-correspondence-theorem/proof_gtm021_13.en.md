---
role: proof
locale: en
of_concept: lie-correspondence-theorem
source_book: gtm021
source_chapter: "13"
source_section: "Correspondence Between Groups and Lie Algebras"
---
The proof relies on two key facts that hold in characteristic 0:

(1) Separability of morphisms: Whenever $\varphi: G \to G'$ is a morphism of algebraic groups, $\operatorname{Ker} d\varphi = \mathcal{L}(\operatorname{Ker} \varphi)$. This follows from the general theory of separable morphisms in characteristic 0.

(2) Intersections: Theorem 12.5 (which holds in characteristic 0 using separability of certain quotient morphisms) affirms that if $A, B$ are closed subgroups of $G$, then $\mathcal{L}(A \cap B) = \mathfrak{a} \cap \mathfrak{b}$.

Now to prove injectivity of $H \mapsto \mathfrak{h}$: Suppose $H_1, H_2$ are closed connected subgroups with $\mathfrak{h}_1 = \mathfrak{h}_2$. Consider $H = H_1 \cap H_2$. By (2), $\mathfrak{h} = \mathfrak{h}_1 \cap \mathfrak{h}_2 = \mathfrak{h}_1 = \mathfrak{h}_2$. But $H \subset H_1$ and $\dim H = \dim \mathfrak{h} = \dim \mathfrak{h}_1 = \dim H_1$. Since both are connected, $H = H_1$. Similarly $H = H_2$, so $H_1 = H_2$.

If $H_1 \subset H_2$, then $H_1 \subset H_2 \cap H_1$, so $\mathfrak{h}_1 \subset \mathfrak{h}_2 \cap \mathfrak{h}_1 = \mathfrak{h}_2$, and conversely, if $\mathfrak{h}_1 \subset \mathfrak{h}_2$, then considering $H_1 \cap H_2$ and using the same dimension argument gives $H_1 \subset H_2$.
