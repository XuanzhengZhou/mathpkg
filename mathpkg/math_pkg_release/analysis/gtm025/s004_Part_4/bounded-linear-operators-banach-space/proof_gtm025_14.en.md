---
role: proof
locale: en
of_concept: bounded-linear-operators-banach-space
source_book: gtm025
source_chapter: "4"
source_section: "14"
---

We prove only completeness. Let $(T_n)$ be Cauchy in $\mathfrak{B}(A, B)$. For each $x \in A$, $\|T_n(x) - T_m(x)\| \le \|T_n - T_m\| \cdot \|x\|$, so $(T_n(x))$ is Cauchy in $B$ and converges to some $T(x)$. Linearity of the pointwise limit $T$ follows from continuity of vector operations. Boundedness: since $(T_n)$ is Cauchy, $\|T_n\| \le \beta$ for some $\beta$. For $\|x\| \le 1$, $\|T(x)\| \le \|T(x) - T_n(x)\| + \|T_n(x)\| \le \|T(x) - T_n(x)\| + \beta$. Taking $n \to \infty$ gives $\|T(x)\| \le \beta$, so $T$ is bounded. Finally, $\|T - T_n\| \to 0$ because for $\|x\| \le 1$ and large $m,n$, $\|T(x) - T_n(x)\| \le \|T(x) - T_m(x)\| + \|T_m - T_n\| \to \|T_m - T_n\| < \varepsilon$.
