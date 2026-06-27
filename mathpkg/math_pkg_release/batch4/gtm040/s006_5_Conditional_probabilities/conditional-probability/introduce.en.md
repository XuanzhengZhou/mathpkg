---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The conditional probability $\Pr[p \mid q]$ quantifies the likelihood of a statement $p$ given that another statement $q$ is known to be true. It is defined on a probability space $(\Omega, \mathcal{B}, \mu)$ as the ratio $\Pr[p \wedge q] / \Pr[q]$ when $\Pr[q] \neq 0$. By convention, it is taken to be zero when $\Pr[q] = 0$. This definition is fundamental to the study of Markov chains, where transition probabilities are expressed as conditional probabilities $\Pr[x_{n+1} = j \mid x_n = i]$.
