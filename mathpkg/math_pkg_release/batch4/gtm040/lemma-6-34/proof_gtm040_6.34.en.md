---
role: proof
locale: en
of_concept: lemma-6-34
source_book: gtm040
source_chapter: "6"
source_section: "34"
---

**Proof:** The first two statements are obvious; for the third we first note that if $\Pr_i[\bar{t}_j = k] > 0$, then for $n \geq k$,

$$\Pr_i[x_n = j \mid \bar{t}_j = k] = \Pr_i[x_n = j \mid x_k = j \land x_{k-1} \neq j \land \cdots \land x_1 \neq j]$$

$$= \Pr_i[x_n = j \mid x_k = j] \quad \text{by Lemma 4-6}$$

$$= \Pr_j[x_{n-k} = j] \quad \text{by Lemma 4-6}$$

$$= P_{jj}^{(n-k)}.$$

Hence no matter what the value of $\Pr_i[\bar{t}_j = k]$, it is true that, for $n \geq k$,

$$\Pr_i[\bar{t}_j = k] \Pr_i[x_n = k \mid \bar{t}_j = k] = \bar{F}_{ij}^{(k)} P_{jj}^{(n-k)}.$$

Using $x_n =

is $c$. We shall show that $c$ divides $d$, the period of the chain. Hence, if $c > 1$, the chain is cyclic. Let $n$ be the smallest integer for which $P_{ii}^{(n)} > 0$ and $c \nmid n$, and write $n = qc + r$ with $0 < r < c$. By Lemma 6-34,

$$P_{ii}^{(n)} = \sum_{k=1}^{n} \bar{F}_{ii}^{(k)} P_{ii}^{(n-k)}$$

$$= \sum_{j=1}^{q} \bar{F}_{ii}^{(jc)} P_{ii}^{((q-j)c+r)}$$

Then the right side is zero since every term $P_{ii}^{((q-j)c+r)}$ is zero, a contradiction. Thus $P_{ii}^{(n)} > 0$ only if $c \mid n$.

The next two lemmas lead to the convergence theorem; the first one is a consequence of Proposition 6-32 and the zero-one law for sums of independent random variables.
