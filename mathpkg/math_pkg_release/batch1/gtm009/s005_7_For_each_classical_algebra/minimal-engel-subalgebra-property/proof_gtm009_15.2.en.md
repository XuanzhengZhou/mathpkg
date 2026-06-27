---
role: proof
locale: en
of_concept: minimal-engel-subalgebra-property
source_book: gtm009
source_chapter: "15"
source_section: "15.2"
---

Begin with fixed, but arbitrary, $x \in K$, and consider the family $\{ \operatorname{ad}(z + cx) \mid c \in F \}$ of endomorphisms of $L$. Since $K_0 = L_0(\operatorname{ad} z)$ is a subalgebra of $L$ including $K$, these endomorphisms stabilize $K_0$, hence induce endomorphisms of the quotient vector space $L/K_0$ as well.

If $T$ is an indeterminate, we can therefore express the characteristic polynomial of $\operatorname{ad}(z + cx)$ as the product $f(T, c) g(T, c)$ of its characteristic polynomials on $K_0$ and on $L/K_0$, respectively.

Write $\dim K_0 = r$, $\dim L = n$. Then $f(T, c) = T^r + a_1(c)T^{r-1} + \cdots + a_r(c)$, where each $a_i(c)$ is a polynomial in $c$. The key observation is that when $c = 0$, $\operatorname{ad} z$ has characteristic polynomial $T^r \cdot (\text{something})$ on $K_0$ (since $K_0 = L_0(\operatorname{ad} z)$ means $\operatorname{ad} z$ is nilpotent on $K_0$) and some polynomial on $L/K_0$ with nonzero constant term (by minimality of $L_0(\operatorname{ad} z)$).

For all but finitely many $c \in F$, $g(T, c)$ has nonzero constant term, which means that $L_0(\operatorname{ad}(z + cx)) \subset K_0$ for all such $c$. By minimality of $K_0$, we must have $L_0(\operatorname{ad}(z + cx)) = K_0$ for all but finitely many $c \in F$.

Since $F$ is algebraically closed (hence infinite), and the condition $y \in L_0(\operatorname{ad}(z + cx))$ is equivalent to $(\operatorname{ad}(z + cx))^n y = 0$, which is a polynomial condition in $c$, the equality $L_0(\operatorname{ad}(z + cx)) = K_0$ holds for all $c \in F$. In particular, taking $c$ such that $z + cx = x$ (i.e., $c = 1$, $z = 0$ in an appropriate coordinate), we obtain $K_0 \subset L_0(\operatorname{ad} x)$ for all $x \in K$, as claimed.
