---
role: proof
locale: en
of_concept: projective-limit-has-no-torsion
source_book: gtm059
source_chapter: "7"
source_section: "1"
---

Suppose otherwise. Then there exists a fixed power $p^{\nu}$ and an element $u = \varprojlim_n u_n$ in $U$ such that $u^{p^{\nu}} = 1$. Writing $u = (u_n)$ with $u_n \in U_n$ and $N_{m,n}(u_m) = u_n$ for $m \ge n$, the condition $u^{p^{\nu}} = 1$ means that $u_n^{p^{\nu}} = 1$ for all $n$. Thus each $u_n$ is a $p^{\nu}$-th root of unity.

Now consider the norm maps. For $m \ge n$, $N_{m,n}(u_m) = u_n$. If $u_n$ is a primitive $p^{\nu}$-th root of unity for some $n$, then taking preimages under successive norm maps would force the existence of $p^{\nu}$-th roots of unity in $U_m$ for arbitrarily large $m$. But the only roots of unity in the local unit groups $U_n$ are the $p$-power roots of unity $\mu_{p^{n+1}}$, and these are bounded in order by the ramification index. For sufficiently large $m$, $U_m$ cannot contain a non-trivial $p^{\nu}$-th root of unity unless $\nu$ is bounded by the structure of the unit group, leading to a contradiction.

Therefore $U$ contains no non-trivial $\mathbb{Z}_p$-torsion elements.
