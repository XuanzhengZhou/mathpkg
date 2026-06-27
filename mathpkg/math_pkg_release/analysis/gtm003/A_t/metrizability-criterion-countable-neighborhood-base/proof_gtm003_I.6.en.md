---
role: proof
locale: en
of_concept: metrizability-criterion-countable-neighborhood-base
source_book: gtm003
source_chapter: "I"
source_section: "6"
---

If $L$ is metrizable, the balls of radius $1/n$ centered at $0$ form a countable neighbourhood base of the origin. Conversely, suppose $L$ possesses a countable neighbourhood base $\{U_n : n \in \mathbb{N}\}$ of $0$. Let $\{V_n : n \in \mathbb{N}\}$ be a neighbourhood base of $0$ consisting of circled sets and satisfying $V_{n+1} + V_{n+1} \subset V_n$ for all $n \in \mathbb{N}$; such a base exists by (1.2). By (1) of the main text, the following implications hold by induction on the number of elements of a non-empty finite subset $H$ of $\mathbb{N}$:

$$p_H < 2^{-n} \;\Rightarrow\; n < H \;\Rightarrow\; V_H \subset V_n,$$

where $n < H$ means that $n < k$ for all $k \in H$, and $p_H = \sum_{k \in H} 2^{-k}$, $V_H = \sum_{k \in H} V_k$.

Define the real-valued function $x \mapsto |x|$ on $L$ by $|x| = 1$ if $x$ is not contained in any $V_H$, and by

$$|x| = \inf_H \{ p_H : x \in V_H \}$$

otherwise; the range of this function is contained in the real unit interval. Since each $V_H$ is circled, condition (i) is satisfied.

To verify the triangle inequality (ii), it is evident for each pair $(x, y)$ such that $|x| + |y| \geq 1$. Hence suppose $|x| + |y| < 1$. Let $\varepsilon > 0$ be such that $|x| + |y| + 2\varepsilon < 1$; there exist non-empty finite subsets $H, K$ of $\mathbb{N}$ such that $x \in V_H$, $y \in V_K$ and $p_H < |x| + \varepsilon$, $p_K < |y| + \varepsilon$. Since $p_H + p_K < 1$, there exists a unique finite subset $M$ of $\mathbb{N}$ for which $p_M = p_H + p_K$; by the property that $V_H + V_K \subset V_M$, it follows that $x + y \in V_M$ and hence

$$|x + y| \leq p_M = p_H + p_K < |x| + |y| + 2\varepsilon,$$

which proves (ii).

For any $\varepsilon > 0$, let $S_\varepsilon = \{ x \in L : |x| \leq \varepsilon \}$. One shows that

$$S_{2^{-n-1}} \subset V_n \subset S_{2^{-n}} \quad (n \in \mathbb{N}).$$

The inclusion $V_n \subset S_{2^{-n}}$ follows directly from the definition of $|x|$, since $x \in V_n$ implies $x \in V_{\{n\}}$ with $p_{\{n\}} = 2^{-n}$. For the reverse inclusion, if $|x| \leq 2^{-n-1}$, then there exists a finite subset $H$ with $p_H < 2^{-n}$ and $x \in V_H$, whence $x \in V_n$. This establishes (iii) and shows that the sets $S_\varepsilon$ form a neighbourhood base of $0$, proving (iv). Condition (iii) is verified since $|x| = 0$ iff $x \in S_\varepsilon$ for all $\varepsilon > 0$, which by the Hausdorff property means $x = 0$.

Since the metric $(x,y) \mapsto |x-y|$ is translation-invariant, it generates not only the topology but also the canonical uniformity of the t.v.s. $L$.
