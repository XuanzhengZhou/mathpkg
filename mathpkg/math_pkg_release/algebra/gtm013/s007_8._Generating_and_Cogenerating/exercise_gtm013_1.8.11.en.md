---
role: exercise
locale: en
chapter: "1"
section: "8"
exercise_number: 11
---

An indexed set $(x_\alpha)_{\alpha \in A}$ of elements of a module is **linearly independent** in case for every finite sequence $\alpha_1, \ldots, \alpha_n$ of distinct elements of $A$ and every $r_1, \ldots, r_n \in R$

$$r_1 x_{\alpha_1} + \cdots + r_n x_{\alpha_n} = 0 \quad \text{implies} \quad r_1 = \cdots = r_n = 0.$$

An $R$-module $F$ with a linearly independent spanning set $(x_\alpha)_{\alpha \in A}$ is called a **free $R$-module** (of rank $\mathrm{card}\, A$) with free basis $(x_\alpha)_{\alpha \in A}$.

(1) Let $(x_\alpha)_{\alpha \in A}$ be an indexed set in a left $R$-module $F$. For each $\alpha$ let $\rho_\alpha: R \to F$ be the right multiplication $r \mapsto r x_\alpha$. Prove that these maps determine an epimorphism $R^{(A)} \to F$ which is an isomorphism iff $(x_\alpha)_{\alpha \in A}$ is a free basis for $F$.
