---
role: proof
locale: en
of_concept: real-maximal-ideal-characterization
source_book: gtm043
source_chapter: "5"
source_section: "5.14"
---

\textbf{(1) implies (2).} Suppose that $(Z(f_n))_{n \in \mathbb{N}}$ is a subfamily of $Z[M]$ whose intersection does not belong to $Z[M]$. Define

$$g(x) = \sum_{n \in \mathbb{N}} \left( |f_n(x)| \wedge 2^{-n} \right) \quad (x \in X).$$

The series converges uniformly (the $n$-th term is bounded by $2^{-n}$), so $g$ is continuous and nonnegative. Moreover, $Z(g) = \bigcap_n Z(f_n) \notin Z[M]$. Thus $g \notin M$, but since $g \geq 0$, we have $M(g) \geq 0$ in the ordered field $C(X)/M$. Because $M$ is real, $C(X)/M \cong \mathbb{R}$, and the only nonnegative element not in the kernel of a real homomorphism is a strictly positive real number; hence $M(g) > 0$.

On the other hand, for any $m \in \mathbb{N}$ and for every $x$ belonging to the member

$$Z(f_1) \cap \cdots \cap Z(f_m)$$

of $Z[M]$, we have

$$g(x) \leq \sum_{n=m+1}^{\infty} 2^{-n} = 2^{-m}.$$

Since each $Z(f_1) \cap \cdots \cap Z(f_m) \in Z[M]$, in the quotient field we obtain $M(g) \leq 2^{-m}$ for every $m$. Letting $m \to \infty$ yields $M(g) \leq 0$, contradicting $M(g) > 0$. Therefore the intersection $\bigcap_n Z(f_n)$ must belong to $Z[M]$, establishing closure under countable intersections.

\textbf{(2) implies (3).} If $Z[M]$ is closed under countable intersection and $\varnothing \in Z[M]$, then taking any countable family whose intersection is empty would force $\varnothing \in Z[M]$, which is impossible for a $z$-filter (or one directly notes that closure under countable intersection implies the countable intersection property).

\textbf{(3) implies (1).} Suppose $Z[M]$ has the countable intersection property but $M$ is not real. Then $C(X)/M$ is a hyper-real field, and there exists $f \in C(X)$ such that $M(f)$ is infinitely large or infinitely small. By adjusting $f$, one can construct a countable family of zero-sets in $Z[M]$ whose intersection is empty, contradicting the countable intersection property. The precise argument: if $M(f)$ is infinitely large, then the sets $Z((f - n) \wedge 0)$ for $n \in \mathbb{N}$ all belong to $Z[M]$, yet their intersection is empty. This contradicts (3). Hence $M$ must be real.
