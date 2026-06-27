---
role: proof
locale: en
of_concept: limit-nonstandard-characterization
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

$(i) \Rightarrow (ii)$. Let $\varepsilon > 0$, $\varepsilon$ standard. Then by $(i)$ there is an $m \in \omega$ such that $|x_n - s| \leq \varepsilon$ for all $n \geq m$. Thus the set $\{n : |x_n - s| \leq \varepsilon\}$ contains a cofinite set and therefore belongs to the nonprincipal ultrafilter $F$. Hence $|{}^*x_n - s| \leq \varepsilon$ holds in $^*\mathbb{R}$ for every infinite $n$. Since $\varepsilon$ is arbitrary, $^*x_n \simeq s$ for every infinite $n$.

$(ii) \Rightarrow (i)$. Assume $(ii)$ and let $\varepsilon > 0$ be standard. Then for every infinite $n$, $|{}^*x_n - s| < \varepsilon$. Hence the internal set $\{n \in {}^*\omega : |{}^*x_n - s| < \varepsilon\}$ contains all infinite natural numbers. By overspill, it must also contain some standard $m \in \omega$, and all $n \geq m$ in $\omega$. Thus $\lim_{n \to \infty} x_n = s$.
