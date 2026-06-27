---
role: proof
locale: en
of_concept: bounded-sequence-nonstandard-characterization
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

$(i) \Rightarrow (ii)$. Choose a positive real number $M$ such that $|x_n| \leq M$ for all $n$. Since $^*\mathbb{R}$ is an elementary extension of $\mathbb{R}$ for any structures over $\mathbb{R}$, the same bound holds in the nonstandard extension: $|{}^*x_n| \leq M$ for all $n \in {}^*\omega$. Hence for every infinite $n$, $^*x_n$ is bounded by the standard real $M$ and is therefore finite.

$(ii) \Rightarrow (i)$. Assume $(ii)$. If $x$ were unbounded, then for each $m \in \omega$ there would exist $n_m \in \omega$ with $|x_{n_m}| > m$. By overspill or by considering the ultrapower construction, this would produce an infinite index at which $^*x$ is infinite, contradicting $(ii)$.
