---
role: proof
locale: en
of_concept: holomorphic-partial-derivatives
source_book: gtm038
source_chapter: "I"
source_section: "3. The Cauchy Integral"
---
**Proof.** 1. Let $P \subset B$, $\mathfrak{z}_1 \in P \cap \mathbb{C}^{*n}$. Then there is an $M \in \mathbb{R}$ such that $|a_v \mathfrak{z}_1^v| < M$ for all $v$, where $\sum_{v=0}^{\infty} a_v \mathfrak{z}^v$ is the power series expansion of $f$ in $P$. If $0 < q < 1$ and $\mathfrak{z}_2 := q \cdot \mathfrak{z}_1$, then $\sum_{v=0}^{\infty} a_v \mathfrak{z}_2^v$ is dominated by $M \cdot \sum_{v=0}^{\infty} q^{|v|}$. Now $\mathfrak{z}_2 = (z_1, \ldots, z_n)$ with $|z_k| \neq 0$ for $k = 1, \ldots, n$. It follows that

$$|a_v \cdot v_j \cdot z_1^{v_1} \cdots z_j^{v_j-1} \cdots z_n^{v_n}| = \frac{v_j}{|z_j|} \cdot |a_v \mathfrak{z}_2^v| \leqslant \frac{v_j}{|z_j|} M \cdot q^{|v|}.$$

2. Formally,

$$\sum_{v=0}^{\infty} v_j \cdot q^{|v|} = \left( \sum_{v_1=0}^{\infty} q^{v_1} \right) \cdots \left( \sum_{v_j=0}^{\infty} v_j q^{v_j} \right) \cdots \left( \sum_{v_n=0}^{\infty} q^{v_n} \right)$$

and since $\sum_{v_j=0}^{\infty} v_j q^{v_j} = q/(1-q)^2 < \infty$, the differentiated series converges absolutely and uniformly on compact subsets. By standard results on termwise differentiation of power series, the partial derivatives $f_{z_\mu}$ exist and are given by the termwise differentiated series, which is again a convergent power series and hence holomorphic. $\square$
