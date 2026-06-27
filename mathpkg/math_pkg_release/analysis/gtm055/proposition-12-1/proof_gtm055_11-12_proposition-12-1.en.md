---
role: proof
locale: en
of_concept: proposition-12-1
source_book: gtm055
source_chapter: "11-12"
source_section: "Section 13_Section_13"
---

PROOF. Since it is clear that (i) implies (ii), it will suffice to show that (ii) implies (iii) and that (iii) implies (i). To see that (ii) implies (iii), choose $\delta > 0$ such that $\|x\| = \|x - 0\| \leq \delta$ implies $\|Tx\| = \|Tx - T0\| \leq 1$. Then $Tx$ belongs to the ball $\mathcal{F}_{1/\delta}$ whenever $x$ belongs to the unit ball $\mathcal{E}_1$, and from this it follows at once that $T$ is bounded. Finally, to see that (iii) implies (i), let $x_0$ be a vector in $\mathcal{E}$ and let $\varepsilon$ be positive. Then for $\delta = \varepsilon/(\|T\| + 1)$ and $\|x - x_0\| < \delta$, we have

$$\|Tx - Tx_0\| \leq \|T\| \|x - x_0\| < \varepsilon.$$

Thus $T$ is continuous at $x_0$.

The main point of the last part of the foregoing argument is that the inequality

$$\|Tx_1 - Tx_2\| \leq \|T\| \|x_1 - x_2\|$$

is valid for an arbitrary pair of vectors $x_1, x_2$ in $\mathcal{E}$. Thus a continuous, and therefore bounded, linear transformation $T$ between two normed spaces is automatically Lipschitzian. In particular, $T$ is uniformly continuous (see Problem 4F).

We deal here solely with continuous linear transformations between two normed spaces because that is the case of principal concern and because the simple criterion of boundedness is applicable in this situation. If $\mathcal{E}$ and $\mathcal{F}$ are merely quasinormed spaces, then no similarly simple criterion for continuity exists. All the more, if $\mathcal{E}$ and $\mathcal{F}$ are arbitrary topological linear spaces, then no such simple criterion for the continuity of a linear transformation of $\mathcal{E}$ into $\mathcal{F}$ can be given. Nevertheless, appropriate counterparts of many of the

Example B. Let $p$ be an extended real number, $1 \leq p \leq +\infty$. For any infinite sequence of complex numbers $x = \{\xi_n\}_{n=0}^{\infty}$ in $(\ell_p)$, set

$$V \{\xi_0, \xi_1, \ldots, \xi_n, \ldots\} = \{0, \xi_0, \ldots, \xi_{n-1}, \ldots\}. \tag{3}$$

Since $\|x\|_p = \|Vx\|_p$ for every $x$ in $(\ell_p)$, it is clear that $V$ is a bounded linear transformation on $(\ell_p)$ and that $\|V\| = 1$. The transformation $V$ is known as the unilateral shift on $(\ell_p)$.

Example C. Let $d = \{\delta_0, \delta_1, \ldots\}$ be a fixed bounded sequence of scalars, and let $p$ be an extended real number, $1 \leq p \leq +\infty$. Define $M_d$ by writing

$$M_d x = \{\delta_0 \xi_0, \delta_1 \xi_1, \ldots\} \tag{4}$$

for an arbitrary sequence $x = \{\xi_n\}_{n=0}^{\infty}$ in $(\ell_p)$. Once again, it is easily seen that $M_d$ is a bounded linear transformation on $(\ell_p)$, and that, in fact, $\|M_d\| = \sup_n |\delta_n| = \|d\|_\infty$. The linear transformation $M_d$ is known as multiplication by $d$.

Example D. On each space $(\ell_p)$, $1 \leq p \leq +\infty$, the product $S = VM_d$ does the following:

$$\{\xi_0, \xi_1, \ldots\} \xrightarrow{S} \{0, \delta_0 \xi_0, \delta_1 \xi_1, \ldots\}.$$

This transformation, known as the weighted unilateral shift on $(\ell_p)$ with weight sequence $d$, is also bounded and again we have $\|

arbitrary element of $(\ell_\infty)^\#$, then multiplication by $d$ is the transformation carrying each $x = \{\xi_n\}_{n=-\infty}^{+\infty}$ in $(\ell_p)^\#$ to the sequence

$$M_d x = dx = \{\delta_n \xi_n\}_{n=-\infty}^{+\infty},$$

and $M_d$ is a bounded linear transformation on $(\ell_p)^\#$ with $\|M_d\| = \|d\|_\infty$. Likewise, the linear transformation $T = UM_d$, where $U$ denotes the bilateral shift of Example E, is a bounded linear transformation on $(\ell_p)^\#$ with $\|T\| = \|d\|_\infty$. The action of $T$ can be better viewed using the notation introduced in that example:

$$\{..., \xi_{-1}, [\xi_0], \xi_1, ...\} \xrightarrow{T} \{..., \delta_{-2}, \xi_{-2}, [\delta_{-1}, \xi_{-1}], \delta_0 \xi_0, ...\}.$$

The transformation $T$ is called the weighted bilateral shift on $(\ell_p)^\#$ with weight sequence $d$.

**Example G.** Let $X$ be a nonempty compact Hausdorff space, let $f_0$ be a fixed function in $\mathcal{C}(X)$ (Ex. 3D), and define $M_{f_0}$ by

$$(M_{f_0} g)(x) = f_0(x)g(x)$$

for all $x$ in $X$ and all $g$ in $\mathcal{C}(X)$. Then $M_{f_0}$ is a bounded linear transformation on $\mathcal{C}(X)$ known as multiplication by $f_0$. Clearly $\|M_{f_0}\| = \|f_0\|_\infty$.

**Example H.** Choose a fixed point $x_0$ in a compact Hausdorff space $X$, and define $\varphi(f) = f(x_0)$ for every $f$ in $\mathcal{C}(X)$. Then $\varphi$ is

$\mathcal{L}(\mathcal{E})$ are properly known as bounded linear operators on $\mathcal{E}$. In this book, however, we shall not be concerned with nonlinear analysis, and we shall have only a limited interest in unbounded transformations. Accordingly, we frequently refer to the elements of $\mathcal{L}(\mathcal{E})$ simply as operators, or as bounded operators, on $\mathcal{E}$. A bounded operator $T$ on $\mathcal{E}$ with $\| T \| \leq 1$ is called a contraction on $\mathcal{E}$.

It is easily seen that if $\mathcal{E}$ and $\mathcal{F}$ are arbitrary normed spaces, then $\mathcal{L}(\mathcal{E}, \mathcal{F})$ is a linear submanifold of the full space of linear transformations of $\mathcal{E}$ into $\mathcal{F}$ (Ch. 2, p. 19), and is therefore a linear space in its own right. In order to verify this, it need only be checked that if $S$ and $T$ are bounded, and if $\lambda$ is a scalar, then $S + T$ and $\lambda S$ are bounded too. But for an arbitrary vector $x$ in $\mathcal{E}$ we have

$$\| (S + T) x \| \leq \| S x \| + \| T x \| \leq \| S \| \| x \| + \| T \| \| x \|$$

and

$$\| (\lambda S) x \| = \| \lambda (S x) \| \leq |\lambda| \| S \| \| x \|,$$

and from these inequalities it follows not only that $S + T$ and $\lambda S$ are bounded, but also that

$$\| S + T \| \leq \| S \| + \| T \|$$

and

$$\| \lambda S \| = |\lambda| \| S \|.$$

Since it is clear that $\| S \| = 0$ implies $S = 0$, we see that $\| \|$, as defined in (2), is, in fact, a norm on $\mathcal{L}(\mathcal{E}, \mathcal{F})$. Is the norm

for all $m \geq N$. (Recall that closed balls in a metric space are closed sets.) Thus we see that $T - T_m$ is bounded and satisfies $\| T - T_m \| \leq \varepsilon$ for all $m \geq N$. From this it follows, in the first place, that $T = (T - T_m) + T_m$ is also bounded, and, secondly, that $\| T - T_m \| \to 0$.

With the aid of the Hahn–Banach theorem (Th. 14.3) it can be shown, conversely, that if $\mathcal{F}$ is not complete, and if $\mathcal{E} \neq (0)$, then $\mathcal{L}(\mathcal{E}, \mathcal{F})$ is not complete. See Problem 14E.

Bounded linear transformations can be multiplied as well as added and subtracted.
