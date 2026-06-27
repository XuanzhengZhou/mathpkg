---
role: proof
locale: en
of_concept: tensor-product-maximum-modulus-theorem
source_book: gtm035
source_chapter: "11"
source_section: "11.4"
---
# Proof of Tensor Product Maximum Modulus Algebra Theorem

**Theorem 11.4.** Let $(A, X, \Omega, p)$ be a maximum modulus algebra over $\Omega$. Assume that $\Delta = \{|z| \leq 1\} \subset \Omega$. Fix $F \in \otimes^n A$ and fix $x^0 \in \Pi^{-1}(0, 0, \ldots, 0)$. Then

$$|F(x^0)| \leq \max_{\Pi^{-1}(\gamma)} |F|,$$

where $\Pi^{-1}(\gamma) = \{(x_1, \ldots, x_n) \in X^n : p(x_1) = \cdots = p(x_n), \; |p(x_1)| = 1\}$.

*Proof.* Let $\mu_j$ be representing measures on $p_j^{-1}(\partial \Delta)$ for the points $x_j^0 \in p^{-1}(0)$, so that for each $g \in A$,

$$\int_{p_j^{-1}(\partial \Delta)} g \, d\mu_j = g(x_j^0).$$

Define the product measure $\mu = \mu_1 \times \mu_2 \times \cdots \times \mu_n$ on $\Pi^{-1}(T^n)$, where $T^n = \{(z_1, \ldots, z_n) \in \Delta^n : |z_j| = 1\}$.

We claim that $\mu$ is a representing measure for the algebra $\otimes^n A$, i.e.,

$$\int_{\Pi^{-1}(T^n)} h \, d\mu = h(x^0), \quad h \in \otimes^n A.$$

Without loss of generality, consider $h(x) = g_1(x_1) g_2(x_2) \cdots g_n(x_n)$ with $g_j \in A$:

$$\int_{\Pi^{-1}(T^n)} h \, d\mu = \prod_{j=1}^n \int_{p_j^{-1}(\partial \Delta)} g_j(x_j) \, d\mu_j(x_j) = \prod_{j=1}^n g_j(x_j^0) = h(x^0),$$

proving the claim.

For $\phi \in C(T^n)$, define $\tilde{\phi}$ on $\Pi^{-1}(T^n)$ by $\tilde{\phi}(y) = \phi(\Pi(y))$. Then

$$\int_{\Pi^{-1}(T^n)} \tilde{\phi} \, d\mu = \int_{T^n} \phi \, d\mu_* = \left(\frac{1}{2\pi}\right)^n \int_{T^n} \phi \, d\theta_1 \cdots d\theta_n,$$

and consequently

$$\int_{\Pi^{-1}(T^n)} |\tilde{\phi}|^2 d\mu = \left(\frac{1}{2\pi}\right)^n \int_{T^n} |\phi|^2 d\theta_1 \cdots d\theta_n.$$

This allows us to lift each $\phi \in L^2(T^n, d\theta/(2\pi)^n)$ to an element $\tilde{\phi} \in L^2(\mu)$, defining a closed subspace $\mathcal{C} \subset L^2(\mu)$ isometric to $L^2(T^n)$.

Let $G_0$ be the orthogonal projection of $F$ onto $\mathcal{C}$ in $L^2(\mu)$. Then $G_0$ is identified with a function in $L^2(T^n)$. For any nonnegative integers $s_1, \ldots, s_n$, not all zero, we compute:

$$\int_{\Pi^{-1}(T^n)} F \, p_1^{s_1} \cdots p_n^{s_n} d\mu = \left(\frac{1}{2\pi}\right)^n \int_{T^n} G_0 \, e^{i s_1 \theta_1} \cdots e^{i s_n \theta_n} d\theta_1 \cdots d\theta_n.$$

Without loss of generality, $F(x) = g_1(x_1) \cdots g_n(x_n)$ with $g_j \in A$. Then the inner integral over $p_1^{-1}(\partial \Delta)$ yields $p_1^{s_1}(x_1^0) g_1(x_1^0) g_2(x_2) \cdots g_n(x_n) = 0$, since $p_1(x_1^0) = 0$. Hence

$$\int_{T^n} G_0 \, e^{i s_1 \theta_1} \cdots e^{i s_n \theta_n} d\theta = 0$$

for all $(s_1, \ldots, s_n)$ with at least one $s_j > 0$. This means all non-constant Fourier coefficients of $G_0$ vanish, so $G_0$ is constant on $T^n$, and in fact $G_0(0, \ldots, 0) = F(x^0)$.

Given $\epsilon > 0$, choose a relatively open set $\mathcal{U} \subset T^n$ containing the diagonal $\gamma$ such that

$$\sup_{\Pi^{-1}(\mathcal{U})} |F| \leq \sup_{\Pi^{-1}(\gamma)} |F| + \epsilon.$$

The Hardy space theory on the polydisk then yields the existence of $G \in H^\infty(T^n)$ such that $G(0, \ldots, 0) = G_0(0, \ldots, 0) = F(x^0)$ and

$$|G(z)| \leq \sup_{\Pi^{-1}(\gamma)} |F| + \epsilon$$

for all $z \in T^n$. Since $\epsilon$ is arbitrary, we obtain

$$|F(x^0)| = |G(0, \ldots, 0)| \leq \sup_{\Pi^{-1}(\gamma)} |F|,$$

as required. $\square$
