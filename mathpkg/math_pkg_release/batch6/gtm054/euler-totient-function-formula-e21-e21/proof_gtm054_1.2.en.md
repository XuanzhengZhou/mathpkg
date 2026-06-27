---
role: proof
locale: en
of_concept: euler-totient-function-formula-e21-e21
source_book: gtm054
source_chapter: "1"
source_section: "ID"
---

Clearly $\varphi(1) = 1$. If $n \geq 2$, let $B = \{1, 2, \ldots, n\}$, and let the function $f: B \rightarrow \mathcal{P}(V)$ be given by $f(b) = \{p \in V: p \text{ divides } b\}$, for each $b \in B$. Thus, $(V, f, B)$ is a system, and $\varphi(n)$ is the number of blocks of size 0. Let $s$ be the selection of $(V, f, B)$. By E8b, for each $S \in \mathcal{P}(V)$, $\bar{s}(S)$ is the number of blocks divisible by every prime in $S$. Thus $\bar{s}(S) = n/\prod_{p \in S} p$. Substituting this into E13b with $k = 0$, we have

$$\varphi(n) = \sum_{t=0}^{|V|} (-1)^t \sum_{|S|=t} \frac{n}{\prod_{p \in S} p} = n \sum_{S \in \mathcal{P}(V)} \prod_{p \in S} \frac{-1}{p} = n \prod_{p \in V} \left(1 - \frac{1}{p}\right).$$

this last step requiring only algebraic manipulation.

We close with two exercises of a general nature.
