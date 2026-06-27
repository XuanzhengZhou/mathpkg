---
role: exercise
locale: en
chapter: "4-5"
section: "Section 06_Section_6"
exercise_number: 1
---

A. (Abel’s Theorem) Let

$$f(\lambda) = \sum_{n=0}^{\infty} \alpha_n \lambda^n,$$

(17)

where the power series (17) has radius of convergence $r_0$, $0 < r_0 < +\infty$, and suppose that for some point $\lambda_0 = r_0 e^{it_0}$ on the circle of convergence the series $\sum_{n} \alpha_n \lambda^n$ converges, say to $\sigma$. Show that

$$\lim_{r \uparrow r_0} f(re^{it_0}) = \sigma.$$

Thus $f$ converges “radially” to the sum of the power series representing $f$ at each point on the circle of convergence at which the series converges. (Hint: It is no loss of generality to assume $r_0 = 1$ and $t_0 = 0$. Multiply the given series by the geometric series $\sum_{n} \lambda^n$ to show that

$$f(\lambda) = (1 - \lambda) \sum_{n=0}^{\infty} \sigma_n \lambda^n,$$

where $\sigma_n = \sum_{i=0}^{n} \alpha_i$, $n \in \mathbb{N}_0$, and hence that

(ii) Let $f$ be an analytic function on a domain $\Delta$, and let $\bar{\Delta}$ denote the reflection of $\Delta$ in the real axis $-\bar{\Delta} = \{\lambda \in \mathbb{C} : \bar{\lambda} \in \Delta\}$. Verify that the function

$$f^(\lambda) = \overline{f(\bar{\lambda})}$$

is analytic on $\bar{\Delta}$ and that, in fact, $(f^\lambda)' = (f')^\lambda$ on $\bar{\Delta}$. If $\Delta = \bar{\Delta}$, then $f = f^\lambda$ if and only if $f$ is real-valued along the intersection of $\Delta$ with the real axis.

As it turns out, if $f$ is an analytic function on a domain $\Delta$, and if $f'(\lambda_0) \neq 0$ at some point $\lambda_0$ of $\Del
...
