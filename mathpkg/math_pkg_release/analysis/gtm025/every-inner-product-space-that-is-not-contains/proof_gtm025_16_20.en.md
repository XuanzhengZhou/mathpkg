---
role: proof
locale: en
of_concept: "every-inner-product-space-that-is-not-contains"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.20"
---

We use Tukey's lemma (3.8). Let $A$ be any nonvoid orthonormal subset of $H$; for example, $A = \{\|x\|^{-1}x\}$ where $x \neq 0, x \in H$. Next let $\mathcal{F} = \{B : B \subset H, A \cup B\}$ is an orthonormal set. To test orthonormality one tests only two vectors at a time, and so it is clear that $\mathcal{F}$ is of finite character. Also $A \in \mathcal{F}$, so that $\mathcal{F}$ is nonvoid. By Tukey's lemma, $\mathcal{F}$ has a maximal member $E$. It is obvious that $E \supset A$. We assert that $E$ is complete. Assume that $y \neq 0$ and that $y \perp E$. Set $z = \|y\|^{-1}y$. Then $E \cup \{z\} \in \mathcal{F}$ and $E \subseteq E \cup \{z\}$. This contradicts the maximality of $E$. Thus $y \perp E$ implies $y = 0$.

The above proof is not constructive; it gives no clue as to how to construct a complete orthonormal set in any given inner product space. There are methods of actually constructing complete orthonormal sets provided that they are not too large. We now take up this construction.
