---
role: exercise
locale: en
chapter: "27"
section: "APPLICATIONS TO ANALYSIS"
exercise_number: 14
---

One more definition of capacity. Given an arbitrary aperiodic transient random walk, and a finite subset $A \subset R$, consider the (random) set $A_n$ which is "swept out" by the random walk in time $n$: formally
$$A_n = \{ x \mid x \in x_k + A \text{ for some } k, \ 0 \leq k \leq n \}.$$
Finally let $C_n(A) = |A_n|$ denote the cardinality of $A_n$. Prove that the capacity $C(A)$ of the set $A$ is given by
$$\lim_{n \to \infty} \frac{C_n(A)}{n} = C(A)$$
with probability one.

Hint: Observe that if $A = \{0\}$, then $C_n(A) = R_n$, the range of the random walk, as defined in D4.1. According to E4.1 the above limit then exists and is $1 - F = G^{-1}$, the capacity of a single point. Observe further that the proof in E4.1 applies, with obvious modifications, in the present case.
