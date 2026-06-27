---
role: proof
locale: en
of_concept: l2-completeness-theorem
source_book: gtm012
source_chapter: "4. Hilbert Spaces and Fourier Series"
source_section: "§1. An inner product in ℂ, and the space L²"
---

# Proof of $L^2$ completeness and inner product structure

**Theorem 1.3.** The inner product in $\mathbf{L}^2$ defined by

$$(F, G) = \lim_{n \to \infty} (u_n, v_n), \quad \text{where } u_n \to F,\; v_n \to G \text{ in } \mathbf{L}^2,$$

satisfies the identities (2)–(6) of the inner product on $\mathcal{C}$. If we define

$$\|F\| = (F, F)^{1/2},$$

then $\|\cdot\|$ is a norm on $\mathbf{L}^2$. The space $\mathbf{L}^2$ is complete with respect to this norm.

*Proof.* **Inner product properties.** The identities (2)–(6) for the inner product on $\mathbf{L}^2$ follow immediately from (17) and the corresponding identities (2)–(6) for the inner product on $\mathcal{C}$, by passing to the limit.

The Schwarz inequality also holds in $\mathbf{L}^2$: for $F, G \in \mathbf{L}^2$ with $u_n \to F$, $v_n \to G$ in $\mathbf{L}^2$,

$$|(F, G)| = \lim_{n \to \infty} |(u_n, v_n)| \leq \lim_{n \to \infty} \|u_n\| \|v_n\| = \|F\| \|G\|.$$

The triangle inequality for $\|\cdot\|$ on $\mathbf{L}^2$ then follows exactly as in Corollary 1.2, using the Schwarz inequality just established. Together with positivity and homogeneity (which follow from (6) and (2) in the limit), $\|\cdot\|$ is a norm on $\mathbf{L}^2$.

**Completeness.** Suppose $(F_n)_{1}^{\infty} \subset \mathbf{L}^2$ is a Cauchy sequence with respect to this norm. For each $n$, since $F_n \in \mathbf{L}^2$, there exists a sequence in $\mathcal{C}$ converging to $F_n$ in $\mathbf{L}^2$. Choose $v_n \in \mathcal{C}$ such that

$$\|F_n - F_{v_n}\| < \frac{1}{n},$$

where $F_{v_n}$ denotes the distribution associated to the constant sequence $(v_n, v_n, v_n, \ldots)$.

Now $(F_{v_n})$ is Cauchy in $\mathbf{L}^2$: given $\varepsilon > 0$, choose $N$ such that $n, m \geq N$ implies $\|F_n - F_m\| < \varepsilon/3$ and $1/n, 1/m < \varepsilon/3$. Then

$$\|F_{v_n} - F_{v_m}\| \leq \|F_{v_n} - F_n\| + \|F_n - F_m\| + \|F_m - F_{v_m}\| < \frac{1}{n} + \frac{\varepsilon}{3} + \frac{1}{m} < \varepsilon.$$

But $\|F_{v_n} - F_{v_m}\| = \|v_n - v_m\|$ (by definition of the norm on $\mathbf{L}^2$ via the limit (17); for constant sequences this reduces to the $\mathcal{C}$-norm). Hence $(v_n)_{1}^{\infty}$ is a $\|\cdot\|$-Cauchy sequence in $\mathcal{C}$. Therefore, by the definition of $\mathbf{L}^2$, the sequence $(v_n)$ defines a distribution $F \in \mathbf{L}^2$ such that $v_n \to F$ in $\mathbf{L}^2$.

It remains to show $F_n \to F$ in $\mathbf{L}^2$. For each $n$,

$$\|F_n - F\| \leq \|F_n - F_{v_n}\| + \|F_{v_n} - F\| < \frac{1}{n} + \|F_{v_n} - F\|.$$

Now $\|F_{v_n} - F\|^2 = \lim_{m \to \infty} \|v_n - v_m\|^2$ by definition (17) and the fact that $v_m \to F$ in $\mathbf{L}^2$. Since $(v_m)$ is Cauchy, this limit tends to $0$ as $n \to \infty$. Hence $\|F_n - F\| \to 0$, proving completeness. ∎
