---
role: proof
locale: en
of_concept: rank-nullity-theorem
source_book: gtm031
source_chapter: "III"
source_section: "9"
---

Let $(z_1, z_2, \dots, z_\nu)$ be a basis for the null space $\mathfrak{N}$. We can supplement this basis by $n_1 - \nu$ vectors $x_i$ to obtain the basis
$$
(x_1, \dots, x_{n_1 - \nu}; z_1, z_2, \dots, z_\nu)
$$
for $\mathfrak{R}_1$. The vectors
$$
x_1 A, x_2 A, \dots, x_{n_1 - \nu} A, z_1 A, \dots, z_\nu A
$$
are generators for the rank space $\mathfrak{R}_1 A \subseteq \mathfrak{R}_2$. Since $z_i A = 0$, the vectors $x_1 A, \dots, x_{n_1 - \nu} A$ are also generators for $\mathfrak{R}_1 A$.

We now show these vectors are linearly independent. Suppose
$$
\beta_1 (x_1 A) + \beta_2 (x_2 A) + \cdots + \beta_{n_1 - \nu} (x_{n_1 - \nu} A) = 0.
$$
Then $(\sum \beta_i x_i)A = 0$, so $\sum \beta_i x_i \in \mathfrak{N} = [z_1, z_2, \dots, z_\nu]$. Since the set $(x_1, \dots, x_{n_1 - \nu}, z_1, \dots, z_\nu)$ is linearly independent, this implies that all $\beta_i = 0$.

Hence if we set $y_i = x_i A$, then $(y_1, y_2, \dots, y_{n_1 - \nu})$ is a basis for $\mathfrak{R}_1 A$. Thus
$$
\dim \mathfrak{R}_1 A = n_1 - \nu = n_1 - \operatorname{nullity}(A),
$$
which proves the theorem.
