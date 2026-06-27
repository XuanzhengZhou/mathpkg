---
role: proof
locale: en
of_concept: theorem-10-12-multiple-derivation-andre-plane
source_book: gtm006
source_chapter: "10"
source_section: "3"
---

We prove some auxiliary results first.

**(a)** If $a \neq 0$ in $K$, then $x^{q-1} = a$ has $0$ or $q-1$ solutions.

*Proof of (a).* If both $g$ and $h$ in $K$ are solutions, that is $g^{q-1} = h^{q-1} = a$, then clearly $(gh^{-1})^{q-1} = 1$. But since $K^*$ is a cyclic group of order $q^2 - 1$, it has a unique cyclic subgroup of order $q - 1$, and so $x^{q-1} = 1$ has $q-1$ solutions. It is now easy to see that each of the elements $gx$ satisfies $(gx)^{q-1} = a$, and there are no other solutions. $\square$

**(b)** If $a \neq 0$ in $K$, if $b, c$ are elements of $K$, and if we consider the equation $ax^{q+1} + bx + c = 0$, then this equation has $0$, $1$, $2$, or $q+1$ solutions.

Now we are given $m$ in $\mathcal{S}_t$, and $k$, and wish to consider the set of points $(x, y)$ in $\mathcal{A}$ satisfying $mx^{q+1} + y = k$, i.e., the set of points $(x, k - mx^{q+1})$, as $x$ ranges over $F$. If a line of $\mathcal{A}$ contains two such points, let the line be $[a, b]$ and the points $(x, k - mx^{q+1})$ and $(y, k - mx^{q+1})$. So:

$$ax + k - mx^{q+1} = b = ay + k - my^{q+1}.$$

But we now have an equation of the type of (b) above, with at least two solutions, and so it has exactly $q+1$ solutions. Thus our line contains exactly $q+1$ points in the distinguished set.

So the set consists of $q^2$ points, every two points are on a common line and each of these common lines contains exactly $q+1$ points of the set. Therefore the set is an affine plane of order $q$ (see Exercise 3.14).

Its points at infinity are the points $(a)$ satisfying $ax + k - mx^{q+1} = ay + k - my^{q+1}$, or

$$a(x - y) = m(x^{q+1} - y^{q+1}) = m(x - y)^{q+1},$$

or

$$a = m(x - y)^{q}.$$

But then

$$a^{q+1} = m^{q+1}(x - y)^{q^{2}-1} = t_i$$

since $(x-y)^{q^{2}-1} = 1$ for all $x, y$ with $x \neq y$. So $(a)$ is in $\mathcal{S}_{t_i}$.

Since at least $q+1$ points on $[\infty]$ must be on lines joining two points of our special set, all $q+1$ of the points of $\mathcal{S}_{t_i}$ will occur in this way. This shows that each $\mathcal{S}_{t_i}$ serves as the set of points at infinity for such a Baer subplane, confirming that the multiply derived plane is precisely an Andr\'{e} plane.

If one of the $t_i$ is $1$, but some element of $F^*$ is not among the $t_j$, then the construction is adjusted via a collineation mapping the collection $\mathcal{S}_t$ onto itself while permuting the distinguished sets appropriately. This completes the identification of the multiply derived desarguesian plane as an Andr\'{e} plane.
