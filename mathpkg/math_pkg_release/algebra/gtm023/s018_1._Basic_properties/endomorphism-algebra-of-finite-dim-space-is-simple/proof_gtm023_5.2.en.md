---
role: proof
locale: en
of_concept: endomorphism-algebra-of-finite-dim-space-is-simple
source_book: gtm023
source_chapter: "5"
source_section: "§2. Ideals"
---

Let $I$ be a nonzero ideal in $A(E; E)$ and let $\varphi \neq 0$ be an element of $I$. Choose $a \in E$ with $\varphi a \neq 0$. Let $e_1, \ldots, e_n$ be a basis of $E$. Define $\varphi_i$ by $\varphi_i e_k = \delta_k^i a$, and choose $\psi_i$ such that $\psi_i \varphi a = e_i$. Then for any $\psi \in A(E; E)$ with matrix $\alpha_i^j$ relative to the basis $e_i$,

$$
\psi e_k = \sum_j \alpha_k^j e_j = \sum_j \alpha_k^j \psi_j \varphi a = \left(\sum_{i,j} \alpha_i^j \psi_j \varphi \varphi_i\right) e_k,
$$

so $\psi = \sum_{i,j} \alpha_i^j \psi_j \varphi \varphi_i \in I$. Hence $I = A(E; E)$. Since $A(E; E)^2 \neq 0$, it is simple.
