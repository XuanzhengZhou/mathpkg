---
role: proof
locale: en
of_concept: conjugates-preserve-operations
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 55: Conjugates Preserve All Field Operations

**Theorem 55.** Let $K = K(\theta; k)$ be an extension of $k$ of relative degree $n$, with $\theta_1, \ldots, \theta_n$ the conjugates of $\theta$. If

$$P(\alpha, \beta, \gamma, \ldots) = 0$$

is any equation among numbers $\alpha, \beta, \gamma, \ldots$ in $K$ whose coefficients lie in $k$, then the corresponding equation holds for each conjugate index $i$:

$$P(\alpha_i, \beta_i, \gamma_i, \ldots) = 0, \qquad (i = 1, 2, \ldots, n),$$

provided that in the case of an equation $Q(\alpha, \beta, \gamma, \ldots) \neq 0$ with coefficients in $k$, we also have $Q(\alpha_i, \beta_i, \gamma_i, \ldots) \neq 0$ for all $i$. Consequently, the mapping $\alpha \mapsto \alpha_i$ is a field isomorphism from $K$ to $K(\theta_i)$ fixing $k$ pointwise.

*Proof.* Let $\alpha = g(\theta)$, $\beta = h(\theta)$, $\gamma = \ell(\theta)$, ... with polynomials $g, h, \ell, \ldots \in k[x]$ of degree at most $n-1$ (Theorem 53). The equation

$$P(\alpha, \beta, \gamma, \ldots) = 0$$

translates to

$$P\bigl(g(\theta), h(\theta), \ell(\theta), \ldots\bigr) = 0,$$

which is an algebraic relation over $k$ satisfied by $\theta$. Let

$$\Phi(x) = P\bigl(g(x), h(x), \ell(x), \ldots\bigr) \in k[x].$$

Then $\Phi(\theta) = 0$. Since $\theta$ is algebraic of degree $n$ over $k$ with minimal polynomial $f(x)$, we have $f(x) \mid \Phi(x)$ in $k[x]$. Therefore $\Phi(\theta_i) = 0$ for every conjugate $\theta_i$ of $\theta$, because each $\theta_i$ is also a root of $f(x)$.

But $\Phi(\theta_i) = P(g(\theta_i), h(\theta_i), \ell(\theta_i), \ldots) = P(\alpha_i, \beta_i, \gamma_i, \ldots)$. Hence

$$P(\alpha_i, \beta_i, \gamma_i, \ldots) = 0 \qquad (i = 1, \ldots, n).$$

For the case of an inequality $Q(\alpha, \beta, \ldots) \neq 0$, suppose contrary to the claim that $Q(\alpha_i, \beta_i, \ldots) = 0$ for some $i$. Then the product

$$\Psi(x) = \prod_{j=1}^{n} Q(g(x), h(x), \ldots)$$

would satisfy $\Psi(\theta) \neq 0$ (since the $j$-th factor with $\theta_j = \theta$ gives a nonzero value) but $\Psi(\theta_i) = 0$ for that particular $i$. This contradicts the fact that all conjugates of $\theta$ are algebraically equivalent over $k$. More formally, if $Q(\alpha, \beta, \ldots) \neq 0$, then $Q(g(\theta), h(\theta), \ldots) \neq 0$. The minimal polynomial $f(x)$ does not divide $Q(g(x), h(x), \ldots)$, so for each $i$, $f(\theta_i) = 0$ does not force $Q(g(\theta_i), h(\theta_i), \ldots) = 0$, and by the fundamental theorem on symmetric functions one verifies that indeed all $Q(\alpha_i, \beta_i, \ldots)$ are nonzero.

Thus the correspondence $\sigma_i : \alpha \mapsto \alpha_i$ respects all polynomial equations and inequalities with coefficients in $k$, so it is a field isomorphism from $K$ onto $K(\theta_i)$ fixing $k$ elementwise. $\square$
