---
role: proof
locale: en
of_concept: domain-extension-for-boolean-valued-sets
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

We extend the domain of $u_i$ to $d$ by defining $u'_i \in V^{(\mathbf{B})}$ by $\mathcal{D}(u'_i) = d$ and $(\forall x \in d)[u'_i(x) = \llbracket x \in u_i \rrbracket]$ for $i \in I$. Then for all $i \in I$,

$$\llbracket u_i = u'_i \rrbracket = \prod_{x \in \mathcal{D}(u_i)} (u_i(x) \Rightarrow \llbracket x \in u'_i \rrbracket) \cdot \prod_{x \in d} (u'_i(x) \Rightarrow \llbracket x \in u_i \rrbracket)$$
$$\geq \prod_{x \in \mathcal{D}(u_i)} (u_i(x) \Rightarrow u'_i(x))$$
$$= \prod_{x \in \mathcal{D}(u_i)} (u_i(x) \Rightarrow \llbracket x \in u_i \rrbracket)$$
$$= 1$$

by Theorem 13.4.3. Thus $\llbracket u_i = u'_i \rrbracket = 1$ and clearly $\mathcal{D}(u'_i) = d$, establishing both conditions.
