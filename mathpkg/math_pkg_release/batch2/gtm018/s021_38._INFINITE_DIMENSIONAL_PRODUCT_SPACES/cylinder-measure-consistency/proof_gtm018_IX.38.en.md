---
role: proof
locale: en
of_concept: cylinder-measure-consistency
source_book: gtm018
source_chapter: "IX"
source_section: "38. Infinite Dimensional Product Spaces"
---

Suppose $E$ is a non-empty measurable subset of $X$ that is simultaneously a $\{1,\dots,m\}$-cylinder and a $\{1,\dots,n\}$-cylinder with $m < n$. By Theorem A, there exist measurable sets $A \subset X_1 \times \cdots \times X_m$ and $B \subset X_1 \times \cdots \times X_n$ such that

$$E = A \times X^{(m)} \quad\text{and}\quad E = B \times X^{(n)}.$$

Rewrite the first relation as

$$E = (A \times X_{m+1} \times \cdots \times X_n) \times X^{(n)}.$$

Since $E = B \times X^{(n)}$ as well, and both are $\{1,\dots,n\}$-cylinders, it follows from Theorem A (more precisely from the representation being unique, which follows from 33.C) that

$$B = A \times X_{m+1} \times \cdots \times X_n.$$

Now, since $E$ is measurable, both $A$ and $B$ are measurable in their respective finite product spaces. Using the finite product measure property,

$$(\mu_1 \times \cdots \times \mu_n)(B) = (\mu_1 \times \cdots \times \mu_n)(A \times X_{m+1} \times \cdots \times X_n).$$

By the definition of finite product measure and the normalization $\mu_i(X_i) = 1$ for all $i$,

$$(\mu_1 \times \cdots \times \mu_n)(A \times X_{m+1} \times \cdots \times X_n) = (\mu_1 \times \cdots \times \mu_m)(A) \cdot \mu_{m+1}(X_{m+1}) \cdots \mu_n(X_n) = (\mu_1 \times \cdots \times \mu_m)(A).$$

Thus $(\mu_1 \times \cdots \times \mu_m)(A) = (\mu_1 \times \cdots \times \mu_n)(B)$. This shows the value is independent of the representation, so that $\mu(A \times X^{(n)}) := (\mu_1 \times \cdots \times \mu_n)(A)$ is well-defined on the algebra $\mathbf{F}$ of all finite-dimensional measurable cylinders.
