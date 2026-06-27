---
role: proof
locale: en
of_concept: function-extension-from-submanifold
source_book: gtm035
source_chapter: "Chapter 17"
source_section: "17.4"
---
# Proof of Extension of Functions from a Submanifold

**Lemma 17.4.** Fix a compact set $K$ on $\Sigma$. Let $u$ be a function of class $C^e$ defined on $\Sigma$. Then there exists a function $U$ of class $C^1$ in $\mathbb{C}^n$ with

(a) $U \equiv u$ on $K$.

(b) There exists a constant $C$ with

$$\left| \frac{\partial U}{\partial \bar{z}_j}(z) \right| \leq C \cdot d(z)^{e-1}, \quad z \in \mathbb{C}^n, \; j = 1, \ldots, n,$$

where $d(z) = \operatorname{dist}(z, \Sigma)$.

*Proof.* Let $m = 2n - k$ be the codimension of $\Sigma$ and let $\rho_1, \ldots, \rho_m$ be local defining functions for $\Sigma$ of class $C^e$. Consider the vectors

$$\xi_\nu = \left( \frac{\partial \rho_\nu}{\partial \bar{z}_1}, \ldots, \frac{\partial \rho_\nu}{\partial \bar{z}_n} \right), \quad \nu = 1, \ldots, m.$$

Suppose that $\xi_1, \ldots, \xi_m$ fail to span $\mathbb{C}^n$. Then there exists $c = (c_1, \ldots, c_n) \neq 0$ with $\sum_{j=1}^{n} c_j (\partial \rho_\nu / \partial \bar{z}_j) = 0$ for $\nu = 1, \ldots, m$. In other words, the tangent vector $\sum_{j=1}^{n} c_j \partial/\partial \bar{z}_j$ annihilates $\rho_1, \ldots, \rho_m$, and hence $\Sigma$ has a complex tangent at $x_0$, which is contrary to assumption.

Hence $\xi_1, \ldots, \xi_m$ span $\mathbb{C}^n$, so we can find $v_1, \ldots, v_n$ with $\xi_{v_1}, \ldots, \xi_{v_n}$ linearly independent. By continuity, the vectors

$$\left( \frac{\partial \rho_{v_j}}{\partial \bar{z}_1}, \ldots, \frac{\partial \rho_{v_j}}{\partial \bar{z}_n} \right)_x, \quad j = 1, \ldots, n$$

are linearly independent and form a basis for $\mathbb{C}^n$ for all $x$ in some neighborhood $\omega_0$ of $x_0$.

Relabel $\rho_{v_1}, \ldots, \rho_{v_n}$ to read $\rho_1, \ldots, \rho_n$. Define functions $h_1, \ldots, h_n$ in $\omega_0$ by

$$\left( \frac{\partial u}{\partial \bar{z}_1}, \ldots, \frac{\partial u}{\partial \bar{z}_n} \right)(x) = \sum_{i=1}^{n} h_i(x) \left( \frac{\partial \rho_i}{\partial \bar{z}_1}, \ldots, \frac{\partial \rho_i}{\partial \bar{z}_n} \right)_x.$$

Set $u_1 = u - \sum_i h_i \rho_i$. Then $u_1 = u$ on $\Sigma$ and $\bar{\partial} u_1 = -\sum_i \bar{\partial} h_i \cdot \rho_i$.

Proceed inductively. Define functions $h_I$ on $\omega_0$, where $I = (\beta_1, \ldots, \beta_n)$ is a multi-index, by

$$\bar{\partial} h_I = \sum_{i=1}^{n} h_{Ij} \, \bar{\partial} \rho_i,$$

where $Ij$ denotes the multi-index obtained by adding 1 to the $j$-th component. Define functions $u_N$, $N = 1, 2, \ldots, e-1$, by

$$u_N = u_{N-1} + \frac{(-1)^N}{N!} \sum_{|I|=N} h_I \rho_I,$$

where $\rho_I = \rho_1^{\beta_1} \cdots \rho_n^{\beta_n}$. Then $h_I \in C^{e-N}(\omega_0)$ if $|I| = N$, and $u_N \in C^{e-N}(\omega_0)$.

One verifies by induction that

$$\bar{\partial} u_N = \frac{(-1)^N}{N!} \sum_{|I|=N} \bar{\partial} h_I \cdot \rho_I.$$

In particular, for $N = e-1$, we have $u_{e-1} = u$ on $\Sigma$ and

$$\bar{\partial} u_{e-1} = \frac{(-1)^{e-1}}{(e-1)!} \sum_{|I|=e-1} \bar{\partial} h_I \cdot \rho_I.$$

Since each $h_I \in C^1(\omega_0)$ for $|I| = e-1$ and $\rho_I$ vanishes to order $e-1$ on $\Sigma$, we obtain

$$\left| \frac{\partial u_{e-1}}{\partial \bar{z}_j}(z) \right| \leq \text{const} \cdot d(z)^{e-1}.$$

**Partition of unity.** For each $x_0 \in K$ we choose a neighborhood $\omega_{x_0}$ in $\mathbb{C}^n$ of the above type. Finitely many of these neighborhoods, say $\omega_1, \ldots, \omega_g$, cover $K$.

Choose $\chi_1, \ldots, \chi_g \in C^\infty(\mathbb{C}^n)$ with $\operatorname{supp} \chi_\alpha \subset \omega_\alpha$, $0 \leq \chi_\alpha \leq 1$, and $\sum_{\alpha=1}^g \chi_\alpha = 1$ on $K$.

By the above construction, applied to $\chi_\alpha u$ in place of $u$, choose $U_\alpha$ in $C^1(\omega_\alpha)$ with $U_\alpha = \chi_\alpha u$ on $\Sigma \cap \omega_\alpha$, $\operatorname{supp} U_\alpha \subset \operatorname{supp} \chi_\alpha u$, and

$$\left| \frac{\partial U_\alpha}{\partial \bar{z}_j}(z) \right| \leq C_\alpha \cdot d(z)^{e-1}, \quad z \in \omega_\alpha, \; j = 1, \ldots, n.$$

Since $\operatorname{supp} U_\alpha \subset \omega_\alpha$, we define $U_\alpha = 0$ outside $\omega_\alpha$ to obtain a $C^1$-function on all of $\mathbb{C}^n$, with the estimate holding for all $z$.

Put $U = \sum_{\alpha=1}^g U_\alpha$. Then $U \in C^1(\mathbb{C}^n)$, and for $z \in K$,

$$U(z) = \sum_{\alpha=1}^g U_\alpha(z) = \sum_{\alpha=1}^g \chi_\alpha(z) u(z) = u(z) \sum_{\alpha} \chi_\alpha = u(z).$$

For every $z$,

$$\frac{\partial U}{\partial \bar{z}_j}(z) = \sum_{\alpha=1}^g \frac{\partial U_\alpha}{\partial \bar{z}_j}(z),$$

so

$$\left| \frac{\partial U}{\partial \bar{z}_j}(z) \right| \leq \sum_{\alpha=1}^g C_\alpha \cdot d(z)^{e-1} = C \cdot d(z)^{e-1},$$

where $C = \sum C_\alpha$. This completes the proof. $\square$
