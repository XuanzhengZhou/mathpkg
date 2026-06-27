---
role: exercise
locale: en
chapter: "6"
section: "8"
exercise_number: R
---

Let $(X, \mathbf{S})$ be a measurable space, let $(Y, \rho)$ be a complete metric space, and let $\{\varphi_n\}_{n=1}^{\infty}$ be a sequence of measurable mappings of $X$ into $Y$. Show that if $E$ denotes the subset of $X$ consisting of the points $x$ at which the sequence $\{\varphi_n(x)\}$ is convergent in $Y$, then $E$ is measurable, and setting

$$\Phi(x) = \lim_n \varphi_n(x), \quad x \in E,$$

defines a measurable mapping $\Phi$ of $E$ into $Y$. (Hint: For each triple $(p, q, r)$ of positive integers write $E_{p,q,r} = \{x \in X : \rho(\varphi_p(x), \varphi_q(x)) \leq 1/r\}$, and for each pair $(N, r)$ of positive integers set $F_{N,r} = \bigcap_{p,q=N}^{\infty} E_{p,q,r}$. Then $\bigcap_{r=1}^{\infty} \bigcup_{N=1}^{\infty} F_{N,r}$ is the set of convergence.)
