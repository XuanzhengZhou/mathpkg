---
role: exercise
locale: en
chapter: "10"
section: "52"
exercise_number: 17
---

Show that $(\mathbb{N} + \{0\}, |)$ is a locally finite lattice with minimum element 1.

As an application of the Möbius function for $(\mathbb{N} + \{0\}, |)$, we shall give another proof of Theorem IE21, which is a formula for the Euler $\varphi$-function.

The function $\varphi$ is a selection; $\varphi \in S(\mathbb{N} + \{0\})$. Since $(\mathbb{N} + \{0\}, |)$ has the properties described in Exercise D17, we may compute for any $m \in \mathbb{N} + \{0\}$,

$$\tilde{\varphi}(m) = \sum_{k \in \mathbb{N} + \{0\}} [k, m] \varphi(k) = \sum_{k \mid m} \varphi(k) = \sum_{k \mid m} \varphi(m/k).$$

For each divisor $k$ of $m$, let $S_k = \{j \in \mathbb{N}_{[1,m]} : \gcd(j, m) = k\}$. Then $|S_k

XI Enumeration Theory

Let $(\mathbb{P}(X), \leq)$ be the lattice of partitions of the finite set $X$, ordered by refinement (cf. Exercise IIB30). If $\mathcal{Q}, \mathcal{R} \in \mathbb{P}(X)$ and $\mathcal{Q} \leq \mathcal{R}$, then for any $R \in \mathcal{R}$, we have $\{Q \in \mathcal{Q}: Q \subseteq R\} \in \mathbb{P}(R)$. This partition is called the restriction of $\mathcal{Q}$ to $R$ and is denoted by $\mathcal{Q}(R)$.
