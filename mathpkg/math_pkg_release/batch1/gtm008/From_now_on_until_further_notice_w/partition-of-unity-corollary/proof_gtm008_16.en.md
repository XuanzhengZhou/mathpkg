---
role: proof
locale: en
of_concept: partition-of-unity-corollary
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

By Theorem 16.1 we can assume $(\forall \xi < \alpha)[\mathcal{D}(u_\xi) = d]$. Define $v \in V^{(\mathbf{B})}$ by

$$\mathcal{D}(v) = d \quad\text{and}\quad (\forall x \in d)\left[ v(x) = \sum_{\xi < \alpha} b_\xi \cdot u_\xi(x) \right].$$

Since the $b_\xi$ are pairwise disjoint, for each $\xi < \alpha$ and $x \in d$ we have $b_\xi \cdot v(x) = b_\xi \cdot u_\xi(x)$. Then

\begin{align*}
\llbracket v = u_\xi \rrbracket &= \prod_{x \in d} (v(x) \Rightarrow \llbracket x \in u_\xi \rrbracket) \cdot \prod_{x \in d} (u_\xi(x) \Rightarrow \llbracket x \in v \rrbracket) \\
&\geq b_\xi \cdot \prod_{x \in d} (b_\xi \cdot u_\xi(x) \Rightarrow b_\xi \cdot u_\xi(x)) \cdot \prod_{x \in d} (b_\xi \cdot u_\xi(x) \Rightarrow b_\xi \cdot u_\xi(x)) \\
&= b_\xi.
\end{align*}

Thus $b_\xi \leq \llbracket v = u_\xi \rrbracket$ for all $\xi < \alpha$.
