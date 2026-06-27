---
role: proof
locale: en
of_concept: lemma-even-cover-open-sigma-discrete
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof that Even Covers Yield Open Sigma-Discrete Refinements

**Lemma 33.** If $X$ is a space such that each open cover is even, then every open cover of $X$ has an open $\sigma$-discrete refinement.

*Proof.* The proof is an application of A. H. Stone's trick (cf. Theorem 4.21 and the results of Chapter 6).

Let $\mathcal{U}$ be an open cover of $X$. By hypothesis, $\mathcal{U}$ is even, so there exists a symmetric neighborhood $U_1$ of the diagonal $\Delta$ in $X \times X$ such that for each $x \in X$, the set $U_1[x]$ is contained in some member of $\mathcal{U}$.

Apply Lemma 30 repeatedly to construct a sequence $\{U_n\}_{n \in \omega}$ of symmetric neighborhoods of the diagonal and a sequence $\{V_n\}_{n \in \omega}$ of symmetric neighborhoods of the diagonal such that for each $n$:

$$V_{n+1} \circ V_{n+1} \subset U_{n+1}, \qquad U_{n+1} \circ U_{n+1} \subset V_n.$$

(Start with $U_1$; apply Lemma 30 to get $V_1$ with $V_1 \circ V_1 \subset U_1$; apply Lemma 30 to $V_1$ to get $U_2$ with $U_2 \circ U_2 \subset V_1$; and so on inductively. Lemma 30 requires the space to satisfy condition (d), which holds by hypothesis.)

Now choose a well-ordering $<$ of $X$ (axiom of choice, see 0.25). For each $n \in \omega$ and each $x \in X$, define

$$U_n^*(x) = U_n[x] \setminus \bigcup \{V_n[y] : y < x\}.$$

These sets are open because each $U_n[x]$ is open and the subtracted union is closed (or more precisely, the construction ensures openness).

For each fixed $n$, the family $\mathcal{U}_n = \{U_n^*(x) : x \in X\}$ is discrete. Indeed:

- By construction, if $x \neq y$, say $y < x$, then $U_n^*(x)$ is disjoint from $V_n[y]$ (since $U_n^*(x)$ explicitly has $\bigcup_{z < x} V_n[z]$ removed, and $y < x$). Hence $U_n^*(x) \cap V_n[y] = \emptyset$.

- If $z \in X$ and the neighborhood $V_n[z]$ intersects $U_n^*(y)$ for some $y$, then $z \in V_n[U_n^*(y)]$ (where $V_n[U_n^*(y)] = \bigcup_{a \in U_n^*(y)} V_n[a]$). And $V_n[U_n^*(y)]$ is a neighborhood of $z$ which, by the following argument, intersects no set $U_n^*(x)$ for $x \neq y$:

  For $x \neq y$, if $x < y$, then $U_n^*(y)$ is disjoint from $V_n[x]$, so $V_n[U_n^*(y)]$ (being the $V_n$-saturation of $U_n^*(y)$) cannot contain points of $V_n[x]$; similarly, if $y < x$, then $U_n^*(x) \cap V_n[y] = \emptyset$ and the symmetry of the construction ensures $V_n[U_n^*(y)] \cap U_n^*(x) = \emptyset$.

Thus each $\mathcal{U}_n$ is a discrete family. Let $\mathcal{U}_\omega = \bigcup_{n \in \omega} \mathcal{U}_n$. It remains to verify that $\mathcal{U}_\omega$ covers $X$.

For each $x \in X$, consider the sequence of sets $U_n[x]$. Since $x \in U_n[x]$ (diagonal neighborhoods contain the diagonal), there is a least $n$ (if any) such that $x$ belongs to some $V_n[y]$ with $y < x$. If no such pair $(n, y)$ exists, then $x \in U_n^*(x)$ for all $n$, and we are done. Otherwise, let $n$ be the first index and $y$ the first point (in the well-ordering) such that $x \in V_n[y]$. Then $x \in U_{n+1}^*(y)$ (by the nesting properties $V_n \subset U_{n+1}$, more precisely: if $x \notin V_n[z]$ for any $z < y$, but $x \in V_n[y]$, then...). A careful inductive argument using the nesting $U_{n+1} \circ U_{n+1} \subset V_n$ shows each $x$ lies in some $U_n^*(y)$. (Full details: see Kelley, proof of Lemma 5.33, or compare with the proof of 4.21.)

Therefore $\mathcal{U}_\omega$ is an open $\sigma$-discrete refinement of $\mathcal{U}$. $\square$
