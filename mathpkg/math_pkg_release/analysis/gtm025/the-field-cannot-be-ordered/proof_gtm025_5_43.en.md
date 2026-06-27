---
role: proof
locale: en
of_concept: "the-field-cannot-be-ordered"
source_book: gtm025
source_chapter: "Set Theory and Algebra"
source_section: "5.43"
---

Assuming the existence in $K$ of a subset $P$ as in (5.7), we have $i \in P$ or $-i \in P$. If $i \in P$, then $i^2 = -1 \in P$, which contradicts (5.8). If $-i \

Since $r_2 - r_1$ can be made arbitrarily small, it follows that $\varphi(x) = x$.

(5.46) The functional equation $\varphi(x + y) = \varphi(x) + \varphi(y)$ has $2^c$ discontinuous solutions on $R$. In fact, regard $R$ as a vector space over $Q$ (3.17.c) and let $B$ be a Hamel basis for $R$ over $Q$ (3.19). For each $x \in R$ let $\alpha_x$ denote that unique function from $B$ into $Q$ as in (3.20) such that $x = \sum_{b \in B} \alpha_x(b) b$. Now for each $f \in R^B$ define $\varphi_f: R \rightarrow R$ by the rule

$$\varphi_f(x) = \sum_{b \in B} \alpha_x(b) f(b).$$

The reader can easily verify that each such $\varphi_f$ satisfies the desired functional equation and that $\varphi_f(rx) = r\varphi_f(x)$ for $r \in Q$, $x \in R$. Thus $\varphi_f(r) = r\varphi_f(1)$ ($r \in Q$), so that if $\varphi_f$ is continuous, then $\varphi_f(x) = x\varphi_f(1)$ for all $x \in R$. Since $\varphi_f(1)$ has just $c$ possible values we see that there are just $c$ continuous $\varphi_f$'s. But $\overline{R^B} = c^c = 2^c$ [see (4.34)] and $f \neq g$ in $R^B$ implies $\varphi_f \neq \varphi_g$, so there exist $2^c$ discontinuous $\varphi_f$'s. The preceding paragraph shows that the additional requirement that $\varphi(xy) = \varphi(x) \varphi(y)$ forces $\varphi$ to be continuous.

To illustrate the bizarre nature of some of these additive functions, define $\psi(x) = \sum_{b \in B} \alpha_x(b)$ for $x \in R$, i.e., $\psi = \varphi_f$ where $f(b) = 1$ for each $

Proof. Applying (5.47) and (5.48), we write

$$|z + w|^2 = (z + w)(\bar{z} + \bar{w}) = z\bar{z} + w\bar{w} + z\bar{w} + \bar{z}w$$
$$= |z|^2 + |w|^2 + 2\operatorname{Re}(z\bar{w})$$
$$\leq |z|^2 + |w|^2 + 2|z\bar{w}|$$
$$= |z|^2 + |w|^2 + 2|z| |w|$$
$$= (|z| + |w|)^2.$$

This shows that $|z + w| \leq |z| + |w|$. Equality holds if and only if $\operatorname{Re}(z\bar{w}) = |z\bar{w}|$, and so by (5.48) if and only if $z\bar{w}$ is a nonnegative real number. If $z = 0$, take $\alpha = 1$ and $\beta = 0$. If $w = 0$, take $\alpha = 0$ and $\beta = 1$. If $z \neq 0$ and $w \neq 0$ and $z\bar{w}$ is a positive real number $\beta$, then $z|w|^2 = z\bar{w}w = \beta w$, and we can take $\alpha = |w|^2 > 0$.

(5.50) Geometric interpretation. As the reader will already know, the field $K$ can be very usefully regarded as the Euclidean plane $R \times R$, in which the point $(a, b)$ corresponds to the complex number $a + bi$. Thus the Euclidean distance between $(a, b)$ and $(0, 0)$ is the absolute value of $a + bi$. Conjugation is simply reflection in the $X$-axis.
