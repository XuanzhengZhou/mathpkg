---
role: proof
locale: en
of_concept: finite-dimensional-hausdorff-tvs-isomorphism
source_book: gtm003
source_chapter: "I. Topological Vector Spaces"
source_section: "3.2"
---

**Proof.** By induction on $n = \dim L$. For $n = 1$, this is Theorem (3.1). Assume the statement holds for dimension $n-1$. Let $M$ and $N$ be subspaces of $L$ with bases $\{x_1, \ldots, x_{n-1}\}$ and $\{x_n\}$, respectively. By the induction hypothesis, $M$ is isomorphic to $K_0^{n-1}$. Since $K_0$ is complete, $M$ is complete and, since $L$ is Hausdorff, $M$ is closed in $L$. By (2.3), $L/M$ is Hausdorff and clearly of dimension 1; hence the map $v$, ordering to each equivalence class mod $M$ its unique representative in $N$, is an isomorphism by (3.1). It follows from (2.4) that $L = M \oplus N$, which means that $(\lambda_1, \ldots, \lambda_n) \mapsto \lambda_1 x_1 + \cdots + \lambda_n x_n$ is an isomorphism of $K_0^{n-1} \times K_0 = K_0^n$ onto $L$. Finally, it is obvious that every isomorphism of $K_0^n$ onto $L$ is of this form.
