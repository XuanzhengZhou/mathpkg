---
role: proof
locale: en
of_concept: closed-ideals-primary-decomposition-characterization
source_book: gtm028
source_chapter: "IV"
source_section: "§6. Krull's intersection theorem"
---

Let $\mathfrak{b} = \bigcap_i \mathfrak{a}_i$ where the intersection runs over those $i$ with $\mathfrak{m} + \mathfrak{p}_i \neq R$. By Theorem 12', each such $\mathfrak{a}_i$ is closed, so by Lemma 3, $\mathfrak{b}$ is closed, and $\mathfrak{b} = \bigcap_n (\mathfrak{b} + \mathfrak{m}^n)$.

Let $\{\mathfrak{a}'_j\}$ be the remaining primary components of $\mathfrak{a}$ and $\{\mathfrak{p}'_j\}$ their radicals. Since $\mathfrak{m} + \mathfrak{p}'_j = R$, $\mathfrak{m}$ is comaximal with each $\mathfrak{p}'_j$, hence with each $\mathfrak{a}'_j$, hence with the intersection $\mathfrak{b}'$ of the $\mathfrak{a}'_j$. Consequently $\mathfrak{m}^n$ is comaximal with $\mathfrak{b}'$ (Theorem 31, III, §13), so $\mathfrak{b}' + \mathfrak{m}^n = R$ for all $n$.

Thus $\mathfrak{b} = (\mathfrak{b}' + \mathfrak{m}^n)\mathfrak{b} = \mathfrak{b}'\mathfrak{b} + \mathfrak{m}^n\mathfrak{b} \subset \mathfrak{a} + \mathfrak{m}^n$ for all $n$. Since $\mathfrak{a} \subset \mathfrak{b}$, we have $\mathfrak{a} \subset \mathfrak{b} \subset \bigcap_n (\mathfrak{a} + \mathfrak{m}^n)$. But $\mathfrak{b}$ is closed and contains $\mathfrak{a}$, so $\mathfrak{b} \supset \bigcap_n (\mathfrak{a} + \mathfrak{m}^n)$. Therefore equality holds.
