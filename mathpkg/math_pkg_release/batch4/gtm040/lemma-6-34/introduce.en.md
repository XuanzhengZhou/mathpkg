---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

For any Markov chain and any states $i$ and $j$,

$$P_{ij}^{(0)} = \delta_{ij}$$

$$\bar{F}_{ij}^{(0)} = 0,$$

and

$$P_{ij}^{(n)} = \sum_{k=1}^{n} \bar{F}_{ij}^{(k)} P_{jj}^{(n-k)} = \sum_{k=0}^{n-1} P_{jj}^{(k)} \bar{F}_{ij}^{(n-k)} \quad \text{for } n > 0.$$
