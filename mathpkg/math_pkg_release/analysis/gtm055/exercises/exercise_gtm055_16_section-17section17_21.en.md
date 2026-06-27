---
role: exercise
locale: en
chapter: "16"
section: "Section 17_Section_17"
exercise_number: 21
---

U. If $\varphi$ is a continuously differentiable function on $\mathbb{R}$ that is supported on some closed interval $[c, d]$, then $\varphi'$ is bounded on $\mathbb{R}$. Use this fact to show that the difference quotient $(\varphi(s + h) - \varphi(s))/h$ tends boundedly to $\varphi'(s)$ on $\mathbb{R}$ as $h$ tends to zero. (Show, that is, that there exists a positive constant $M$ such that $|(\varphi(s + h) - \varphi(s))/h| \leq M$ for all $h \neq 0$.) Conclude that if $f$ is a locally integrable function on $\mathbb{R}$ (Ex. O), then the function

$$g(s) = \int_{\mathbb{R}} f(t) \varphi(s - t) dt$$

has derivative

$$g'(s) = \int_{\mathbb{R}} f(t) \varphi'(s - t) dt$$

at every point $s$ of $\mathbb{R}$. (Hint: See Problem 7W).)

(i) Let $r$ be a positive number and let $\varphi_r$ be a nonnegative test function on $\mathbb{R}^n$ that is supported on the ball $(\mathbb{R}^n)_r = \{x \in \mathbb{R}^n : \|x\|_2 \leq r\}$ and satisfies the condition $\int_{\mathbb{R}^n} \varphi_r d\mu_n

(Hint: This is just an infinitely differentiable version of Example 3G, $qv$. One may assume the open sets $U_1, \ldots, U_m$ to be bounded, and it is convenient to do so. There exists a closed covering of $\mathbb{R}^n$ consisting of a closed set $F_0$ that is disjoint from $K$ and compact sets $K_1, \ldots, K_m$ such that $K_i \subset U_i, i = 1, \ldots, m$ (see Example 3G). Let $\eta_0 = d(K, F_0)$, let $\eta_i = d(K_i, \mathbb{R}^n \setminus U_i), i = 1, \ldots, m$, and set $\varepsilon = 
...
