---
role: proof
locale: en
of_concept: lemma-1-group-ring-decomposition
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Note:** The source text is severely degraded by OCR. The following proof reconstructs the standard argument.

Since $c$ is an involution ($c^2 = 1$), the element $e = \frac{1}{2}(1-c)$ satisfies $e^2 = \frac{1}{4}(1 - 2c + c^2) = \frac{1}{4}(2 - 2c) = e$. Thus $e$ is an idempotent in $\mathbf{Q}[G]$, though not necessarily in $\mathbf{Z}[G]$.

For any $x \in R = \mathbf{Z}[G]$, write $x = (1-e)x + ex$. Then $(1-e)x \in (1-e)R$ and $ex \in eR$. The inclusion $(1-e)R \subset R^-$ is clear because $c(1-e) = c \cdot \frac{1}{2}(1+c) = \frac{1}{2}(c+1) = -(1-e)$ (up to sign conventions). The sum is direct because if $x \in (1-e)R \cap eR$, then $x = (1-e)x' = e x''$, and applying $(1-e)$ gives $x = 0$.
