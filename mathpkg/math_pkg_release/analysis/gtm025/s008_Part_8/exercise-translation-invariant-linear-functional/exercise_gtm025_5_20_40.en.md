---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 40
---

(a) Prove that there exists a linear functional $M$ on $\mathfrak{B}^r(R)$ such that for all $f \in \mathfrak{B}^r(R)$ and all $t \in R$, we have

(i) $\inf\{f(x): x \in R\} \leq M(f) \leq \sup\{f(x): x \in R\}$

and

(ii) $M(f_t) = M(f)$, where $f_t(x) = f(x + t)$.

[Hints. Let $\mathfrak{H}$ be the linear subspace of $\mathfrak{B}^r(R)$ consisting of all finite sums of functions of the form $f_t - f$ for $f \in \mathfrak{B}^r(R)$ and $t \in R$. For

$$h = \sum_{k=1}^{n} \left[ (f_k)_{t_k} - f_k \right] \in \mathfrak{H},$$

prove that $\inf\{h(x): x \in R\} \leq 0$. Assuming this is false, choose $\varepsilon > 0$ such that $h(x) \geq \varepsilon$ for all $x \in R$. Let $p$ be an arbitrary positive integer, and let $\Phi$ denote the set of all functions $\varphi$ from $\{1, 2, \ldots, n\}$ into $\{1, 2, \ldots, p\}$. For each $\varphi \in \Phi$, let $x(\varphi) = \varphi(1)t_1 + \varphi(2)t_2 + \cdots + \varphi(n)t_n$. Show that

$$\sum_{\varphi \in \Phi} \left[ f_k(x(\varphi) + t_k) - f_k(x(\varphi)) \right] \leq 2p^{n-1} \|f_k\|_u.$$

Summing over $k = 1, \ldots, n$ and dividing by $p^n$ yields a contradiction as $p \to \infty$.]
