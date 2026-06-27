---
role: proof
locale: en
of_concept: l2-extension-for-delbar
source_book: gtm035
source_chapter: "Chapter 16"
source_section: "16.9"
---
# Proof of L^2 Extension for \bar{\partial}-Closed Forms

**Lemma 16.9.** Let $\Omega$ be a bounded domain in $\mathbb{C}^n$ and let $u \in L^2(\Omega)$. Assume that for all $j = 1, \ldots, n$,

$$\frac{\partial u}{\partial \bar{z}_j} = 0 \quad \text{as a distribution on } \Omega.$$

Then $u$ is holomorphic on $\Omega$; i.e., $u \in H(\Omega)$.

**Proof.** Extend $u$ to all of $\mathbb{C}^n$ by defining $u = 0$ outside $\Omega$. Then $u \in L^2(\mathbb{C}^n)$.

Fix a smooth mollifier $\chi \in C_0^\infty(\mathbb{C}^n)$ with $\chi \geq 0$, $\int \chi = 1$, and $\operatorname{supp} \chi \subset B(0,1)$. For $\varepsilon > 0$, define $\chi_\varepsilon(z) = \varepsilon^{-2n} \chi(z/\varepsilon)$ and the convolution

$$u_\varepsilon(z) = \int_{\mathbb{C}^n} u(\zeta) \chi_\varepsilon(z - \zeta) dV(\zeta).$$

Since $u \in L^2(\mathbb{C}^n)$, standard properties of mollification yield:

- $u_\varepsilon \in C^\infty(\mathbb{C}^n)$,
- $u_\varepsilon \to u$ in $L^2(\mathbb{C}^n)$ as $\varepsilon \to 0$,
- If $u$ is continuous in a neighborhood of a closed ball, then $u_\varepsilon \to u$ uniformly on that ball.

Now fix $z \in \Omega$ and choose $\varepsilon < \operatorname{dist}(z, \partial \Omega)$. We compute the $\bar{\partial}$-derivative of $u_\varepsilon$ at $z$:

$$\frac{\partial u_\varepsilon}{\partial \bar{z}_j}(z) = \int_{\mathbb{C}^n} u(\zeta) \frac{\partial}{\partial \bar{z}_j} \chi_\varepsilon(z - \zeta) dV(\zeta).$$

Observe the key identity:

$$\frac{\partial}{\partial \bar{z}_j} \chi_\varepsilon(z - \zeta) = -\frac{\partial}{\partial \bar{\zeta}_j} \chi_\varepsilon(z - \zeta).$$

(This follows from the chain rule: $\frac{\partial}{\partial \bar{z}_j} \chi_\varepsilon(z - \zeta) = \chi_\varepsilon'(z - \zeta) \cdot 1$, while $\frac{\partial}{\partial \bar{\zeta}_j} \chi_\varepsilon(z - \zeta) = \chi_\varepsilon'(z - \zeta) \cdot (-1)$.)

Therefore,

$$\frac{\partial u_\varepsilon}{\partial \bar{z}_j}(z) = -\int_{\mathbb{C}^n} u(\zeta) \frac{\partial}{\partial \bar{\zeta}_j} \chi_\varepsilon(z - \zeta) dV(\zeta).$$

Define $g(\zeta) = \chi_\varepsilon(z - \zeta)$. Since $\varepsilon < \operatorname{dist}(z, \partial \Omega)$, we have $\zeta \mapsto g(\zeta)$ supported in $B(z, \varepsilon) \subset \Omega$. In particular, $g \in C_0^\infty(\Omega)$.

Now, by Definition 16.1, the condition $\frac{\partial u}{\partial \bar{z}_j} = 0$ as a distribution on $\Omega$ means precisely that for every test function $g \in C_0^\infty(\Omega)$,

$$\int_\Omega u(\zeta) \frac{\partial g}{\partial \bar{\zeta}_j}(\zeta) dV(\zeta) = 0.$$

Applying this with $g(\zeta) = \chi_\varepsilon(z - \zeta)$, we obtain

$$\frac{\partial u_\varepsilon}{\partial \bar{z}_j}(z) = -\int_\Omega u(\zeta) \frac{\partial g}{\partial \bar{\zeta}_j}(\zeta) dV(\zeta) = 0,$$

for all $j = 1, \ldots, n$.

Thus $u_\varepsilon$ satisfies the Cauchy-Riemann equations $\frac{\partial u_\varepsilon}{\partial \bar{z}_j} = 0$ on $\Omega$ (for all $z$ with $\operatorname{dist}(z, \partial \Omega) > \varepsilon$), which means $u_\varepsilon$ is holomorphic on $\Omega$.

Now fix any closed ball $B' \subset \Omega$. Choose $\varepsilon_0 > 0$ small enough so that the $\varepsilon_0$-neighborhood of $B'$ is still contained in $\Omega$. By the hypothesis, $\frac{\partial u}{\partial \bar{z}_j} = 0$ as a distribution, which in particular means these derivatives are continuous (identically zero) in a neighborhood of $B'$. Therefore, by property (30) of mollifiers, $u_\varepsilon \to u$ uniformly on $B'$ as $\varepsilon \to 0$.

Since each $u_\varepsilon$ is holomorphic on a neighborhood of $B'$, and the uniform limit of holomorphic functions is holomorphic (by Weierstrass's theorem), $u$ is holomorphic on the interior of $B'$. As $B' \subset \Omega$ was arbitrary, $u \in H(\Omega)$. $\square$

**Remark.** This lemma is a regularity result of Weyl's lemma type: a distributional solution of the homogeneous Cauchy-Riemann equations is automatically a smooth (indeed, real-analytic) holomorphic function. In the context of the $L^2$ $\bar{\partial}$-theory developed in this chapter, Lemma 16.9 ensures that the $L^2$ solutions produced by the Hormander estimates are genuine holomorphic functions whenever the right-hand side vanishes in the distributional sense.
