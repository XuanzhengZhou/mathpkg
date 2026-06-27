---
role: exercise
locale: en
chapter: "6-7"
section: "Section 08_Section_8"
exercise_number: 18
---

R. Let $(X, S)$ be a measurable space, let $(Y, \rho)$ be a complete metric space, and let $\{\varphi_n\}_{n=1}^{\infty}$ be a sequence of measurable mappings of $X$ into $Y$. Show that if $E$ denotes the subset of $X$ consisting of the points $x$ at which the sequence $\{\varphi_n(x)\}$ is convergent in $Y$, then $E$ is measurable, and setting

$$\Phi(x) = \lim_{n} \varphi_n(x), \quad x \in E,$$

defines a measurable mapping $\Phi$ of $E$ into $Y$. (Hint: For each triple $(p, q, r)$ of positive integers write $E_{p, q, r} = \{x \in X : \rho(\varphi_p(x), \varphi_q(x)) \leq 1/r\}$, and for each pair $(N, r)$ of positive integers set $F_{N, r} = \bigcap_{p, q=N}^{\infty} E_{p, q, r}$. Then $\bigcap_{r

and (iv) every real-valued function on $X$ that is measurable [S] belongs to $\mathcal{A}$. (Hint: The proofs of (i) and (ii) are straightforward, and (iv) follows at once from Proposition 6.6. To establish (iii) let $f$ be a function in $\mathcal{A}$ and let $U$ be an open subset of $\mathbb{R}$. Use Problem M and the Weierstrass approximation theorem (see Example 18C) to show that there exists a sequence $\{p_n(t)\}$ of real polynomials that converges pointwise to $\chi_U$, and observe that the function $h_n(t) = p_n(f(t))$ belongs to $\mathcal{A}$ for every positive integer $n$.
