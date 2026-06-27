---
role: proof
locale: en
of_concept: hughes-plane-addition
source_book: gtm006
source_chapter: "IX"
source_section: "6. The Hughes Planes"
---

Let $T(a,b,c)$ be the ternary operation for $\mathcal{H}$, with $a \oplus b = T(1,a,b)$ and $a \otimes b = T(a,b,0)$. To find the value of $T(m,u,v)$, we consider the line $\ell$ which contains $(1,0,-m)$ and $(u,1,v)$, and let $(0,1,k)$ be the intersection of $\ell$ with the $y$-axis; then $k = T(m,u,v)$. Let $\ell$ be the line
$$xa + yb + zc + (xa' + yb' + zc')t = 0.$$

Then:
$$a - mc + (a' - mc')t = 0, \tag{5}$$
$$ua + b + vc + (ua' + b' + vc')t = 0. \tag{6}$$

Now let $m = 1$ in (5). Then $a - c + (a' - c')t = 0$. So if $t = 1$, we have $a + a' = c + c'$, and (6) becomes
$$u(a + a') + (b + b') + v(c + c') = 0,$$
or
$$(u + v) \cdot (a + a') + (b + b') = 0.$$

This last equation is that of the line joining $(\infty)$ and $(0,1,u+v)$, which meets the $y$-axis at $(0,1,u+v)$. Hence $k = u + v$, so $T(1,u,v) = u \oplus v = u + v$.
