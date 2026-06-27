---
role: proof
locale: en
of_concept: theorem-dimension-prime-ideal-associated-prime-primary-ideal-transcendence-degree
source_book: gtm029
source_chapter: "VII"
source_section: "11"
---

Let $P$ be a prime ideal of $q^e$. We have $P^c \supset q$, whence $P^c \supset p$ since $P^c$ is prime. We also have $q^e : P > q^e$, and hence a fortiori $q^e : P^{ce} > q^e$, since $P^{ce} \subset P$. By (3) we can write $q^e : P^{ce} = (q : P^c)^e$. Hence we have $(q : P^c)^e > q^e$, and therefore taking contractions in $R$ and using (1) we find $q : P^c > q$. Therefore $P^c \subset P$, showing that $P^c = p$.

Let $K'$ be an intermediate field between $k$ and $K$ such that $K'$ is a pure transcendental extension of $k$ and $K$ is an algebraic extension of $K'$. We denote by $R'$ the polynomial ring $K'[X_1, X_2, \cdots, X_n]$ and by $p', q'$ the extended ideals $R'p$ and $R'q$. The ideal $q^e$ is also the extension of $q'$ to $S$. Since, by the preceding theorem, $q^e$ is primary and $p' = \sqrt{q'}$, it follows, by the preceding part of proof, that $P \cap R' = p'$. Since $K$ is algebraic over $K'$, $S$ is integral over $R'$. Hence $dim P = dim p'$ (Vol. I, Ch. V, § 2, Lemma 1). Since, by the preceding theorem, we have $dim p' = dim p$, we conclude that $dim P = dim p$.

Conversely, assume that $P$ is a prime ideal in $S$ such that $P^c = p$ and $dim P = dim p$. Since $P \sups

We shall now study in more detail the behavior of a prime ideal $p$ in $R$ under extension to $S$. We give the following definitions:

(1) $p$ splits in $S$ if $p^e$ is not a primary ideal.

(2) $p$ is unramified in $S$ if $p^e$ is an intersection of prime ideals (or, equivalently, if $p^e = \sqrt{p^e}$). In the contrary case $p$ is said to be ramified in $S$.

(3) $p$ is absolutely prime if for every extension $K$ of $k$ the ideal $p^e$ is prime. In other words: $p$ is absolutely prime if it is unramified and does not split, for any extension $K$ of $k$.

(4) $p$ is quasi-absolutely prime if $p^e$ is a primary ideal for any extension $K$ of $k$.

(5) $p$ is absolutely unramified if $p$ is unramified for any extension $K$ of $k$.

Since the ring $S/p^e$ is the tensor product $K \otimes R/p$ over $k$, we can state the following lemma:

Lemma. If $p$ is a prime ideal in $R$ then

(1) $p$ does not split in $S$ if and only if every zero divisor in $K \otimes R/p$ is nilpotent (or—equivalently—if and only if the zero ideal in the tensor product $K \otimes R/p$ is primary);

(2) $p$ is unramified in $S$ if and only if zero is the only nilpotent element in $K \otimes R/p$;

(3) $p^e$ is a prime ideal if and only if $K \otimes R/p$ is an integral domain.

In Vol. I, Ch. III, § 15 (Theorem 39) we have proved that if $K$ and $K'$ are two integral domains containing a field $k$ and if the quotient field of one of these domains is separable over $k$, then $K \otimes K'$ has no proper nilpotent elements. This yields at once the following consequence

$X_1 X_2, \cdots, X_n$ respectively. We have $R/\mathfrak{p} = k[x_1, x_2, \cdots, x_n]$ and $S/\mathfrak{p}^e = K[x_1, x_2, \cdots, x_n] = K \otimes k[x_1, x_2, \cdots, x_n]$.

By assumption, $\mathfrak{p}^e$ is an intersection of prime ideals. By Corollary 2 to Theorem 36, $\mathfrak{p}^e$ is a primary ideal. Hence $\mathfrak{p}^e$ is a prime ideal, and $K[x_1, x_2, \cdots, x_n]$ is an integral domain. By the definition of tensor products, $R/\mathfrak{p}$ and $K$ are linearly disjoint in $K \otimes R/\mathfrak{p}$. We have therefore that the quotient field of $R/\mathfrak{p}$ and the field $k^{p-1}$ are linearly disjoint, over $k$, in their common overfield $k^{p-1}(x_1, x_2, \cdots, x_n)$, and the theorem now follows from the definition of separability (Vol. I, Ch. II, § 15, p. 113). Q.E.D
