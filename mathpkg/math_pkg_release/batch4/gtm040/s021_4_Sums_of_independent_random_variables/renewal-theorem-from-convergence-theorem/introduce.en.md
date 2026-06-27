---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 6-40 demonstrates that the convergence theorem for Markov chains (Theorem 6-38) and the classical Renewal Theorem (Theorem 1-67) are essentially equivalent. Given an arbitrary renewal sequence $\{f_n\}$ with $\sum f_n = 1$ and $\gcd\{n : f_n > 0\} = 1$, one constructs a basic example Markov chain whose first return probabilities $ar{F}_{00}^{(n)}$ equal $f_n$. The chain is noncyclic and recurrent by construction. The convergence of $P_{00}^{(n)}$ in this chain then implies that the renewal sequence $u_n$ (defined by $u_0 = 1$ and $u_n = \sum_{k=1}^n f_k u_{n-k}$) converges, which is precisely the assertion of the Renewal Theorem.
