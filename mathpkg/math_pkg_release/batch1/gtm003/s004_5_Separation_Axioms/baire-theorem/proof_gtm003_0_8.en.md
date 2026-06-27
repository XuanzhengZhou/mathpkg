---
role: proof
locale: en
of_concept: baire-theorem
source_book: gtm003
source_chapter: "0"
source_section: "8"
---

The text mentions Baire's theorem without proof. Note: the standard Baire theorem holds for complete metric spaces (or locally compact Hausdorff spaces). The version stated here (every metrizable space is Baire) is actually false in general metrizable spaces — a counterexample is $\mathbb{Q}$ with its usual metric. The intended statement is almost certainly: "Every completely metrizable space is a Baire space." The standard proof: Let $\{U_n\}$ be a sequence of dense open sets and $W$ any nonempty open set. Since $U_1$ is dense, $W \cap U_1 \neq \varnothing$; pick $x_1$ and a ball $B_1$ of radius $\leq 1$ with $\overline{B}_1 \subset W \cap U_1$. Iteratively, since $U_{n+1}$ is dense, $B_n \cap U_{n+1} \neq \varnothing$; pick $x_{n+1}$ and $B_{n+1}$ of radius $\leq 1/(n+1)$ with $\overline{B}_{n+1} \subset B_n \cap U_{n+1}$. The centers $\{x_n\}$ form a Cauchy sequence; by completeness, $x_n \to x$. Then $x \in \bigcap \overline{B}_n \subset W \cap \bigcap U_n$, so $\bigcap U_n$ meets every nonempty open set $W$.
