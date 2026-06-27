---
role: proof
locale: en
of_concept: borel-theorem-smooth-functions
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The construction uses a smooth bump function $\rho: \mathbf{R} \to [0,1]$ with $\rho(t) = 1$ for $|t| \leq 1/2$ and $\rho(t) = 0$ for $|t| \geq 1$. Define
$$F(t, x) = \sum_{l=0}^{\infty} \frac{t^l}{l!} \rho(\mu_l t) f_l(x)$$
where $\{\mu_l\}$ increases to infinity.

**Well-definedness:** The RHS is well-defined for all $t$ since for any given $t$, only finitely many terms are nonzero (because $\rho(\mu_l t) = 0$ when $|t| > 1/\mu_l$). For $t \neq 0$, only finitely many terms are not identically zero on a neighborhood of $t$, so $F$ is smooth on $\mathbf{R} \setminus \{0\}$.

**Smoothness at $t = 0$:** Choose a compact neighborhood $K$ of $0$ in $\mathbf{R}^n$ contained in the common domain of the $f_l$'s, and let $M_l = \sup_{x \in K} |f_l(x)|$. Differentiating the RHS $s$ times with respect to $t$ gives a series dominated on $K$ by
$$C_s \sum_{l=s}^{\infty} \frac{|t|^{l-s}}{(l-s)!} \rho(\mu_l t) \mu_l^s M_l$$
where $C_s$ depends on $\rho$ and its first $s$ derivatives. Since $\rho(\mu_l t) = 0$ as soon as $|t| > 1/\mu_l$, this series is dominated by
$$C_s \sum_{p=0}^{\infty} \frac{M_{p+s}}{\mu_p^p \, p!}.$$
If the $\mu_l$ tend to infinity rapidly enough, this series converges for all $s$. Thus the termwise $s$-times differentiated series converges uniformly on $\mathbf{R} \times K$, proving $F$ is smooth.

**Verification of derivatives:** Since $\rho(\mu_l t) = 1$ for $|t| \leq 1/(2\mu_l)$, in a sufficiently small neighborhood of $t = 0$ the factor $\rho(\mu_l t)$ is identically $1$ for all $l$, so $F(t, x) = \sum_{l=0}^{\infty} \frac{t^l}{l!} f_l(x)$ as formal series, giving $\partial^l F / \partial t^l (0, x) = f_l(x)$.
