---
role: proof
locale: en
of_concept: hausdorff-tvs-metrizability-criterion
source_book: gtm003
source_chapter: "I"
source_section: "6"
---

**Proof of Theorem 6.1.** If $L$ is metrizable, the open balls of radius $1/n$ centered at $0$ form a countable neighborhood base of $0$. Conversely, suppose $L$ possesses a countable neighborhood base of $0$. Since $L$ is a Hausdorff t.v.s., by (1.2) there exists a decreasing sequence $\{V_n\}_{n \in \mathbb{N}}$ of circled $0$-neighborhoods such that $V_{n+1} + V_{n+1} \subset V_n$ for each $n$, and $\{V_n\}$ is a neighborhood base of $0$.

For each non-empty finite subset $H \subset \mathbb{N}$, let

$$V_H = \sum_{k \in H} V_k,$$

and define

$$p_H = \sum_{k \in H} 2^{-k}.$$

One shows that if $H$ and $K$ are non-empty finite subsets of $\mathbb{N}$ and $M$ is the unique finite subset of $\mathbb{N}$ for which $p_M = p_H + p_K$ (this $M$ is well-defined whenever $p_H + p_K < 1$, which happens precisely when $H$ and $K$ are disjoint---otherwise the binary expansions of $p_H$ and $p_K$ overlap; the subset $M$ is defined by the condition that $k \in M$ if and only if exactly one of $k \in H$ or $k \in K$ holds, carrying the sum in binary), then

$$V_H + V_K \subset V_M. \tag{1}$$

Indeed, since each $V_k$ is circled and the $V_k$ are decreasing, one has $V_j + V_k \subset V_k$ whenever $j \geq k$. The binary addition property ensures that each term in the sum $V_H + V_K$ can be absorbed into $V_M$.

It follows by induction on the number of elements of $H$ that

$$p_H < 2^{-n} \;\Longrightarrow\; n < H \;\Longrightarrow\; V_H \subset V_n, \tag{2}$$

where $n < H$ means $n < k$ for all $k \in H$.

Define the real-valued function $x \mapsto |x|$ on $L$ by $|x| = 1$ if $x$ is not contained in any $V_H$, and by

$$|x| = \inf_H \{\, p_H : x \in V_H \,\}$$

otherwise. The range of this function is contained in the real unit interval $[0, 1]$.

Since each $V_H$ is circled, for $|\lambda| \leq 1$ we have $x \in V_H \Rightarrow \lambda x \in V_H$, which yields $|\lambda x| \leq |x|$. Hence (i) is satisfied.

We next verify the triangle inequality (ii). This is evident for each pair $(x, y)$ such that $|x| + |y| \geq 1$. Hence suppose $|x| + |y| < 1$. Let $\varepsilon > 0$ be any real number such that $|x| + |y| + 2\varepsilon < 1$. There exist non-empty finite subsets $H$, $K$ of $\mathbb{N}$ such that $x \in V_H$, $y \in V_K$ and

$$p_H < |x| + \varepsilon, \qquad p_K < |y| + \varepsilon.$$

Since $p_H + p_K < 1$, there exists a unique finite subset $M$ of $\mathbb{N}$ for which $p_M = p_H + p_K$. By (1), $M$ has the property that $V_H + V_K \subset V_M$. It follows that $x + y \in V_M$ and hence

$$|x + y| \leq p_M = p_H + p_K < |x| + |y| + 2\varepsilon.$$

Since $\varepsilon > 0$ is arbitrary, this yields $|x + y| \leq |x| + |y|$, which proves (ii).

For any $\varepsilon > 0$, let $S_\varepsilon = \{ x \in L : |x| \leq \varepsilon \}$. From the definition of $|\cdot|$ and property (2) we assert that

$$S_{2^{-n-1}} \subset V_n \subset S_{2^{-n}} \qquad (n \in \mathbb{N}).$$

Indeed, if $x \in S_{2^{-n-1}}$ then $|x| \leq 2^{-n-1}$, so there exists $H$ with $x \in V_H$ and $p_H < 2^{-n}$. By (2), $n < H$, hence $V_H \subset V_n$ and $x \in V_n$. Conversely, if $x \in V_n$, taking $H = \{n\}$ gives $p_H = 2^{-n}$, so $|x| \leq 2^{-n}$ and $x \in S_{2^{-n}}$.

These inclusions show that $\{S_{2^{-n}}\}_{n \in \mathbb{N}}$ is a neighborhood base of $0$, and consequently the metric $(x, y) \mapsto |x - y|$ generates the topology of $L$. This proves (iv).

Finally, $|x| = 0$ implies $x \in S_{2^{-n}}$ for all $n$, hence $x \in \bigcap_{n} V_n = \{0\}$ since $L$ is Hausdorff; conversely $|0| = 0$ because $0 \in V_n$ for all $n$. This establishes (iii) and completes the proof. $\square$
