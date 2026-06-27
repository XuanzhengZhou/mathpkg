---
role: proof
locale: en
of_concept: fermat-curve-affine-point-count
source_book: gtm059
source_chapter: "1"
source_section: "6. Application to the Fermat Curve"
---

For $u \in F$, let
$$N_a(u) = \#\{x \in F : x^d = u\}.$$
Then
$$N_a(u) = \begin{cases}
1 & \text{if } u = 0,\\
0 & \text{if } u \neq 0,\ u \text{ is not a } d\text{th power in } F,\\
d & \text{if } u \neq 0,\ u \text{ is a } d\text{th power in } F.
\end{cases}$$
Therefore
$$N_a(u) = \sum_{a \bmod d} \chi_a(u).$$

We have
$$N = \sum_{a,b,c} \sum_{u+v+w=0} \chi_a(u)\chi_b(v)\chi_c(w),$$
where the sum over $u, v, w$ is taken over triples of elements of $F$ lying on the line $u + v + w = 0$. The sum over $a, b, c$ is taken over elements in $\mathbb{Z}/d\mathbb{Z}$.

The term for which $a = b = c = 0$ yields a contribution of $q^2$, that is the number of points on the line in $F$.

Next, suppose that in the remaining sum, one of $a, b, c$ is $0$ but not all are $0$ in $\mathbb{Z}/d\mathbb{Z}$. Say $a = 0$ but $b \neq 0$. Then we may write the sum
$$\sum_{u+v+w=0} \sum_{\text{certain } u, w} \chi_a(u)\chi_c(w) \sum_{\text{all } v \in F} \chi_b(v),$$
and the sum on the far right is $0$. This shows that all the terms in the sum with one, but not all, of $a, b, c$ equal to $0$ give a contribution $0$. Hence we get
$$N = q^2 + \sum_{0 < a,b,c < d} \sum_{u+v+w=0} \chi_a(u)\chi_b(v)\chi_c(w),$$
where the sum over $a, b, c$ is taken over positive integers satisfying the indicated inequality.

If $w = 0$ then $\chi_c(w) = 0$. We may therefore assume that in the inner sum, we have $w \neq 0$. We then put
$$u = u'w \quad \text{and} \quad v = v'w.$$
The inner sum then has the form
$$\sum_{w \neq 0} \chi_{a+b+c}(w) \sum_{u'+v'=-1} \chi_a(u')\chi_b(v').$$

If $a + b + c \not\equiv 0 \pmod{d}$, then the sum on the left is $0$. Otherwise it is $q-1$, which we assume from now on. Since $0 < a, b, c < d$, there is no such triple $(a,b,c)$ with $a + b \equiv 0 \pmod{d}$, because any accompanying $c$ would have to equal $d$. Hence the sum over $a, b, c$ is for $a + b \not\equiv 0 \pmod{d}$, and then $c$ is uniquely determined.

Changing back the variables $u', v'$ to $u'' = -u'$, $v'' = -v'$ and taking into account the value of the Jacobi sum yields the expression as stated in the theorem.
