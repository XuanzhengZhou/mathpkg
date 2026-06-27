---
role: proof
locale: en
of_concept: random-variable-25
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 5 (Lattice structure from characteristic function values)

**Theorem 5.** Let $\varphi_{\xi}(t)$ be the characteristic function of the random variable $\xi$.

(a) If $|\varphi_{\xi}(t_0)| = 1$ for some $t_0 \neq 0$, then $\xi$ is a lattice random variable concentrated at the points $a + nh$, $h = 2\pi/|t_0|$, that is,

$$\sum_{n=-\infty}^{\infty} P\{\xi = a + nh\} = 1,$$

where $a$ is a constant.

(b) If $|\varphi_{\xi}(t)| = |\varphi_{\xi}(\alpha t)| = 1$ for two different points $t$ and $\alpha t$, where $\alpha$ is irrational, then $\xi$ is degenerate, that is $P\{\xi = a\} = 1$, where $a$ is some number.

(c) If $|\varphi_{\xi}(t)| \equiv 1$, then $\xi$ is degenerate.

## Proof

**(a)** If $|\varphi_{\xi}(t_0)| = 1$, $t_0 \neq 0$, there exists a number $a$ such that $\varphi(t_0) = e^{it_0 a}$. Then

$$e^{it_0 a} = \int_{-\infty}^{\infty} e^{it_0 x} dF(x) \implies 1 = \int_{-\infty}^{\infty} e^{it_0 (x-a)} dF(x)$$
$$\implies 1 = \int_{-\infty}^{\infty} \cos t_0(x-a) dF(x) \implies \int_{-\infty}^{\infty} [1 - \cos t_0(x-a)] dF(x) = 0.$$

Since $1 - \cos t_0(x-a) \geq 0$, it follows from property H (Subsection 2 of Sect. 6) that

$$1 = \cos t_0(\xi - a) \quad (P\text{-a.s.}),$$

which means $t_0(\xi - a) \in 2\pi\mathbb{Z}$ almost surely, i.e., $\xi = a + \frac{2\pi n}{t_0}$ for some $n \in \mathbb{Z}$. Setting $h = 2\pi/|t_0|$ yields (a).

**(b)** From $|\varphi_{\xi}(t)| = |\varphi_{\xi}(\alpha t)| = 1$ and (a), $\xi$ is concentrated on two lattices: $a + n h_1$ where $h_1 = 2\pi/|t|$, and $a' + m h_2$ where $h_2 = 2\pi/|\alpha t| = h_1/\alpha$. Since $\alpha$ is irrational, the ratio $h_1/h_2$ is irrational, and the intersection of these two lattices can be nonempty only if each lattice reduces to a single point. Hence $\xi$ is degenerate.

**(c)** If $|\varphi_{\xi}(t)| \equiv 1$, then in particular $|\varphi_{\xi}(t)| = |\varphi_{\xi}(\sqrt{2}\,t)| = 1$ for any $t \neq 0$, and since $\sqrt{2}$ is irrational, part (b) implies degeneracy. Alternatively, this follows directly from (a) since the condition holds for all $t$, forcing the lattice spacing to be arbitrarily small, hence zero.
