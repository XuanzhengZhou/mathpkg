---
role: proof
locale: en
of_concept: corollary-maximum-principle-family-representation
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \llbracket (\exists u) \varphi(u) \rrbracket = \sum_{x \in V^{(B)}} \llbracket \varphi(x) \rrbracket$. There exists an ordinal $\alpha$ and elements $u_\xi \in V^{(B)}$ ($\xi < \alpha$) such that $b = \sum_{\xi < \alpha} \llbracket \varphi(u_\xi) \rrbracket$. Set $b_\xi = \llbracket \varphi(u_\xi) \rrbracket \cdot \prod_{\eta < \xi} (-\llbracket \varphi(u_\eta) \rrbracket)$. Then $\{b_\xi \mid \xi < \alpha\}$ is a disjoint family with sum $b$, and $b_\xi \leq \llbracket \varphi(u_\xi) \rrbracket$.

By Theorem 16.1, we may assume all $u_\xi$ have the same complete domain $d$. Define $v \in V^{(B)}$ by $\mathcal{D}(v) = d$ and $v(x) = \sum_{\xi < \alpha} b_\xi \cdot u_\xi(x)$ for $x \in d$. Then one checks that $b_\xi \leq \llbracket v = u_\xi \rrbracket$ for all $\xi < \alpha$, hence $b_\xi \leq \llbracket \varphi(v) \rrbracket$. Therefore $b = \sum_{\xi} b_\xi \leq \llbracket \varphi(v) \rrbracket$. But also $\llbracket \varphi(v) \rrbracket \leq \sum_{x \in V^{(B)}} \llbracket \varphi(x) \rrbracket = b$, hence $\llbracket \varphi(v) \rrbracket = b$.
