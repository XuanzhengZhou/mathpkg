---
role: proof
locale: en
of_concept: closure-of-vf-contains-uf
source_book: gtm041
source_chapter: "8"
source_section: "8.6"
---

The closure $\overline{V_f(\sigma_0)}$ is the set of adherent points of $V_f(\sigma_0)$. We are to prove that every point $u$ in $U_f(\sigma_0)$ is an adherent point of $V_f(\sigma_0)$. In other words, given $u$ in $U_f(\sigma_0)$ and given $\varepsilon > 0$, we must find a real $t$ such that $|f(\sigma_0 + it) - u| < \varepsilon$.

Since $u \in U_f(\sigma_0)$, there exist real numbers $\mu_n$ such that $u = \sum_{n=1}^{\infty} a(n) e^{-\sigma_0 \lambda(n)} e^{-i\mu_n}$. Hence

$$f(\sigma_0 + it) - u = \sum_{n=1}^{\infty} a(n)e^{-\sigma_0 \lambda(n)}(e^{-it \lambda(n)} - e^{-i \mu_n}).$$

The idea of the proof is to split the sum into two parts, $\sum_{n=1}^{N} + \sum_{n=N+1}^{\infty}$. Choose $N$ so the second part is small (possible by absolute convergence), then choose $t$ to make the first part small via Kronecker's theorem.

For the given $\varepsilon$, choose $N$ so that

$$\left| \sum_{n=N+1}^{\infty} a(n)e^{-\sigma_0 \lambda(n)}(e^{-it \lambda(n)} - e^{-i \mu_n}) \right| < \frac{\varepsilon}{2}.$$

This is possible because the series converges absolutely at $\sigma_0$ and $|e^{-it\lambda(n)} - e^{-i\mu_n}| \leq 2$. Then

$$|f(\sigma_0 + it) - u| < \left| \sum_{n=1}^{N} a(n)e^{-\sigma_0 \lambda(n)}(e^{-it \lambda(n)} - e^{-i \mu_n}) \right| + \frac{\varepsilon}{2}.$$

Set $M = 1 + \sum_{n=1}^{N} |a(n)| e^{-\sigma_0 \lambda(n)}$, so that

$$\sum_{n=1}^{N} |a(n)| e^{-\sigma_0 \lambda(n)} < M.$$

The problem reduces to finding $t$ and integers $k_1, \ldots, k_N$ such that

$$|t \lambda(n) - \mu_n - 2\pi k_n| < \frac{\varepsilon}{2M} \qquad (n = 1, 2, \ldots, N).$$

Since $|e^{i\theta} - 1| \leq |\theta|$ for real $\theta$, we have

$$\left| \sum_{n=1}^{N} a(n)e^{-\sigma_0 \lambda(n)}(e^{-it \lambda(n)} - e^{-i \mu_n}) \right| = \left| \sum_{n=1}^{N} a(n)e^{-\sigma_0 \lambda(n)} e^{-i\mu_n} \left( e^{i(\mu_n - t\lambda(n))} - 1 \right) \right|$$

$$\leq \sum_{n=1}^{N} |a(n)| e^{-\sigma_0 \lambda(n)} |e^{i(t \lambda(n) - \mu_n)} - 1|$$

and hence, assuming (4),

$$\sum_{n=1}^{N} |a(n)| e^{-\sigma_0 \lambda(n)} |e^{i(t \lambda(n) - \mu_n)} - 1| < \frac{\varepsilon}{2M} \sum_{n=1}^{N} |a(n)| e^{-\sigma_0 \lambda(n)} < \frac{\varepsilon}{2}.$$

Thus the proof will be complete if we can find $t$ and integers $k_1, \ldots, k_N$ satisfying (4). We now apply Kronecker's theorem. Express each $\lambda(n)$ in terms of the basis $B = \{\beta(1), \beta(2), \ldots\}$:

$$\lambda(n) = r_{n,1} \beta(1) + \cdots + r_{n,q(n)} \beta(q(n)),$$

where the $r_{n,j}$ are rational numbers. Let $Q$ be the largest of the integers $q(1), \ldots, q(N)$, and let $D$ be the least common multiple of the denominators of the rational numbers $r_{i,j}$ that arise from $\lambda(1), \ldots, \lambda(N)$ (there are at most $q(1) + \cdots + q(N)$ such numbers).

Define

$$\theta_m = \frac{\beta(m)}{2\pi D}, \qquad \alpha_m = \frac{y_m}{2\pi D} \qquad (m = 1, 2, \ldots, Q),$$

where $y_m$ are the imaginary parts of the numbers $z_m$ that determine $u$ (so that $\mu_n = \sum_{m=1}^{Q} r_{n,m} y_m$ with $r_{n,m} = 0$ for $m > q(n)$). The numbers $\theta_1, \ldots, \theta_Q$ are linearly independent over the integers because $B$ is a basis.

By Kronecker's theorem, for any $\delta > 0$, there exists a real $t'$ and integers $h_1, \ldots, h_Q$ such that

$$|t' \theta_m - \alpha_m - h_m| < \delta \qquad (m = 1, 2, \ldots, Q).$$

Multiplying by $2\pi D$, this becomes

$$|t' \beta(m) - y_m - 2\pi D h_m| < 2\pi D \delta \qquad (m = 1, 2, \ldots, Q).$$

Set $t = t'$. For each $n = 1, \ldots, N$, we have

$$t \lambda(n) - \mu_n = \sum_{m=1}^{Q} r_{n,m} \big( t \beta(m) - y_m \big).$$

Since each $r_{n,m}$ has denominator dividing $D$, we can set

$$k_n = \sum_{m=1}^{Q} r_{n,m} D h_m,$$

which is an integer. Then

$$|t \lambda(n) - \mu_n - 2\pi k_n| = \left| \sum_{m=1}^{Q} r_{n,m} \big( t \beta(m) - y_m - 2\pi D h_m \big) \right| \leq \sum_{m=1}^{Q} |r_{n,m}| \cdot 2\pi D \delta.$$

Choosing $\delta$ sufficiently small (depending on $\varepsilon$, $M$, $N$, and the coefficients $r_{n,m}$) ensures that condition (4) is satisfied. This completes the proof.
