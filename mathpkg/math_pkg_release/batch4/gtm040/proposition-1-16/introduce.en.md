---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $\rho$ be an additive set function defined on a field of sets $\mathcal{F}$. Let $\{A_n\}$ be a sequence of sets in $\mathcal{F}$ such that $A_1 \subset A_2 \subset \cdots$, and suppose $A = \bigcup_{n=1}^{\infty} A_n$ is in $\mathcal{F}$. If $\rho$ is completely additive, then $\lim_{n \to \infty} \rho(A_n) = \rho(A)$. Conversely, if $\lim_{n \to \infty} \rho(A_n) = \rho(A)$ for all such sequences, $\rho$ is completely additive.

We give four examples of measure spaces.

(1) Let $X$ be any set, let $\mathcal{F} = \{\varnothing, X\}$, and define $\mu(\varnothing) = 0$ and $\mu(X) = a \geq 0$. Then $X$ is the trivial measure space.

(2) Let $X$ be Euclidean $n$-space, let $\mathcal{F}$ be the Lebesgue measurable sets, and let $\mu$ be Lebesgue measure (the natural generalization of length, area, or volume).

(3) Let $X$ be the set of six possible outcomes for tossing a die. Assign weight $\frac{1}{6}$ to each of the six points in the space, and for any subset of $X$ assign as a measure the sum of the weights of the points in the set. Then $\mathcal{F}$ is the family of all subsets of $X$, and $X$ is a probability space.

(4) Let $X$ be a denumerable index set, and let $\pi$ be a non-negative row vector with $X$ as its index set. Assign as a weight to each point of $X$ the value of the corresponding entry of $\pi$. For any subset of $X$ assign as a measure the sum of the weights of the points in the set. Then $\mathcal{F}$ is the family of all subsets of $X$, and $X$ is a measure space with total measure $\pi 1$.

The sets of a field on which a measure $\mu$ is defined are called the $\mu$-measurable or simply the measurable subsets of $X$. In the construction of a measure on a field, it is possible for a non-empty set $A$ to be assigned measure zero. In example (2) above, for instance, every denumerable set and even certain uncountable sets are sets of measure zero. Suppose $B$ is a subset of such a set $A$. If $B$ is measurable, then $\mu(B) \geq 0$ since $\mu$ is a measure. But

$$\mu(B) \leq \mu(A) = 0$$

since $B \subset A$ and $A$ is of measure zero. Thus, a measurable subset of a set of measure zero

Proposition 1-18: Let $\mu$ be a measure defined on a field of sets $\mathcal{F}$. If $\{A_n\}$ is a sequence of sets in $\mathcal{F}$, if $A$ is in $\mathcal{F}$, and if $A \subset \bigcup_n A_n$, then

$$\mu(A) \leq \sum_n \mu(A_n).$$
