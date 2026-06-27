---
role: proof
locale: en
of_concept: measurability-of-sections-of-measurable-functions
source_book: gtm018
source_chapter: "VII. Product Spaces"
source_section: "34. Sections"
---

Let $f$ be a measurable function on $X \times Y$, let $x$ be a point of $X$, and let $M$ be any Borel set on the real line. We must show that $N(f_x) \cap f_x^{-1}(M)$ is measurable. Observe that

$$f_x^{-1}(M) = \{ y : f_x(y) \in M \} = \{ y : f(x,y) \in M \} = \{ y : (x,y) \in f^{-1}(M) \} = (f^{-1}(M))_x.$$

Since $f$ is measurable, $f^{-1}(M)$ is a measurable set in $X \times Y$. By Theorem A, its section $(f^{-1}(M))_x$ is measurable in $Y$. Similarly, $N(f_x) = (N(f))_x$ is measurable by Theorem A. Therefore $N(f_x) \cap f_x^{-1}(M)$ is measurable as the intersection of two measurable sets. This proves that the $X$-section $f_x$ is measurable. The proof for an arbitrary $Y$-section of $f$ is entirely similar.
