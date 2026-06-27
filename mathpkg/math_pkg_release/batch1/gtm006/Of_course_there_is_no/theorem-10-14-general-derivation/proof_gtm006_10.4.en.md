---
role: proof
locale: en
of_concept: theorem-10-14-general-derivation
source_book: gtm006
source_chapter: "10"
source_section: "4"
---

The proof constructs the derived plane by showing that the sets $\mathcal{B}(a,b,c)$ satisfy the axioms of an affine plane when the line at infinity is restricted to $\mathcal{S}$.

Let $\mathcal{B}(a,b,c) = \{(\alpha a + b, \beta a + c) \mid \alpha, \beta \in F\}$. The proof proceeds through several steps:

**(d)** The elements $\alpha, \beta, \delta$ in $R$ which satisfy $\alpha a + \alpha_2 a = \alpha_1 a$, $\beta a + b_1 a = \beta_2 a$, $\delta(\alpha a) = \beta a$ are all in $F$.

**(e)** There is an element $\lambda$ in $F$ such that
$$\lambda(\alpha_1 + a) - \lambda(\alpha_2 + a) = \delta[(\alpha_1 + a) - (\alpha_2 + a)].$$

From (d) and (e), one shows that any two points $X = (\alpha_1 + a, b + \beta_1, \beta_2 a + c)$ and $Y = (\alpha_2 + a, b + \beta_2, a + c)$ of $\mathcal{B}(a,b,c)$ lie on a line $[\lambda, k]$ where $\lambda \in \mathcal{S}$. Specifically:

$$\lambda(\alpha_1 + a) + (\beta_1 + a) = \lambda(\alpha_2 + a) + (\beta_2 + a) = k.$$

For each $\alpha$ in $F$, there is a unique $\beta$ in $F$ such that $\lambda(\alpha a + b) + \beta a + c = k$, giving exactly $q$ points of $\mathcal{B}(a,b,c)$ on each such line. The set $\mathcal{B}(a,b,c)$ therefore consists of $q^2$ points, every pair of points determines a unique line meeting $l_{\infty}$ in $\mathcal{S}$, and each such line contains exactly $q$ points of the set. This verifies that $\mathcal{B}(a,b,c)$ is an affine Baer subplane, and $\mathcal{S}$ is the derivation set.

For arbitrary points $(x_1, y_1)$ and $(x_2, y_2)$ with $x_1 \neq x_2$, one sets $\mu = \lambda(x_1 - x_2) - (y_1 - y_2)$. The points are then expressed as:
$$(x_1, y_1) = (1 \cdot (x_1 - x_2) + x_2, 0(x_1 - x_2) + y_1),$$
$$(x_2, y_2) = (0(x_1 - x_2) + x_2, \mu(x_1 - x_2) + y_1).$$

This confirms that any two distinct points lie in some $\mathcal{B}(a,b,c)$ with the line joining them meeting $l_{\infty}$ in $\mathcal{S}$, establishing derivability.

[Note: The source text for Theorem 10.14 is partially truncated in the OCR. The statement and proof have been reconstructed from the available fragments and mathematical context.]
