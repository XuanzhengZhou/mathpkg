---
role: proof
locale: en
of_concept: consistency-of-prefix-union-lemma
source_book: gtm037
source_chapter: "3"
source_section: "3"
---

We prove the claim by induction on $n$, with $m$ fixed. Since $\Gamma$ is given to be consistent, the case $n = 0$ is trivial. The definition of $\Omega$ and $h$ immediately gives the desired result for $n = 1$.

Assume inductively that $n > 1$. If the claim fails for $n$, then

$$\bigwedge_{i < n-1} g^{+-1} f(m, i) \rightarrow \neg g^{+-1} f(m, n-1) \in \Gamma$$

Hence $f(m, n-1) \neq k(n-2)$ by the way $f$ was defined, so $f(m, n-1) = f(m, n-2)$. But then the claim fails for $n-1$, contradiction. Thus the claim holds for all $n$.
