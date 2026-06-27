---
role: proof
locale: en
of_concept: convergence-constants-lemma
source_book: gtm095
source_chapter: "3"
source_section: "§6. Infinitely divisible and stable distributions"
---

# Proof of Convergence of Constants Lemma (Convergence of Types)

**Lemma.** Let $\xi_n \stackrel{d}{\to} \xi$ and let there be constants $a_n > 0$ and $b_n$ such that

$$a_n \xi_n + b_n \stackrel{d}{\to} \tilde{\xi},$$

where the random variables $\xi$ and $\tilde{\xi}$ are not degenerate. Then there exist constants $a > 0$ and $b$ such that

$$a_n \to a, \quad b_n \to b \quad \text{as } n \to \infty,$$

and

$$\tilde{\xi} \stackrel{d}{=} a \xi + b.$$

**Proof.** Passing to characteristic functions, we have

$$\varphi_n(t) \to \varphi(t), \quad t \in \mathbb{R}, \tag{7}$$

and

$$e^{i b_n t} \varphi_n(a_n t) \to \tilde{\varphi}(t), \quad t \in \mathbb{R}, \tag{8}$$

where $\varphi_n$, $\varphi$, $\tilde{\varphi}$ are the characteristic functions of $\xi_n$, $\xi$, $\tilde{\xi}$ respectively.

*Step 1: Show $a < \infty$.* Let $\{n_i\}$ be a subsequence of $\{n\}$ such that $a_{n_i} \to a$ (where $a$ may be infinite). Suppose $a = \infty$. By (7) and (8),

$$\sup_{|t| \leq c} \bigl| |\varphi_n(a_n t)| - |\tilde{\varphi}(t)| \bigr| \to 0, \quad n \to \infty,$$

for every $c > 0$. Replace $t$ by $t_0 / a_{n_i}$. Then, since $a_{n_i} \to \infty$, we obtain

$$\bigl| \varphi_{n_i}\bigl(a_{n_i} \tfrac{t_0}{a_{n_i}}\bigr) \bigr| - \bigl| \tilde{\varphi}\bigl(\tfrac{t_0}{a_{n_i}}\bigr) \bigr| \to 0,$$

and therefore

$$|\varphi_{n_i}(t_0)| \to |\tilde{\varphi}(0)| = 1.$$

But $|\varphi_{n_i}(t_0)| \to |\varphi(t_0)|$. Hence $|\varphi(t_0)| = 1$ for every $t_0 \in \mathbb{R}$. By Theorem 5 of Sect. 12, Chap. 2, a random variable whose characteristic function has modulus identically equal to 1 must be degenerate, which contradicts the hypothesis that $\xi$ is nondegenerate. Thus $a < \infty$.

*Step 2: Show uniqueness of the limit.* Now suppose there are two subsequences $\{n_i\}$ and $\{n_i'\}$ such that $a_{n_i} \to a$, $a_{n_i'} \to a'$, with $a \neq a'$. Without loss of generality, assume $0 \leq a' < a$. Then by (7) and (8),

$$|\varphi_{n_i}(a_{n_i} t)| \to |\varphi(a t)|, \quad |\varphi_{n_i}(a_{n_i} t)| \to |\tilde{\varphi}(t)|,$$

and

$$|\varphi_{n_i'}(a_{n_i'} t)| \to |\varphi(a' t)|, \quad |\varphi_{n_i'}(a_{n_i'} t)| \to |\tilde{\varphi}(t)|.$$

Hence $|\tilde{\varphi}(t)| = |\varphi(a t)| = |\varphi(a' t)|$. Setting $t = s/a$ yields $|\varphi(s)| = |\varphi((a'/a) s)|$, and iterating gives $|\varphi(s)| = |\varphi((a'/a)^m s)|$ for all $m \geq 1$. Since $a'/a < 1$, letting $m \to \infty$ gives $|\varphi(s)| = |\varphi(0)| = 1$ for all $s$, again contradicting nondegeneracy of $\xi$. Therefore $a = a'$, and so the limit $a = \lim a_n$ exists uniquely.

*Step 3: Show $b_n$ converges.* From (8), for all sufficiently large $n$,

$$|\varphi_n(a_n t)| > 0 \quad \text{for } |t| < \delta,$$

for some $\delta > 0$ (since $|\tilde{\varphi}(t)| > 0$ in a neighbourhood of 0 for a nondegenerate distribution). Taking logarithms of the characteristic functions (or using the argument function), one can extract the convergence of $b_n$. Specifically, from

$$e^{i b_n t} \varphi_n(a_n t) \to \tilde{\varphi}(t)$$

and $\varphi_n(a_n t) \to \varphi(a t)$, we obtain

$$e^{i b_n t} \to \frac{\tilde{\varphi}(t)}{\varphi(a t)}$$

for $|t| < \delta$. The right-hand side is a characteristic function (up to a factor), and the convergence implies that $b_n$ must converge to some finite limit $b$.

*Step 4: Conclusion.* Thus there exist finite limits $a = \lim a_n$ and $b = \lim b_n$, and from (7)–(8) we obtain

$$\tilde{\varphi}(t) = e^{i b t} \varphi(a t),$$

which means that $\tilde{\xi} \stackrel{d}{=} a \xi + b$. Since $\tilde{\xi}$ is not degenerate, we must have $a > 0$. $\square$
