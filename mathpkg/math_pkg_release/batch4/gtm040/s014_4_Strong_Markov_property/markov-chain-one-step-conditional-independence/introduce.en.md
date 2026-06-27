---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Lemma 4-6 establishes a key form of the Markov property: conditioning on the present state $x_n = i$ makes the immediate future (from time $n+1$ onward, encoded as a statement $r$ relative to $\mathcal{T}_{n+1} \cap \mathcal{F}$) conditionally independent of the past before time $n$ (encoded as a statement $q$ relative to $\mathcal{F}_{n-1}$). Moreover, the conditional probability $\Pr_{\pi}[r \mid x_n = i]$ equals $\Pr_i[r']$, the probability of the shifted statement $r'$ when the chain starts from state $i$. This lemma provides the stepping stone to the full strong Markov property.
