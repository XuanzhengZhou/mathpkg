---
role: proof
locale: en
of_concept: lemma-cofinal-in-qalpha
source_book: gtm043
source_chapter: "13"
source_section: "21"
---

Given $A \subset Q_\alpha$, let $x = \sup A$ (in $s$). If $x \in A$, then $\{x\}$ is cofinal. Assume $x \notin A$. By 13.18(a), there exists an ordinal $\leq \alpha$ — and hence a smallest such ordinal $\tau$ — such that $x_\xi = 0$ for all $\xi \geq \tau$; also, $x \notin Q$, so $\tau$ must be a limit ordinal.

By definition of $\tau$, there exist arbitrarily large indices $\sigma < \tau$ for which $x_\sigma = 1$. To each such $\sigma$, associate an element $s$ defined by:
$$s_\xi = x_\xi \text{ for } \xi \leq \sigma, \text{ and } s_\xi = 0 \text{ for } \xi > \sigma.$$

Since $\tau$ is countable, there are only countably many such elements $s$; and their supremum is $x$. For each such $s$, pick $a \in A$ with $a \geq s$; the set of all such $a$ is a countable cofinal subset of $A$. The construction of a countable coinitial subset is analogous.
