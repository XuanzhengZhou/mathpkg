---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 6
---

# Exercise 6

Prove the statement in Remark 1 on Theorem 1. That is, show that Theorem 1 admits a natural generalization to the case when the probability measures $P$ and $P_n$ defined on $(E, \mathcal{E}, \rho)$ are replaced by arbitrary (not necessarily probability) finite measures $\mu$ and $\mu_n$. For such measures we can introduce weak convergence $\mu_n \xrightarrow{w} \mu$ and convergence in general $\mu_n \Rightarrow \mu$ and, just as in Theorem 1, establish the equivalence of the conditions:

$$(\text{I}^*)\ \mu_n \xrightarrow{w} \mu,$$

$$(\text{II}^*)\ \limsup \mu_n(A) \leq \mu(A),\ \text{where } A \text{ is closed and } \mu_n(E) \rightarrow \mu(E),$$

$$(\text{III}^*)\ \liminf \mu_n(A) \geq \mu(A),\ \text{where } A \text{ is open and } \mu_n(E) \rightarrow \mu(E),$$

$$(\text{IV}^*)\ \mu_n \Rightarrow \mu.$$

Each of these is equivalent to any of $(\text{V}^*)$–$(\text{VIII}^*)$, which are the conditions $(\text{V})$–$(\text{VIII})$ with $P_n$ and $P$ replaced by $\mu_n$ and $\mu$.

*Hint.* The proof for finite measures follows the same structure as for probability measures. The additional condition $\mu_n(E) \to \mu(E)$ is needed in $(\text{II}^*)$ and $(\text{III}^*)$ because without it mass could escape to infinity even while satisfying the limsup/liminf inequalities.
