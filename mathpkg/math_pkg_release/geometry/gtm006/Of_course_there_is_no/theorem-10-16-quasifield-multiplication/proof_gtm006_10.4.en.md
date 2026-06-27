---
role: proof
locale: en
of_concept: theorem-10-16-quasifield-multiplication
source_book: gtm006
source_chapter: "10"
source_section: "4"
---

The line $[\alpha + \beta t, 0]'$ is on $(0,0)' = (0,0)$ and on $(-1, \alpha + \beta t)' = (-1 + \alpha t, \beta t)$. If $\beta \neq 0$, then $[\alpha + \beta t, 0]'$ is not a line of the form $\mathcal{B}(x, y, z)$, since $(0,0)$ is on $\mathcal{B}(x, y, z)$ if and only if $\mathcal{B}(x, y, z) = \mathcal{B}(w, 0, 0)$ for some $w$, and $(-1 + \alpha t, \beta t)$ is on no line of the form $\mathcal{B}(w, 0, 0)$.

Now Eq. (1) yields:
$$-r + asu = 0,$$
$$ar - s + vas = -b,$$

and these can be solved for $r$ and $s$ to give:
$$r = -abu(a^2 u + av - 1)^{-1},$$
$$s = -b(a^2 u + av - 1)^{-1}.$$

Substituting for $r$ and $s$ in (2) gives:
$$b(acu - hu)(a^2 u + av - 1)^{-1} = d,$$
$$b(c - ahu - hv)(a^2 u + av - 1)^{-1} = -m,$$

and solving these two equations for $h$ and $m$ gives:
$$h = ac - b^{-1}dg(a),$$
$$m = bc - ad - dv/u,$$

where $g(a) = a^2 + (v/u)a - 1/u$. Every irreducible quadratic over $GF(q)$ is satisfied by some element in $GF(q^2)$, and so $\lambda^2 - v\lambda - u$ is an arbitrary irreducible quadratic over $GF(q)$. Hence (see Exercise 10.7), $g$ is also arbitrary.

It is now immediate that we can choose the parameters to give us any Hall quasifield for $\mathcal{A}_H$, since $a * (c + \lambda d) = ac + \lambda ad$ follows from Theorem 10.16.
