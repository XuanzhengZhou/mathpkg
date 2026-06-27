---
role: proof
locale: en
of_concept: measurable-group-covering
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

By Theorem D, $A^{-1}$ and $B^{-1}$ are measurable sets of positive measure. Applying Theorem D further, the set $x^{-1}A \cap B^{-1}$ is measurable. Since $\mu$ is not identically zero and is $\sigma$-finite, and $A$ has positive measure, there exists at least one $x$ such that $\mu(x^{-1}A \cap B^{-1}) > 0$ (this follows from the Fubini-type argument using the transformation $Q$ and the fact that $\mu \times \mu(Q(A \times B)) = \mu(A)\mu(B) > 0$).

Choose $x_1$ such that $C_1 = x_1^{-1}A \cap B$ has positive measure (note: we use $B$ rather than $B^{-1}$; the argument is symmetric). Then $x_1 C_1 = x_1(x_1^{-1}A \cap B) \subset A$, and $C_1 \subset B$. Setting $y_1 = e$ gives $y_1 C_1 = C_1 \subset B$, so the conclusion holds with $x = x_1$, $y = e$, and $C = C_1$.

For the general case with arbitrary $y$, apply the result to $A^{-1}$ and $B^{-1}$: there exist $x_0, y_0$ and $C_0$ of positive measure such that $x_0 C_0 \subset A^{-1}$ and $y_0 C_0 \subset B^{-1}$. Setting $C_2 = C_0^{-1}$, $x_2 = x_0^{-1}$, $y_2 = y_0^{-1}$, we obtain $x_2 C_2 \subset A$ and $y_2 C_2 \subset B$.
