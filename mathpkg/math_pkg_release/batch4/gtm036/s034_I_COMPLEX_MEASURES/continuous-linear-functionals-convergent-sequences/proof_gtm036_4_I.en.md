---
role: proof
locale: en
of_concept: continuous-linear-functionals-convergent-sequences
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
The space $c_0(X)$ is a closed hyperplane in $C(Y)$ under the uniform norm, where $Y = X \cup \{\infty\}$ is the one-point compactification. When $X$ is the set of positive integers, $C(Y)$ is denoted by $c$, the space of all convergent sequences.

For a discrete space $X$, every regular Borel measure $\mu$ is atomic, with $\mu(A) = \sum_{x \in A} g(x)$ for some function $g$. Applying the Riesz representation theorem of part (b), the adjoint of $c_0(X)$ is $l^1(X)$ and the adjoint of $c(Y)$ is $l^1(Y)$.

For $c$ specifically, $Y = \mathbb{N} \cup \{\infty\}$ and we identify $g \in l^1(Y)$ with the sequence $\{y_n\}_{n=0}^\infty$ where $y_0 = g(\infty)$ and $y_n = g(n)$ for $n \geq 1$. The functional is then
$$\phi(\{x_n\}) = \sum_{n=1}^\infty x_n y_n + (\lim_{n\to\infty} x_n) y_0,$$
with $\|\phi\| = \sum_{n=0}^\infty |y_n|$.
