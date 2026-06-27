---
role: proof
locale: en
of_concept: runges-theorem
source_book: gtm055
source_chapter: "18"
source_section: "20"
---

If $U = \mathbb{C}$ then $P = \{\infty\}$, $f$ is entire, and the partial sums of any power series expansion of $f$ may be used. Otherwise, for each positive integer $n$ let $D_n^- = \{\lambda \in \mathbb{C}: |\lambda| \leq n\}$ and set
$$K_n = \left\{ \lambda \in D_n^- : d(\lambda, \mathbb{C} \setminus U) \geq \frac{1}{n} \right\}.$$

Then $\{K_n\}$ is an increasing sequence of compact subsets of $U$ with $K_n \subset K_{n+1}^\circ$ and $U = \bigcup_{n=1}^{\infty} K_n$. For any compact $K \subset U$, there exists $n$ with $K \subset K_n$. By Proposition 18.14, for each $n$ there exists a rational function $r_n$ with poles in $P$ approximating $f$ to within $1/n$ on $K_n$. The sequence $\{r_n\}$ converges to $f$ uniformly on each compact subset of $U$.

When $U$ is simply connected, $\hat{\mathbb{C}} \setminus U$ is connected, and we may take $P = \{\infty\}$, obtaining polynomial approximation — the special case also known as Runge's theorem for simply connected domains.
