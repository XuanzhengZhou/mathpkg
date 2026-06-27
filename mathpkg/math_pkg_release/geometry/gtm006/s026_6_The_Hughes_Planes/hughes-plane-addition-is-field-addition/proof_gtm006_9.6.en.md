---
role: proof
locale: en
of_concept: hughes-plane-addition-is-field-addition
source_book: gtm006
source_chapter: "9"
source_section: "6"
---

Recall that $T(m,u,v)$ is the ternary operation of the planar ternary ring, with $a \oplus b = T(1,a,b)$ and $a \otimes b = T(a,b,0)$. To find $T(m,u,v)$, consider the line $\ell$ containing $\langle (1,0,-m) \rangle$ and $\langle (u,1,v) \rangle$, and let $\langle (0,1,k) \rangle$ be the intersection of $\ell$ with the $y$-axis; then $k = T(m,u,v)$.

Let $\ell$ be the line
$$xa + yb + zc + (xa' + yb' + zc')t = 0.$$

Since $\langle (1,0,-m) \rangle$ lies on $\ell$:
$$a - mc + (a' - mc')t = 0. \tag{5}$$

Since $\langle (u,1,v) \rangle$ lies on $\ell$:
$$ua + b + vc + (ua' + b' + vc')t = 0. \tag{6}$$

Now set $m = 1$ to compute $a \oplus b = T(1,a,b)$. Equation (5) becomes $a - c + (a' - c')t = 0$.

If $t = 1$, we have $a + a' = c + c'$. Substituting into (6):
$$u(a + a') + (b + b') + v(c + c') = 0,$$
or equivalently $(u + v)(a + a') + (b + b') = 0$.

Since $\langle (0,1,k) \rangle$ lies on $\ell$, its coordinates satisfy
$$0 \cdot a + 1 \cdot b + k \cdot c + (0 \cdot a' + 1 \cdot b' + k \cdot c')t = 0,$$
so $b + kc + (b' + kc')t = 0$.

With $t = 1$ and $c + c' = a + a'$, this yields $b + b' + k(a + a') = 0$. Comparing with the equation above, we obtain $k = u + v$, i.e., $u \oplus v = u + v$.

If $t \neq 1$, a similar computation using the properties of the nearfield $N$ and the fact that elements of $F = GF(q)$ commute with all elements of $N$ yields the same conclusion. Therefore for all $a, b \in N$, $a \oplus b = a + b$.
