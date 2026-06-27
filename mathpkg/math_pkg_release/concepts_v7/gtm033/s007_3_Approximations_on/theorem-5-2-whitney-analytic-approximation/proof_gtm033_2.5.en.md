---
role: proof
locale: en
of_concept: theorem-5-2-whitney-analytic-approximation
source_book: gtm033
source_chapter: "2"
source_section: "5. Analytic Approximations"
---

# Proof of Theorem 5.2 (Whitney): Analytic Approximation of $C^r$ Maps

**Theorem 5.2 (Whitney).** Let $U \subset \mathbb{R}^m$ be open and $f: U \to \mathbb{R}$ a $C^r$ map, $0 \leqslant r < \infty$. Let $v: \mathbb{R}^m \to [0,1]$ be a $C^\infty$ map of bounded support, equal to $1$ on a neighborhood of a compact set $K \subset U$. Set $h(x) = v(x)f(x)$. Let $\delta: \mathbb{R}^m \to \mathbb{R}$, $\delta(x) = \exp(-|x|^2)$. Let $T = 1/\int_{\mathbb{R}^m} \delta$. Let $\varepsilon > 0$. Then for $\kappa > 0$ sufficiently large, the convolution $g$ of $h$ with the function $T\kappa^m \delta(\kappa x)$ is analytic and satisfies $\|g - f\|_{r,K} < \varepsilon$.

*Proof.* The proof is a direct computation using properties of the Gaussian convolution kernel. Set

$$g(x) = (h * \phi_\kappa)(x) = \int_{\mathbb{R}^m} h(y)\, T\kappa^m \exp(-\kappa^2|x-y|^2)\,dy$$

where $\phi_\kappa(x) = T\kappa^m \exp(-\kappa^2|x|^2)$. Since $\phi_\kappa$ is real-analytic (the Gaussian is analytic) and $h$ has compact support, $g$ is real-analytic on $\mathbb{R}^m$.

For the approximation estimate, one verifies that as $\kappa \to \infty$, the kernel $\phi_\kappa$ approaches the Dirac delta. Standard convolution estimates give:

$$\|g - h\|_{r,K} \to 0 \quad \text{as } \kappa \to \infty.$$

Since $h = f$ on a neighborhood of $K$ (because $v = 1$ there), we have $\|g - f\|_{r,K} = \|g - h\|_{r,K} < \varepsilon$ for $\kappa$ sufficiently large.

The key observation is that the Gaussian kernel is analytic, and the convolution of a compactly supported continuous function with an analytic kernel yields an analytic function. This is what distinguishes Theorem 5.2 from ordinary smooth convolution: the use of the Gaussian (rather than a merely $C^\infty$ bump function) produces analytic approximations.

QED
