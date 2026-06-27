---
role: proof
locale: en
of_concept: noncyclicity-gcd-criterion-sums-of-independent
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Let $c$ be the greatest common divisor of $\{k \mid p_k > 0\}$. We claim that $c$ divides the period $d$ of the chain. Suppose to the contrary that there exists an integer $n$ such that $P_{ii}^{(n)} > 0$ but $c \nmid n$. Let $n$ be the smallest such integer, and write $n = qc + r$ with $0 < r < c$.

By Lemma 6-34 (the decomposition of transition probabilities via first passage probabilities),

$$P_{ii}^{(n)} = \sum_{k=1}^{n} \bar{F}_{ii}^{(k)} P_{ii}^{(n-k)}.$$

Since the chain is a sums of independent random variables process, the first passage probabilities $\bar{F}_{ii}^{(k)}$ depend only on $k-j$ (by translation invariance) and are given by the step size probabilities. In particular, $\bar{F}_{ii}^{(k)} > 0$ only if $c \mid k$, because the first return to $i$ corresponds to a sum of steps whose sizes all belong to $\{k \mid p_k > 0\}$, and any sum of multiples of $c$ is a multiple of $c$. Thus the sum reduces to

$$P_{ii}^{(n)} = \sum_{j=1}^{q} \bar{F}_{ii}^{(jc)} P_{ii}^{((q-j)c+r)}.$$

But by the minimality of $n$, every term $P_{ii}^{((q-j)c+r)}$ on the right-hand side is zero (since $(q-j)c + r < n$ and $c \nmid ((q-j)c + r)$ because $0 < r < c$). This forces $P_{ii}^{(n)} = 0$, contradicting the assumption that $P_{ii}^{(n)} > 0$.

Therefore $P_{ii}^{(n)} > 0$ only if $c \mid n$, which means that the period $d$ of the chain divides $c$. Consequently, if $c > 1$, the chain is cyclic; if $c = 1$, the chain is noncyclic.
