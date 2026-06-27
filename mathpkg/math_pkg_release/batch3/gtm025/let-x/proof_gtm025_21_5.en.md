---
role: proof
locale: en
of_concept: "let-x"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.5"
---

Note first that the family $F$ exists, for $P(T)$ is a monotone family and the intersection of all monotone families containing $A$ is again a monotone family containing $A$; this intersection is $F$.

Since any $\sigma$-algebra is a monotone family and $S(A) \supset F \supset A$, it follows that $S(A) \supset F \supset A$. To finish the proof it therefore suffices to prove that $F$ is a $\sigma$-algebra. For a monotone sequence $(H_n)_{n=1}^{\infty}$, we write $\lim H_n$ for the set $\bigcup_{n=1}^{\infty} H_n$ or $\bigcap_{n=1}^{\infty} H_n$ according as $(H_n)$ is an increasing or a decreasing sequence. If $E \in F$, write

$$F_E = \{F \in F : F \cap E' \in F, E \cap F' \in F, E \cup F \in F\}.$$

Note that $F \in F_E$ if and only if $E \in F_E$. It is also clear that if $(F_n)_{n=1}^{\infty}$ is a monotone sequence in $F_E$, then

$$(\lim F_n) \cap E' = \lim (F_n \cap E') \in F,$$

$$E \cap (\lim F_n)' = E \cap (\lim F_n') = \lim (E \cap F_n') \in F,$$

and

$$E \cup (\lim F_n) = \lim (E \cup F_n) \in F,$$

since $F$ is a monotone family. Thus $F_E$ is a monotone family for every $E \in F$.

If $E, F \in A$, then, since $A$ is an algebra, $E$ belongs to $F_E$ and $F$ belongs to $F_E$. It follows that $A \subset F_E$ for all $E \in A$. Since $F$ is the smallest monotone family containing $A$, we therefore have $F \subset F_E$ for all $E \in A$. Thus for any $F \in F$

Proof. Let $\mathcal{F}$ be the family of all sets $E \in \mathcal{M} \times \mathcal{N}$ such that (i), (ii), and (iii) hold for $E$. We will show that $\mathcal{F}$ is a monotone family that contains all finite disjoint unions of measurable rectangles. Then (21.7) will show that $\mathcal{F} = \mathcal{M} \times \mathcal{N}$.

Suppose that $E = A \times B$ is a measurable rectangle. Since $E_x = B$ or $\varnothing$ according as $x \in A$ or $x \in A'$, and $E^y = A$ or $\varnothing$ according as $y \in B$ or $y \in B'$, we have $\nu(E_x) = \nu(B) \xi_A(x)$ and $\mu(E^y) = \mu(A) \xi_B(y)$; hence (i) and (ii) hold for this $E$. We may also write

$$\int_X \nu(E_x) \, d\mu(x) = \int_X \nu(B) \xi_A \, d\mu = \nu(B) \cdot \mu(A)$$

$$= \int_Y \mu(A) \xi_B \, d\nu = \int_Y \mu(E^y) \, d\nu(y).$$

Thus (iii) holds for this $E$, and so $E \in \mathcal{F}$. Thus $\mathcal{F}$ contains all measurable rectangles.

Let $\{E_1, \ldots, E_p\}$ be a finite, pairwise disjoint subfamily of $\mathcal{F}$. Since $\left( \bigcup_{n=1}^p E_n \right)_x = \bigcup_{n=1}^p (E_n)_x$ and $\left( \bigcup_{n=1}^p E_n \right)_y = \bigcup_{n=1}^p (E_n)_y$ for all $x \in X$ and $y \in Y$, it is clear that $\left( \bigcup_{n=1}^p E_n \right)_\in \mathcal{F}$. Thus, $\mathcal{F}$ contains all finite disjoint unions of

that

$$v(F_x) = \lim_{n \to \infty} v((F_n)_x)$$

for every $x \in X$. Thus the function $x \rightarrow v(F_x)$ is the pointwise limit of a sequence of $\mathcal{M}$-measurable functions, and so it is $\mathcal{M}$-measurable (11.14); hence (i) holds for $F$. Likewise (ii) holds for $F$. Since

$$\int_X v((F_1)_x) d\mu(x) \leq \int_X v(B) \xi_A d\mu < \infty$$

and

$$\int_Y \mu((F_1)^y) d\nu(y) \leq \int_Y \mu(A) \xi_B d\nu < \infty,$$

Lebesgue's dominated convergence theorem (12.24) implies that

$$\int_X v(F_x) d\mu(x) = \lim_{n \to \infty} \int_X v((F_n)_x) d\mu(x)$$

$$= \lim_{n \to \infty} \int_Y \mu((F_n)^y) d\nu(y)$$

$$= \int_Y \mu(F^y) d\nu(y),$$

and therefore (iii) holds for $F$.

Use the $\sigma$-finiteness hypothesis to choose increasing sequences $(A_k)_{k=1}^{\infty} \subset \mathcal{M}$ and $(B_k)_{k=1}^{\infty} \subset \mathcal{N}$ such that $\mu(A_k) < \infty$ and $\nu(B_k) < \infty$ for all $k$, and such that $X = \bigcup_{k=1}^{\infty} A_k$ and $Y = \bigcup_{k=1}^{\infty} B_k$. Let $\mathcal{E} = \{E \in \mathcal{M} \times \mathcal{N} : E \cap (A_k \times B_k) \in \mathcal{F}$ for all $k \in N\}$. Since the family $\mathcal{A}$ of all finite disjoint unions of measurable rectangles is an algebra (21.3) and $\mathcal{A} \subset \mathcal{F}$, we have

We now define a set function on $M \times N$ that turns out to be the desired product measure.
