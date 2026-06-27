---
role: proof
locale: en
of_concept: maximum-principle
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $\langle u_\xi \mid \xi < \alpha \rangle$ be an enumeration of $V^{(\mathbf{B})}$. Set
$$b_\xi = \llbracket \varphi(u_\xi) \rrbracket \cdot \prod_{\eta < \xi} \neg \llbracket \varphi(u_\eta) \rrbracket$$
for $\xi < \alpha$. Then the $b_\xi$ are pairwise disjoint and
$$b = \sum_{\xi < \alpha} b_\xi = \sum_{\xi < \alpha} \llbracket \varphi(u_\xi) \rrbracket = \llbracket (\exists u) \varphi(u) \rrbracket.$$

By Theorem 16.1 we can assume that $(\forall \xi < \alpha)[\mathcal{D}(u_\xi) = d]$ for some common domain $d$. Define $v \in V^{(\mathbf{B})}$ by
$$\mathcal{D}(v) = d \quad\text{and}\quad (\forall x \in d)\left[ v(x) = \sum_{\xi < \alpha} b_\xi \cdot u_\xi(x) \right].$$

Then by construction, for $\xi < \alpha$ and $x \in d$,
$$b_\xi \cdot v(x) = b_\xi \cdot u_\xi(x).$$

Therefore, for $\xi < \alpha$,
\begin{align*}
\llbracket v = u_\xi \rrbracket &= \prod_{x \in d} (v(x) \Rightarrow \llbracket x \in u_\xi \rrbracket) \cdot \prod_{x \in d} (u_\xi(x) \Rightarrow \llbracket x \in v \rrbracket) \\
&\geq b_\xi \cdot \prod_{x \in d} (v(x) \Rightarrow \llbracket x \in u_\xi \rrbracket) \cdot \prod_{x \in d} (u_\xi(x) \Rightarrow \llbracket x \in v \rrbracket) \\
&\geq b_\xi \cdot \prod_{x \in d} (b_\xi \cdot u_\xi(x) \Rightarrow b_\xi \cdot u_\xi(x)) \cdot \prod_{x \in d} (b_\xi \cdot u_\xi(x) \Rightarrow b_\xi \cdot u_\xi(x)) \\
&= b_\xi.
\end{align*}

Hence $b_\xi \leq \llbracket v = u_\xi \rrbracket \cdot \llbracket \varphi(u_\xi) \rrbracket \leq \llbracket \varphi(v) \rrbracket$ for all $\xi < \alpha$. Therefore
$$b \leq \llbracket \varphi(v) \rrbracket.$$

But also $\llbracket \varphi(v) \rrbracket \leq \sum_{x \in V^{(\mathbf{B})}} \llbracket \varphi(x) \rrbracket = b$, therefore
$$b = \llbracket \varphi(v) \rrbracket = \llbracket (\exists u) \varphi(u) \rrbracket.$$
