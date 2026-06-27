---
role: proof
locale: en
of_concept: proper-inclusion-of-polynomial-kernels
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

Conditions (i) and (ii) imply there exist polynomials $f_1, g_1$ such that

$$\mu = f f_1, \qquad f = g g_1, \qquad \deg g_1 > 0.$$

Set $g_2 = g_1 f_1$. Then $\deg g_2 < \deg \mu$, so $\mu$ is not a divisor of $g_2$. It follows that $g_2$ cannot annihilate all vectors of $E$; i.e., there exists $x \in E$ with $g_2(\varphi) x \neq 0$. Let $y = f_1(\varphi) x$. Then

$$f(\varphi) y = f(\varphi) f_1(\varphi) x = \mu(\varphi) x = 0,$$

so $y \in K(f)$. However,

$$g(\varphi) y = g(\varphi) f_1(\varphi) x = g_1(\varphi)^{-1} f(\varphi) f_1(\varphi) x.$$

Wait — more directly: $g(\varphi) y = g(\varphi) f_1(\varphi) x$. Since $f = g g_1$, we have $g_1(\varphi) g(\varphi) f_1(\varphi) x = f(\varphi) f_1(\varphi) x = \mu(\varphi) x = 0$. But $g_2(\varphi)x = g_1(\varphi) f_1(\varphi) x \neq 0$, which implies $g(\varphi) f_1(\varphi) x = g(\varphi) y \neq 0$. Hence $y \notin K(g)$. Thus $K(g)$ is a proper subspace of $K(f)$.
