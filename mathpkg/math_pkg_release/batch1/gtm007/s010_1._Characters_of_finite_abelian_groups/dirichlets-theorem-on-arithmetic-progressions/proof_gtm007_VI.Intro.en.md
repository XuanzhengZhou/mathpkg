---
role: proof
locale: en
of_concept: dirichlets-theorem-on-arithmetic-progressions
source_book: gtm007
source_chapter: "VI"
source_section: "§1–§4"
---

The proof proceeds in several stages.

**1. Characters of finite abelian groups (§1).** For a fixed modulus $m$, consider the multiplicative group $G(m) = (\mathbb{Z}/m\mathbb{Z})^*$ of order $\phi(m)$. A *character modulo $m$* is a homomorphism $\chi: G(m) \to \mathbb{C}^*$. The characters form the dual group $\widehat{G(m)}$, also of order $\phi(m)$. The orthogonality relation holds:
$$\sum_{\chi} \chi(x) = \begin{cases} \phi(m) & \text{if } x \equiv 1 \pmod{m} \\ 0 & \text{otherwise.} \end{cases}$$

**2. $L$-functions (§3).** For each character $\chi$ modulo $m$, define the Dirichlet $L$-function:
$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s},$$
which converges absolutely for $\Re(s) > 1$ and (for $\chi \neq 1$) conditionally for $\Re(s) > 0$. For the principal character $\chi = 1$, $L(s, 1) = \zeta(s) \prod_{p \mid m} (1 - p^{-s})$, which has a simple pole at $s = 1$.

**3. Non-vanishing at $s = 1$ (§3.4).** Consider the product over all characters:
$$\zeta_m(s) = \prod_{\chi} L(s, \chi).$$
This is a Dirichlet series with non-negative coefficients. If $L(1, \chi) = 0$ for some $\chi \neq 1$, then $\zeta_m(s)$ would be holomorphic at $s = 1$ and hence (by Landau's theorem, Proposition 7) would converge for all $\Re(s) > 0$. But the $p$-th factor of $\zeta_m(s)$ dominates $(1 - p^{-\phi(m)s})^{-1}$, whose series diverges at $s = 1/\phi(m)$, a contradiction. Hence $L(1, \chi) \neq 0$ for all $\chi \neq 1$.

**4. Density and infinitude (§4).** For $s > 1$, define
$$g_a(s) = \sum_{p \equiv a \pmod{m}} \frac{1}{p^s}.$$
By the orthogonality relations,
$$g_a(s) = \frac{1}{\phi(m)} \sum_{\chi} \chi(a)^{-1} f_\chi(s), \quad \text{where } f_\chi(s) = \sum_{p \nmid m} \frac{\chi(p)}{p^s}.$$
For $\chi = 1$, $f_1(s) \sim \log \frac{1}{s-1}$ as $s \to 1^+$. For $\chi \neq 1$, since $L(1, \chi) \neq 0$, the function $\log L(s, \chi)$ remains bounded near $s = 1$, whence $f_\chi(s)$ remains bounded. Therefore
$$g_a(s) \sim \frac{1}{\phi(m)} \log \frac{1}{s-1} \quad (s \to 1^+),$$
which implies that the set $P_a = \{p \text{ prime} : p \equiv a \pmod{m}\}$ has analytic density $1/\phi(m)$. In particular, $P_a$ is infinite since a finite set has density zero.
