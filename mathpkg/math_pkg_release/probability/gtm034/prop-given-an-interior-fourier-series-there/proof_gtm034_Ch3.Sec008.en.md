---
role: proof
locale: en
of_concept: prop-given-an-interior-fourier-series-there
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: The extension of

$$\psi_i(\theta) = \sum_{k=0}^{\infty} c_k e^{ik\theta}$$

is

$$f_i(z) = \sum_{k=0}^{\infty} c_k z^k, \quad |z| \leq 1,$$

which is an inner function. Uniqueness follows from the fact that an analytic function in $|z| < 1$ is determined by its boundary values. The proof for $\psi_e$ and $f_e$ is the same, with $|z| \ge

$g$ is continuous everywhere and also bounded. The continuity of $g$ suffices to apply Morera's theorem: one integrates $g$ around a point $z_0$ with $|z_0| = 1$ and verifies that the integral is zero. Morera's theorem then guarantees that $g$ is analytic at $z_0$. Since $z_0$ is arbitrary, $g$ is analytic everywhere. But such a function, if in addition bounded, reduces to a constant by Liouville's theorem. Thus $g(z) \equiv c$ which implies P3.

A pair of useful inner and outer functions are $f_i$ and $f_e$ defined by
