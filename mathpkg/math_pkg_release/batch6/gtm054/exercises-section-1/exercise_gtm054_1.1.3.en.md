---
role: exercise
locale: en
chapter: "1"
section: "1"
exercise_number: 3
---

Let $S, T \in \mathcal{P}(U)$. Prove that

$$c_s + c_t = c_{s+t} \quad \text{and} \quad c_s c_t = c_{s \cap T},$$

and express $c_{s \cup T}$ in terms of $c_s$ and $c_t$.

For a set $U$, a function $s \in \mathbb{N}^U$ is called a selection from $U$. If $x \in U$, the number $s(x)$ is the "number of times $x$ is selected by $s$". The number

$$|s| = \sum_{x \in U} s(x)$$

is the cardinality (weight) of the selection $s$. If $|s| = m$, we say that $s$ is an $m$-selection. The set of all $m$-selections from $U$ is denoted by $\mathbb{S}_m(U)$, and we let

$$\mathbb{S}(U) = \bigcup_{m=0}^{\infty} \mathbb{S}_m(U) = \mathbb{N}^U.$$

If $S \in \mathcal{P}(U)$, we define the characteristic selection of $S$ by
