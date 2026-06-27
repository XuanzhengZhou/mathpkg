---
role: proof
locale: en
of_concept: density-mapping-properties
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

**(1)** This is exactly the Lebesgue Density Theorem (Theorem 3.20): $m(A \triangle \phi(A)) = 0$, i.e., $\phi(A) \sim A$.

**(2)** If $A \sim B$, then $m(A \triangle B) = 0$. For any interval $I$,

$$
m(I \cap A) - m(I \cap B) \leq m((I \cap A) \triangle (I \cap B)) \leq m(A \triangle B) = 0,
$$

hence $m(I \cap A) = m(I \cap B)$ for all intervals $I$. Therefore the densities of $A$ and $B$ coincide at every point, so $\phi(A) = \phi(B)$.

**(3)** The density of $\emptyset$ at every point is $0$, so $\phi(\emptyset) = \emptyset$. The density of $\mathbb{R}$ at every point is $1$, so $\phi(\mathbb{R}) = \mathbb{R}$.

**(4)** For any interval $I$, we have $I - (A \cap B) = (I - A) \cup (I - B)$. Hence

$$
m(I) - m(I \cap A \cap B) \leq m(I) - m(I \cap A) + m(I) - m(I \cap B).
$$

Rearranging,

$$
\frac{m(I \cap A)}{|I|} + \frac{m(I \cap B)}{|I|} - 1 \leq \frac{m(I \cap A \cap B)}{|I|}.
$$

Take $I = [x - h, x + h]$ and let $h \to 0$. If $x \in \phi(A) \cap \phi(B)$, then the left-hand side tends to $1 + 1 - 1 = 1$, forcing the density of $A \cap B$ at $x$ to be $1$. Thus $\phi(A) \cap \phi(B) \subset \phi(A \cap B)$. The opposite inclusion $\phi(A \cap B) \subset \phi(A) \cap \phi(B)$ follows from the fact that $A \cap B \subset A$ and $A \cap B \subset B$ together with property (5).

**(5)** This is an immediate consequence of property (4), since $A \subset B$ implies $A \cap B = A$, and therefore $\phi(A) = \phi(A \cap B) = \phi(A) \cap \phi(B) \subset \phi(B)$.
