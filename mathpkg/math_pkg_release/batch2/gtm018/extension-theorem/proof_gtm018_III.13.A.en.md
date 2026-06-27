---
role: proof
locale: en
of_concept: extension-theorem
source_book: gtm018
source_chapter: "III"
source_section: "13"
---

The existence of $\bar{\mu}$ (even without the restriction of $\sigma$-finiteness) is proved by 11.C and 12.A. To prove uniqueness, suppose that $\mu_1$ and $\mu_2$ are two measures on $\mathbf{S}(\mathbf{R})$ such that $\mu_1(E) = \mu_2(E)$ whenever $E \in \mathbf{R}$, and let $\mathbf{M}$ be the class of all sets $E$ in $\mathbf{S}(\mathbf{R})$ for which $\mu_1(E) = \mu_2(E)$. If one of the two measures is finite, and if $\{E_n\}$ is a monotone sequence of sets in $\mathbf{M}$, then, since

$$\mu_i(\lim_n E_n) = \lim_n \mu_i(E_n), \quad i = 1, 2,$$

we have $\lim_n E_n \in \mathbf{M}$. (The full justification of this step in the reasoning makes use of the fact that one of the two numbers $\mu_1(E_n)$ and $\mu_2(E_n)$, and therefore also the other one, is finite for every $n = 1, 2, \cdots$; cf. 9.D and 9.E.) Since this means that $\mathbf{M}$ is a monotone class, and since $\mathbf{M}$ contains $\mathbf{R}$, it follows from 6.B that $\mathbf{M}$ contains $\mathbf{S}(\mathbf{R})$.

In the general, not necessarily finite case, we may write $X$ as a countable disjoint union of sets in $\mathbf{R}$ of finite measure, and apply the result just proved to each such set separately, obtaining uniqueness for the whole space by countable additivity.
