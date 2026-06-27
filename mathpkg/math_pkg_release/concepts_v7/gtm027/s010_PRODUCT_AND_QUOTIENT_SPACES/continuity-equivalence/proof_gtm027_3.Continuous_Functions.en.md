---
role: proof
locale: en
of_concept: continuity-equivalence
source_book: gtm027
source_chapter: "3"
source_section: "Continuous Functions"
---

# Proof of Equivalent Conditions for Continuity

**Theorem.** If $X$ and $Y$ are topological spaces and $f$ is a function on $X$ to $Y$, then the following statements are equivalent.

(a) The function $f$ is continuous.

(b) The inverse of each closed set is closed.

(c) The inverse of each member of a subbase for the topology for $Y$ is open.

(d) For each $x$ in $X$ the inverse of every neighborhood of $f(x)$ is a neighborhood of $x$.

(e) For each $x$ in $X$ and each neighborhood $U$ of $f(x)$ there is a neighborhood $V$ of $x$ such that $f[V] \subset U$.

(f) For each net $S$ (or $\{S_n, n \in D\}$) in $X$ which converges to a point $s$, the composition $f \circ S$ (or $\{f(S_n), n \in D\}$) converges to $f(s)$.

(g) For each subset $A$ of $X$, $f[A^{-}] \subset f[A]^{-}$.

(h) For each subset $B$ of $Y$, $f^{-1}[B]^{-} \subset f^{-1}[B^{-}]$.

*Proof.*

**(a) $\leftrightarrow$ (b):** This is a simple consequence of the fact that the inverse of a function preserves relative complements; that is, $f^{-1}[Y \sim B] = X \sim f^{-1}[B]$ for every subset $B$ of $Y$. If $f$ is continuous, the inverse of every open set is open; equivalently, the inverse of every closed set is closed.

**(b) $\rightarrow$ (c):** Each member of a subbase for the topology of $Y$ is open. By (b), the inverse of each closed set is closed, which is equivalent (via complements) to the inverse of each open set being open. Hence the inverse of each subbase element is open.

**(c) $\rightarrow$ (d):** Let $U$ be a neighborhood of $f(x)$. Then $U$ contains an open set $V$ with $f(x) \in V \subset U$. The set $V$ is a union of finite intersections of subbase elements; consequently there is a finite intersection $W$ of members of the subbase such that $f(x) \in W \subset V$. Then $f^{-1}[W]$ is an open neighborhood of $x$ which is a subset of $f^{-1}[V]$; consequently $f^{-1}[V]$ is a neighborhood of $x$, and therefore $f^{-1}[U] \supset f^{-1}[V]$ is a neighborhood of $x$.

**(d) $\rightarrow$ (e):** Assuming (d), if $U$ is a neighborhood of $f(x)$, then $f^{-1}[U]$ is a neighborhood of $x$ such that $f[f^{-1}[U]] \subset U$.

**(e) $\rightarrow$ (f):** Assuming (e), let $S$ be a net in $X$ which converges to a point $s$. Then if $U$ is a neighborhood of $f(s)$ there is a neighborhood $V$ of $s$ such that $f[V] \subset U$, and since $S$ is eventually in $V$, $f \circ S$ is eventually in $U$.

**(f) $\rightarrow$ (g):** Assuming (f), let $A$ be a subset of $X$ and $s$ a point of $A^{-}$. Then there is a net $S$ in $A$ which converges to $s$, and $f \circ S$ converges to $f(s)$, which is therefore a member of $f[A]^{-}$. Hence $f[A^{-}] \subset f[A]^{-}$.

**(g) $\rightarrow$ (h):** Assuming (g), take $A = f^{-1}[B]$. Then $f[A^{-}] \subset f[A]^{-} \subset B^{-}$ and hence $A^{-} \subset f^{-1}[B^{-}]$. That is, $f^{-1}[B]^{-} \subset f^{-1}[B^{-}]$.

**(h) $\rightarrow$ (b):** Assuming (h), if $B$ is a closed subset of $Y$, then $f^{-1}[B]^{-} \subset f^{-1}[B^{-}] = f^{-1}[B]$ and $f^{-1}[B]$ is therefore closed. $\square$
