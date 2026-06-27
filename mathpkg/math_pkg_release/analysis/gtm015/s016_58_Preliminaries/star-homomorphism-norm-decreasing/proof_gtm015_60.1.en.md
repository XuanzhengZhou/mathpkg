---
role: proof
locale: en
of_concept: star-homomorphism-norm-decreasing
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Unital *-Homomorphisms are Norm-Decreasing

Proof. {By ‘*-homomorphism’ is meant an algebra homomorphism $\varphi$ such that $\varphi(a^*) = \varphi(a)^*$ for all $a$.} It is elementary that $\sigma_B(\varphi(a)) \subset \sigma_A(a)$ for all $a$ in $A$ (if $a - \lambda 1$ is invertible in $A$, then $\varphi(a) - \lambda 1 = \varphi(a - \lambda 1)$ is invertible in $B$), therefore $r_B(\varphi(a)) \leq r_A(a)$. If $a$ is self-adjoint then so is $\varphi(a)$, and (58.3) yields

$$\|\varphi(a)\| = r_B(\varphi(a)) \leq r_A(a) = \|a\|.$$

If $a \in A$ is arbitrary then $a^*a$ is self-adjoint, therefore

$$\|\varphi(a)\|^2 = \|\varphi(a)^*\varphi(a)\| = \|\varphi(a^*a)\| \leq \|a^*a\| = \|a\|^2,$$

thus $\|\varphi(a)\| \leq \|a\|$.

The case that $B = \mathcal{L}(H)$, $H$ a

If $x = (x_i)$ and $y = (y_i)$ are in $H$, then the coordinatewise sum $(x_i + y_i)$ is also in $H$; this follows at once from the relations

$$\|x_i + y_i\|^2 + \|x_i - y_i\|^2 = 2\|x_i\|^2 + 2\|y_i\|^2.$$

Also, if $x = (x_i) \in H$ and $\lambda \in \mathbb{C}$, then $(\lambda x_i) \in H$ results from the relations $\|\lambda x_i\| = |\lambda| \|x_i\|$. Clearly $H$ is a vector space relative to the coordinatewise linear operations

$$x + y = (x_i + y_i), \quad \lambda x = (\lambda x_i).$$

From the relations

$$(x_i | y_i) = \frac{1}{4} \left\{ \|x_i + y_i\|^2 - \|x_i - y_i\|^2 + i \|x_i + iy_i\|^2 - i \|x_i - iy_i\|^2 \right\}$$

it follows that $\sum_{\iota \in I} |(x_i | y_i)| < \infty$; the formula

$$(x | y) = \sum_{\iota \in I} (x_i | y_i)$$

(the limit of the net of finite subsums) evidently defines a sesquilinear form on $H$ such that

$$(x | x) = \sum_{\iota \in I} \|x_i\|^2.$$

In particular, $(x | x) > 0$ when $x \neq \theta$, thus $H$ is an inner product space (41.9); the norm derived from the inner product is given by

$$\|x\| = (x | x)^{1/2} = \left( \sum_{\iota \in I} \|x_i\|^2 \right)^{1/2}.$$

It remains to show that $H$ is complete relative to this norm. Suppose $x_n$ is a Cauchy sequence in $H$,
