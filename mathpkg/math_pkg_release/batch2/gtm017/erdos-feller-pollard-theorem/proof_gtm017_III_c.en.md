---
role: proof
locale: en
of_concept: erdos-feller-pollard-theorem
source_book: gtm017
source_chapter: "III"
source_section: "c"
---
The theorem: For $\{f_n\}$ with $f_0=0$, $f_n \geq 0$, $\sum f_n=1$, gcd$\{n: f_n>0\}=1$, and $u_n$ satisfying $u_n = \sum_{k=0}^n f_k u_{n-k}$ with $u_0=1$, then $\lim u_n = (\sum n f_n)^{-1}$.

Let $\lambda = \limsup u_n$, $\gamma = \liminf u_n$. Take a subsequence $n_\nu$ with $u_{n_\nu} \to \lambda$. For any $j$ with $f_j > 0$, careful estimates using the renewal equation show $u_{n_\nu - j} \to \lambda$. By the gcd condition, any integer can be expressed as a linear combination of such $j$, forcing $\lambda = \gamma$ (limit exists). The value is determined by taking limits in the renewal equation and using $\sum f_n = 1$.
