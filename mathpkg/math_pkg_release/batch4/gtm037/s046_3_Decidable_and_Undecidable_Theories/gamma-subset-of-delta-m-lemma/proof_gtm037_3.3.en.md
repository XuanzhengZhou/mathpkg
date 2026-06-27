---
role: proof
locale: en
of_concept: gamma-subset-of-delta-m-lemma
source_book: gtm037
source_chapter: "3"
source_section: "3"
---

Let $\varphi \in \Gamma$. Say $\varphi = g^{+-1} k(n)$ for some $n$. Then by the consistency lemma (1), $\Gamma \cup \{g^{+-1} f(m, i) : i \leq n\}$ is consistent, which implies that

$$\bigwedge_{i \leq n} g^{+-1} f(m, i) \rightarrow \neg g^{+-1} k(n) \notin \Gamma.$$

Therefore, by the definition of $f$, we have $f(m, n+1) = k(n)$, so $g^{+-1} f(m, n+1) = \varphi$ and consequently $\varphi \in \Delta_m$.
