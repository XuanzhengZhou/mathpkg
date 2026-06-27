---
role: proof
locale: en
of_concept: gelfand-spectral-radius-formula
source_book: gtm015
source_chapter: "55"
source_section: "55.1"
---

# Proof of Gelfand spectral radius formula

(55.1) Theorem. If $x \in A$ then $r(x) = \lim_{n \to \infty} \

(the convention is that $1/r(x) = +\infty$ when $r(x) = 0$) as follows: define $G(0) = 0$; if $0 < |\mu| < 1/r(x)$ then $|\mu^{-1}| > r(x)$ and we define

$$G(\mu) = f[R(\mu^{-1})].$$

It follows from (51.6) that $G$ is differentiable at every point of the punctured disc $D_1 - \{0\}$. {On the punctured disc, $G$ is the composite of the differentiable functions $\mu \mapsto \mu^{-1}$ and $\lambda \mapsto f[R(\lambda)]$.}

Consider the (possibly smaller) disc

$$D_2 = \{\mu \in \mathbb{C} : |\mu| < 1/\|x\|\}$$

(with the convention that $1/\|x\| = +\infty$ when $x = 0$). If $0 < |\mu| < 1/\|x\|\}$ then $|\mu^{-1}| > \|x\|\) and therefore (50.4)

$$R(\mu^{-1}) = \sum_{n=0}^{\infty} \mu^{n+1}x^n;$$

since $f$ is continuous and linear, we conclude that

$$G(\mu) = \sum_{n=0}^{\infty} f(x^n)\mu^{n+1}.$$

The representation (*) is trivially valid at $\mu = 0$ (recall that $G(0) = 0$ by definition). Thus the series representation (*) of $G$ is valid on the entire open disc $D_2$, and in particular $G$ is analytic on $D_2$. But $G$ is known to be analytic on the (possibly larger) disc $D_1$, hence is representable on $D_1$ by a power series; by the theorem on uniqueness of coefficients, the series (*) must also represent $G$ on $D_1$. In particular, for each $\mu \in D_1$ the sequence $f(x^n)\mu^{n+1}$ is bounded (indeed, it is a null sequence).

In summary

{Postlude: Since $r(x) \leq \|x^n\|^{1/n}$ for all $n$, and the right side is known to converge to $r(x)$, we infer that $\lim \|x^n\|^{1/n} = \inf \|x^n\|^{1/n}$.}

If $x \in B \subset A$, where $B$ is a closed subalgebra of $A$ that contains 1, the evident inclusion $\sigma_A(x) \subset \sigma_B(x)$ implies that $r_A(x) \leq r_B(x)$; although the inclusion may be proper (51.14), the inequality is never strict:
