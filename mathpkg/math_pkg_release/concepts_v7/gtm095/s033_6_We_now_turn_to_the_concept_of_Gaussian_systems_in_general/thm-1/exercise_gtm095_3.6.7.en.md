---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 7
---

# Exercise 7

Establish the equivalence of $(\text{I}^*)$–$(\text{IV}^*)$ as stated in Remark 2 on Theorem 1. Specifically, prove that for finite measures $\mu, \mu_1, \mu_2, \ldots$ on a metric space $(E, \mathcal{E}, \rho)$, the following are equivalent:

$(\text{I}^*)$ $\mu_n \xrightarrow{w} \mu$,

$(\text{II}^*)$ $\limsup_n \mu_n(F) \leq \mu(F)$ for every closed $F$, and $\mu_n(E) \to \mu(E)$,

$(\text{III}^*)$ $\liminf_n \mu_n(G) \geq \mu(G)$ for every open $G$, and $\mu_n(E) \to \mu(E)$,

$(\text{IV}^*)$ $\mu_n(A) \to \mu(A)$ for every Borel set $A$ with $\mu(\partial A) = 0$.

*Hint.* Mimic the proof of Theorem 1. The key difference is that when handling the complement argument for $(\text{II}^*) \Leftrightarrow (\text{III}^*)$, use $\mu_n(G) = \mu_n(E) - \mu_n(G^c)$ and the fact that $\mu_n(E) \to \mu(E)$ to pass the limit through. For the proof of $(\text{IV}^*) \Rightarrow (\text{I}^*)$, note that the set $D = \{t : \mu(f^{-1}\{t\}) > 0\}$ remains at most countable because $\mu$ is finite.
