---
role: proof
locale: en
of_concept: minimal-regular-function-characterization
source_book: gtm040
source_chapter: "10"
source_section: "9. Fine boundary functions"
---

**Proof.** ($\Rightarrow$) Suppose $h$ is minimal. The regularity of $h$ implies that the constant function $1$ is regular for $P^h$ restricted to $S^h$. Let $\bar{h}$ be any bounded regular function for $P^h$ restricted to $S^h$. By adding a suitable multiple of $1$, we may assume without loss of generality that $0 \leq \bar{h} \leq c 1$ for some constant $c$. Define
\[
k_i = \begin{cases}
\bar{h}_i h_i & \text{if } i \in S^h, \\
0 & \text{otherwise}.
\end{cases}
\]

Then $k$ is a regular function for $P$. Since $0 \leq k_i \leq c h_i$ for all $i$, and $h$ is minimal, we must have $k = \lambda h$ for some constant $\lambda$. On $S^h$, this gives $\bar{h}_i h_i = \lambda h_i$, so $\bar{h}_i = \lambda$ for all $i \in S^h$. Hence $\bar{h}$ is constant on $S^h$.

($\Leftarrow$) Conversely, suppose the only bounded regular functions for $P^h$ restricted to $S^h$ are constants. Let $k$ be a regular function for $P$ with $0 \leq k \leq c h$ for some constant $c$. On $S^h$, define $\bar{h}_i = k_i / h_i$. Then $\bar{h}$ is a bounded regular function for $P^h$ restricted to $S^h$, with $0 \leq \bar{h} \leq c$. By hypothesis, $\bar{h}$ must be constant, so $k = \lambda h$ for some $\lambda$, showing $h$ is minimal.
