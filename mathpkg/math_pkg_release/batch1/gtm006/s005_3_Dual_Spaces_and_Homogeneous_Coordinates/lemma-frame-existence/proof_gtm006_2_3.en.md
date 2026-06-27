---
role: proof
locale: en
of_concept: lemma-frame-existence
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $e_1, \dots, e_{n+1}$ be a basis for $V$ and set $E_i = \langle e_i \rangle$ for $i = 1, \dots, n+1$, and $E_{n+2} = \langle e_1 + \cdots + e_{n+1} \rangle$. We must show that no $n+1$ of the $E_j$ are contained in a hyperplane.

Suppose some $n+1$ of them are contained in a hyperplane $H$. A hyperplane is the annihilator $U^{a_V}$ of a one-dimensional subspace $U = \langle u \rangle$ of $V'$, so $H$ consists of all points $\langle v \rangle$ with $u(v) = 0$. Thus there is a non-zero linear functional $f$ on $V$ such that $f$ vanishes on each of those $n+1$ points.

If $E_{n+2}$ is among the $n+1$ points, then the remaining $n$ are $n$ of the $E_i$ ($i = 1, \dots, n+1$), say all except $E_k$. Then $f(e_i) = 0$ for all $i \neq k$, and $f(e_1 + \cdots + e_{n+1}) = 0$. But $f(e_1 + \cdots + e_{n+1}) = \sum_i f(e_i) = f(e_k)$ since all other terms vanish. So $f(e_k) = 0$ as well. Then $f$ vanishes on all basis vectors, so $f = 0$, contradiction.

If $E_{n+2}$ is not among the $n+1$ points, then the $n+1$ points are all $E_1, \dots, E_{n+1}$. Then $f(e_i) = 0$ for all $i$, so $f = 0$, contradiction.

Hence no $n+1$ points lie in a hyperplane, so they form a frame. $\square$
