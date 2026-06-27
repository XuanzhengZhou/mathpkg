---
role: proof
locale: en
of_concept: theorem-19-8
source_book: gtm055
source_chapter: "18-19"
source_section: "Section 20_Section_20"
---

Proof. As has been noted, the uniqueness requirement in the definition of a basis ensures that $\{x_n\}$ is linearly independent, so Proposition 19.7 applies. Hence the linear space $\mathcal{L}$ of all the coordinate sequences of vectors in $\mathcal{E}$ (with respect to the given basis $\{x_n\}$) is a Banach space in the norm (3). Moreover, it is clear that if we write $\Phi(a) = \sum_{n=0}^{\infty} \alpha_n x_n$ for each $a = \{\alpha_n\}$ in $\mathcal{L}$, then $\|\Phi(a)\| \leq \sup_N \|\sum_{n=0}^{N} \alpha_n x_n\| = \|a\|$. Thus $\Phi$

Example F. The functions $f_n(\lambda) = \lambda^n$ are continuous on the unit circle $Z$ for every $n$ in $\mathbb{Z}$ and therefore belong to $\mathcal{L}_p(Z)$ for all $p, 1 \leq p \leq +\infty$. Moreover,

$$\int_Z f_m f_{-n} d\theta = \int_Z \lambda^{m-n} d\theta(\lambda) = 2\pi \delta_{mn}, \quad m, n \in \mathbb{Z}.$$

Hence the two-way infinite sequence $\{u_n = f_n/\sqrt{2\pi}\}_{n=-\infty}^{+\infty}$ and the companion sequence $\{\alpha_n = f_{-n}/\sqrt{2\pi} = u_{-n}\}_{n=-\infty}^{+\infty}$ (regarded as a sequence in $\mathcal{L}_q(Z)$, where $q$ denotes the Hölder conjugate of $p$) constitute a biorthogonal system for $\mathcal{L}_p(Z)$, $1 \leq p < +\infty$ (for $p = 1$ set $q = +\infty$). This trigonometric biorthogonal system is of the greatest importance both intrinsically and for historical reasons. The (formal) series expansion of an integrable function $f$ in this system is the Fourier series of $f$, frequently denoted by $S(f)$. The generic term of $S(f)$ is $\alpha_n(f)u_n(\lambda) = (1/2\pi)\lambda^n \int_Z f(\zeta)\zeta^{-n} d\theta(\zeta)$, and it is customary to write $c_n$ (or $c_n(f)$ when necessary) for the $n$th Fourier coefficient of $f$:

$$c_n = \frac{1}{2\pi} \int_Z f(\zeta)\zeta^{-n} d\theta(\zeta).$$

Thus

$$S(f) = \sum_{n=-\infty}^{+\infty} c_n \lambda^n = \frac{1}{2\pi} \sum_{n=-\infty}^{+\infty} \lambda^n \int_Z f(\zeta)\zeta^{-n}

It turns out that if $f$ is a function in $\mathcal{L}_p(Z)$ for any $p$ such that $1 < p < +\infty$, then the sequence $\{s_N(f)\}_{N=0}^{\infty}$ converges to $f$ in the norm $\parallel \parallel_p$, but for $p = 1$ the situation is quite different; there exist functions $f$ in $\mathcal{L}_1(Z)$ such that the partial sums $s_N(f)$ do not converge to $f$ in the norm $\parallel \parallel_1$. In other words, the sequence $U = \{u_n\}_{n=-\infty}^{+\infty}$ is a basis (in the Cauchy sense) for $\mathcal{L}_p(Z)$, $1 < p < +\infty$, but is not a basis (even in the Cauchy sense) for $\mathcal{L}_1(Z)$. The proofs of these assertions are quite deep, and well beyond the scope of this discussion; the interested reader may consult [3; Ch. VIII, §§20, 22].

**Example G.** Let $U = \{u_n\}_{n=-\infty}^{+\infty}$ and $A = \{\alpha_n\}_{n=-\infty}^{+\infty}$ be as in the preceding example, and for each integer $n$ write $\rho_n$ for the Borel measure on $Z$ that is the indefinite integral of $\alpha_n$ with respect to $\theta$. If we set $R = \{\rho_n\}_{n=-\infty}^{+\infty}$, then the pair $(U, R)$ is a biorthogonal system for $\mathcal{C}(Z)$ (see Proposition 9.5 and Theorem 18.3), but the sequence $U$ is not a basis (even in the Cauchy sense) for $\mathcal{C}(Z)$. This is equivalent to saying that there exist continuous functions $f$ on $Z$ such that the partial sums $s_N(f)$ given by (6) do not converge uniformly to $f$, a fact that is well known, though a concrete counterexample is not easily constructed. (One may be found in [3; Chap. I, §44].)

As the foregoing examples show,
