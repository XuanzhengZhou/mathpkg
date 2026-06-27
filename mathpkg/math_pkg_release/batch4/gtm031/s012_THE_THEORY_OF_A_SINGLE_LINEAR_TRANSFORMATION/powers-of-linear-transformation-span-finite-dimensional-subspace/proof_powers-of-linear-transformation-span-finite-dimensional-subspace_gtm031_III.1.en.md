---
role: proof
locale: en
of_concept: powers-of-linear-transformation-span-finite-dimensional-subspace
source_book: gtm031
source_chapter: "III"
source_section: "1"
---

If $A$ is not a scalar multiple of $1$, then $(1, A)$ is linearly independent. If $A^2$ is not linearly dependent on $(1, A)$, then $(1, A, A^2)$ is independent. Continuing this process yields the nested sequence of independent sets $(1), (1, A), (1, A, A^2), (1, A, A^2, A^3), \dots$.

Since $\mathfrak{L}$ is finite-dimensional (dimension $n^2$), this process must terminate after finitely many steps. Termination occurs at the first power $A^m$ that is linearly dependent on the preceding powers $1, A, \dots, A^{m-1}$. Thus $(1, A, \dots, A^{m-1})$ is linearly independent, and we have
$$A^m = \mu_0 1 + \mu_1 A + \cdots + \mu_{m-1} A^{m-1}$$
with $\mu_i \in \Phi$.

Multiplying by $A$ and using the algebra condition $\gamma(AB) = (\gamma A)B = A(\gamma B)$ yields
$$A^{m+1} = \mu_0 A + \mu_1 A^2 + \cdots + \mu_{m-1} A^m.$$
Since $A^m \in [1, A, \dots, A^{m-1}]$, the right-hand side lies in $[1, A, \dots, A^{m-1}]$, so $A^{m+1} \in [1, A, \dots, A^{m-1}]$. By induction, $A^{m+k} \in [1, A, \dots, A^{m-1}]$ for all $k \ge 0$.
