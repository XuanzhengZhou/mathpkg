---
locale: en
of_concept: let-f-u-rightarrow-v-be-a-diffeomorphism-between-two-open-co
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '3'
---

By translations, we can assume that $f(0) = 0 = x$. Let $f(x) = Lx + g(x)$, where $Lx$ is linear and $D(g)(0) = 0$, $g(0) = 0$. As maps defined $(U, U - 0) \rightarrow (\mathbf{R}^n, \mathbf{R}^n - 0)$, there is a homotopy $h_t(x) = Lx + (1 - t)g(x)$, where $h_0(x) = f(x)$ and $h_1(x) = Lx$. We have reduced the problem to the case where $f: U \rightarrow V$ is linear.

By a second homotopy we can change $f$ into an orthogonal transformation. Then $f = r_1 \cdots r_q$ is a reflection through an $(n - 1)$-subspace of $\mathbf{R}^n$. Then $(r_i)_*(\alpha_0) = -\alpha_0, (r_i)^*(\beta_0) = -\beta_0$, and $O(r_i) = -1$. By the rule for composition, we have $f_*(\alpha_0) = O(f)\alpha_0$ and $f^*(\beta_0) = O(f)\beta_0$. This proves the theorem.

This theorem allows extension of the notion of orientation to topological maps.
