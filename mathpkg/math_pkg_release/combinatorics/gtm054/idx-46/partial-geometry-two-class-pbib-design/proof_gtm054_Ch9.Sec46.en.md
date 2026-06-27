---
role: proof
locale: en
of_concept: partial-geometry-two-class-pbib-design
source_book: gtm054
source_chapter: "IX"
source_section: "46"
---

From F1 it is immediate that $\lambda_1 = 1$ (any two collinear points lie on exactly one line) and $\lambda_2 = 0$ (non-collinear points share no common line).

Each point $x \in V$ is incident with exactly $r$ lines, each of which contains exactly $k - 1$ points other than $x$. Thus each point has precisely $n_1 = r(k - 1)$ first associates.

Substituting this value and the value of $v$ from F5(d) into the identity $n_2 = v - n_1 - 1$ (cf. E1) yields
$$n_2 = \frac{(k - t)(k - 1)(r - 1)}{t}.$$

If $x$ and $y$ are first associates, the unique line $L$ through them contains $k - 2$ other points, each of which is a first associate of both $x$ and $y$, giving $(k - 2)$ common first associates from $L$. Additionally, through $x$ there are $r - 1$ lines other than $L$, and through $y$ there are $r - 1$ lines other than $L$. For each such line through $x$ not equal to $L$, and each such line through $y$, by F2 with parameter $t$, there are $(t - 1)$ lines through $x$ meeting that line (excluding $L$ itself). Counting yields $p_{11}^1 = (t - 1)(r - 1) + k - 2$.

For $p_{11}^2$, if $x$ and $y$ are second associates, each of the $r$ lines through $x$ meets each of the $r$ lines through $y$ in at most one point. By F2, for any point $z$ collinear with both $x$ and $y$, the lines through $x$ and $y$ meeting at $z$ correspond to the $t$ parameter, giving $p_{11}^2 = rt$.
