---
role: proof
locale: en
of_concept: maximum-principle
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \llbracket (\exists u) \varphi(u) \rrbracket = \sum_{x \in V^{(\mathbf{B})}} \llbracket \varphi(x) \rrbracket$. If $b = 0$ we can take any $v$, so assume $b > 0$. Let $\alpha$ be an ordinal such that $V_{\alpha}^{(\mathbf{B})}$ contains a set of representatives for all $\{x \in V^{(\mathbf{B})} \mid \llbracket \varphi(x) \rrbracket \neq 0\}$. Choose an enumeration $\langle x_\xi \mid \xi < \alpha \rangle$ of $V_{\alpha}^{(\mathbf{B})}$ and define

$$b_\xi = \llbracket \varphi(x_\xi) \rrbracket \cdot \prod_{\eta < \xi} (-\llbracket \varphi(x_\eta) \rrbracket)$$

for $\xi < \alpha$. Then the $b_\xi$ are pairwise disjoint (orthogonal) and

$$\sum_{\xi < \alpha} b_\xi = \sum_{\xi < \alpha} \llbracket \varphi(x_\xi) \rrbracket = b.$$

By Lemma 13.4 (properties of Boolean-valued models), there exist $u_\xi \in V^{(\mathbf{B})}$ such that

i) $\llbracket u_\xi = x_\xi \rrbracket \geq b_\xi$ and $\llbracket \varphi(u_\xi) \rrbracket \geq b_\xi$ for all $\xi < \alpha$.

By Theorem 16.1 we can assume that $(\forall \xi < \alpha)[\mathcal{D}(u_\xi) = d]$ for some common $d \subseteq V^{(\mathbf{B})}$. Define $v \in V^{(\mathbf{B})}$ by

$$\mathcal{D}(v) = d \land (\forall x \in d) \left[ v(x) = \sum_{\xi < \alpha} b_\xi \cdot u_\xi(x) \right].$$

Then by i),

ii) $\xi < \alpha \land x \in d \rightarrow b_\xi \cdot v(x) = b_\xi \cdot u_\xi(x)$.

Therefore, for $\xi < \alpha$,

$$\llbracket v = u_\xi \rrbracket = \prod_{x \in d} (v(x) \Rightarrow \llbracket x \in u_\xi \rrbracket) \cdot \prod_{x \in d} (u_\xi(x) \Rightarrow \llbracket x \in v \rrbracket)$$

$$\geq b_\xi \cdot \prod_{x \in d} (v(x) \Rightarrow \llbracket x \in u_\xi \rrbracket) \cdot \prod_{x \in d} (u_\xi(x) \Rightarrow \llbracket x \in v \rrbracket)$$

$$\geq b_\xi \cdot \prod_{x \in d} (b_\xi u_\xi(x) \Rightarrow b_\xi u_\xi(x)) \cdot \prod_{x \in d} (b_\xi u_\xi(x) \Rightarrow b_\xi u_\xi(x))$$

$$= b_\xi.$$

Hence $b_\xi \leq \llbracket v = u_\xi \rrbracket \cdot \llbracket \varphi(u_\xi) \rrbracket \leq \llbracket \varphi(v) \rrbracket$ for all $\xi < \alpha$. Therefore

$$b \leq \llbracket \varphi(v) \rrbracket.$$

But also $\llbracket \varphi(v) \rrbracket \leq \sum_{x \in V^{(\mathbf{B})}} \llbracket \varphi(x) \rrbracket = b$, therefore

$$b = \llbracket \varphi(v) \rrbracket.$$
