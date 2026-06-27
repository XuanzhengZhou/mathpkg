---
role: exercise
locale: en
chapter: "1"
section: "010"
exercise_number: 20
---

In this exercise we indicate how compact abelian groups arise as the algebras over a theory in Set. We begin by reviewing some of the theory of character groups (see e.g. [Hewitt and Ross '63], [Pontrjagin '46]). Let $S$ denote the circle group, that is, the compact metric abelian group of complex numbers of modulus 1 with complex multiplication as group operation. For each locally compact abelian group $C$, the character group $C^\wedge$ of $C$ is the locally compact abelian group of all continuous homomorphisms from $C$ to $S$ with neighborhood basis at the origin $\{U(F, n): F$ is a compact subset of $C$ and $n = 1, 2, 3 \ldots\}$ where $U(F, n)$ is the set of all characters $\chi$ in $C^\wedge$ such that $|x\chi - 1| < 1/n$ for all $x$ in $F$. If $C, D$ are locally compact abelian groups then the passage from $f: C \longrightarrow D$ to $f^\wedge: D^\wedge \longrightarrow C^\wedge$, where $\chi f^\wedge = f.\chi$, establishes a bijection between the two sets of continuous homomorphisms. The map $C \longrightarrow (C^\wedge)^\wedge$ which sends $c$ to “evaluate at $c$” is a topological isomorphism, so “$(C^\wedge)^\wedge = C$.” $C$ is compact if and only if $C^\wedge$ is discrete.

(a) For each set $A$, consider the discrete group (ignore the natural product topology!) $S^A$ of functions from $A$ to $S$ and let $AT$ denote the underlying set of the compact abelian group $(S^A)^\wedge$. Let $A\eta: A \longrightarrow AT$ send

$$aaxyC = x \quad abxxC = x$$
$$abxyC = baxyC \quad ababC = b$$
$$abtuvwC \hat{t} \hat{u} \hat{v} \hat{w} CC = abt \hat{t} Cabu \hat{u} Cabv \hat{u} Cabw \hat{w} CC$$

(see exercise 3.3.8). Show that the corresponding algebraic theory has generating rank 3. [Hint: show $abxyC = yabyWabxWW$ if $tuvW = tuvtC$.]

(c) Prove that "generating rank $\leq$ rank."

(d) Let $n$ be a generating cardinal for $T$ and let $\xi:XT \longrightarrow X$ satisfy "$X\eta.\xi = \text{id}_X$" and "for all $\alpha, \beta:A \longrightarrow XT$ with $\text{card}(A) < n^\bullet$, if $\alpha.\xi = \beta.\xi$ then $\alpha^\#.\xi = \beta^\#.\xi$". Prove that $(X, \xi)$ is a $T$-algebra. [Hint: use exercise 4.11; let $AT_k$ be the subset of those elements of $AT$ which, in the definition of "generating cardinal" above, admit a factorization of size $k$; prove "for arbitrary $A$ and $\alpha, \beta:A \longrightarrow XT$, if $\alpha.\xi = \beta.\xi$ then $\langle p, \alpha^\#.\xi \rangle = \langle p, \beta^\#.\xi \rangle$ for all $p \in AT_k$" by induction on $k$; the assumptions on $\xi$ provide the basis; if $p \in AT_{k+1}$, the basis argument also proves $(\alpha_{k+1} \circ \alpha).\xi = (\alpha_{k+1} \circ \beta).\xi$; now use the induction hypothesis.]
