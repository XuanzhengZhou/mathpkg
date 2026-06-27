---
role: proof
locale: en
of_concept: limit-of-monotone-sequence
source_book: gtm018
source_chapter: "I"
source_section: "3"
---

Let $\{E_n\}$ be a monotone sequence of subsets of $X$.

If $\{E_n\}$ is increasing, i.e., $E_n \subset E_{n+1}$ for all $n$, then for any point $x$ belonging to infinitely many $E_n$, we have $x \in E_n$ for all sufficiently large $n$ (since once $x \in E_n$, monotonicity implies $x \in E_m$ for all $m \geq n$). Thus $\limsup_n E_n = \liminf_n E_n = \bigcup_n E_n$.

If $\{E_n\}$ is decreasing, i.e., $E_n \supset E_{n+1}$ for all $n$, then for any point $x$ belonging to all but finitely many $E_n$, we have $x \in \bigcap_n E_n$. Conversely, any point in $\bigcap_n E_n$ clearly belongs to all $E_n$. Thus $\limsup_n E_n = \liminf_n E_n = \bigcap_n E_n$.

In both cases, $\limsup_n E_n = \liminf_n E_n$, so $\lim_n E_n$ exists and is equal to

$$\bigcup_n E_n \text{ or } \bigcap_n E_n$$

according as the sequence is increasing or decreasing.
