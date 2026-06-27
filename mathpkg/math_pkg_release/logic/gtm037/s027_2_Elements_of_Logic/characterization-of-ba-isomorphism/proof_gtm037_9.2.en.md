---
role: proof
locale: en
of_concept: characterization-of-ba-isomorphism
source_book: gtm037
source_chapter: "9"
source_section: "2"
---

Assume $(i) \Rightarrow (ii)$. If $f$ is an isomorphism onto $\mathfrak{A}'$, then $f$ maps $A$ onto $A'$ and preserves the order in both directions, so $(ii)$ holds.

Now assume $(ii)$. If $fx = fy$, then $fx \leq' fy$ and $fy \leq' fx$, so $x \leq y$ and $y \leq x$, hence $x = y$. Thus $f$ is one-one.

Now we apply the characterization of Boolean algebra homomorphisms (9.13(iv)). For any $x, y \in A$ we have $fx \leq' f(x + y)$ and $fy \leq' f(x + y)$, since $x \leq x + y$ and $y \leq x + y$. Thus $fx +' fy \leq' f(x + y)$. Let $fx +' fy = fz$ (since $f$ is onto $A'$). Then $fx \leq' fz$, so $x \leq z$. Similarly $y \leq z$, so $x + y \leq z$. But $fz = fx +' fy \leq' f(x + y)$ implies $z \leq x + y$. Thus $z = x + y$, and hence $fx +' fy = fz = f(x + y)$.

Next, choose $x$ so that $fx = 0'$. Then $0 \leq x$, so $f0 \leq' fx = 0'$ and hence $f0 = 0'$. Similarly $f1 = 1'$. The preservation of complement follows from the preservation of join and the order condition, establishing that $f$ is an isomorphism.
