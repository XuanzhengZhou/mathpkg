---
role: proof
locale: en
of_concept: theorem-3
source_book: gtm026
source_chapter: "1"
source_section: "4.25"
---

Define $\Omega_n = \{n\} \times V_n T$ where $V_n$ is as defined in 4

The proof of 4.26 is an immediate consequence of the fact that $(r.f)T = rT.fT$. As might have been expected, we assign an $\Omega$-algebra structure $\delta$ to the $\mathbf{T}$-algebra $(X, \xi)$ by setting $\delta_\omega = X\hat{\omega}.\xi$. It is immediately clear from 4.26 and a glance at the diagram

$$
\begin{array}{c c c c c}
X^n & XT & \xi & X \\
f^n & fT & f & Y^n \\
Y^n & YT & \theta & Y
\end{array}
$$

that a $\mathbf{T}$-homomorphism is an $\Omega$-homomorphism. To prove, conversely, that an $\Omega$-homomorphism is a $\mathbf{T}$-homomorphism it is sufficient to prove that every element $\bar{x} \in XT$ is in the image of $X\hat{\omega}$ for some $\omega$, that is, there must exist some integer $n$, some element $\omega \in V_nT$, and some function $r: V_n \longrightarrow X$ such that $\langle \omega, rT \rangle = \bar{x}$; but this is precisely the definition “$\mathbf{T}$ is finitary.” In particular, consideration of $f = \mathrm{id}_X$ and the fact that $T$ is a functor allows us to see that if $\xi \neq \xi'$ then $\delta \neq \delta'$. Let $\mathcal{A}$ be the class of all $\Omega$-algebras which arise from $\mathbf{T}$-algebras as above. It is clear that, to finish the proof, it is sufficient to find a set $E$ of equations such that $\mathcal{A} = \text{all } (\Omega, E)$-algebras. By 4.22 we need only show that $\mathcal{A}$ is closed under products, subalgebras, and quotients. We will give particular attention to the verification since it gives us our first encounter with “universal algebra in the language of $\mathbf{T}$-algebras.”

(4.27) Let $(X_i

$(X, \xi)$ is a $\mathbf{T}$-algebra. Consider

Everything commutes except perhaps (?). But now apply the principle that to prove that two functions into $X$ are equal it is necessary and sufficient to prove that they are equal followed by each projection; which is exactly what we know. The other algebra law is proved by the same reasoning:

This finishes 4.27 and also establishes that $\mathcal{A}$ is closed under products, since both products are the unique structure making projections homomorphisms.

(4.28) Let $(X, \xi)$ be a $\mathbf{T}$-algebra and let $A$ be a subset of $X$ with inclusion map $i: A \hookrightarrow X$. Say that $A$ is a $\mathbf{T}$-subalgebra of $(X, \xi)$ if there exists a factorization:

In common with the family $(pr_i)$ of 4.27, $i: A \hookrightarrow X$ has the virtue that to prove two elements of $A$ are the same it is necessary and sufficient to prove this followed by $i$. The same reasoning as in 4.27 guarantees, then, that $(A, \xi_0)$ is a $\mathbf{T}$-algebra, so that $A$ is a $\mathbf{T}$-subalgebra of $(X, \xi)$ if and only if there exists a $\mathbf{T}$-algebra structure on $A$ making $i$ a $\mathbf{T}$-homomorphism. To prove that $\mathcal{A}$ is closed under subalgebras it is still necessary to show that an $\Omega$-subalgebra of $(X, \xi)$ is a $\mathbf{T}$-subalgebra. Let $A$ be an $\Omega$-subalgebra. For $\bar{a} \in AT$ there exists $r: V_n \longrightarrow A$ and $\omega \in V_n T$ with $\langle \omega, rT \rangle = \bar{a}$. For $1 \leqslant j \leqslant n$ set $a_j = v_j r$. By hypothesis, $\delta_\omega: X^n \longrightarrow X$ maps $A^n$ into $A$. Therefore, $\langle \bar{a}, iT.\xi \rangle = \langle \omega, rT.iT.\xi \rangle = \langle \omega, (r.i)T.\xi \rangle = (a_1, \ldots, a_n) \delta_\omega \in A$. As $\bar{a} \in AT$ is arbitrary, the proof that $\mathcal{A}$ is closed under subalgebras is complete.

(4.29) If $H: \mathbf{Set} \longrightarrow \mathbf{Set}$ is any functor and if $f: X \longrightarrow Y$ is surjective than $fH: XH \longrightarrow YH$ is also surjective. This is a consequence of the axiom of choice. Let $d: Y \longrightarrow X$ be a choice function such that $d.f = \mathrm{id}_

to show that if $f$ is an $\Omega$-quotient algebra via the $\Omega$-structure $\gamma$, then $f$ is a T-quotient algebra. To this end we invoke the axiom of choice to get a choice function $d: Y \longrightarrow X$ with $d.f = \text{id}_Y$. Define $\theta: YT \longrightarrow Y = (dT: YT \longrightarrow XT). (\xi: XT \longrightarrow X). (f: X \longrightarrow Y)$. We will show $fT.\theta = \xi.f$. Let $x \in XT$. There exists $r: V_n \longrightarrow X$ and $\omega \in V_nT$ with $\langle \omega, rT \rangle = \bar{x}$. Then

$$\langle \bar{x}, \xi.f \rangle =$$
$$\langle \omega, rT.\xi.f \rangle =$$
$$(v_1r, \ldots, v_nr) \delta_\omega f =$$
$$(v_1rf, \ldots, v_nrf) \gamma_\omega =$$
$$(v_1rf.df, \ldots, v_nrf.df) \gamma_\omega =$$
$$(v_1rfd, \ldots, v_nrfd) \delta_\omega f =$$
$$\langle \omega, (rfd)T.\xi.f \rangle =$$
$$\langle \bar{x}, fT.dT.\xi.f \rangle$$

The proof of 4.25 is complete. $\square$

For use in the next section, we prove a further result about T-subalgebras. One expects that each subset $A$ of a T-algebra $(X, \xi)$ generates a T-subalgebra $\langle A \rangle$ of $(X, \xi)$ by “closing up $A$ under the T-operations.” For example, if $T$ is as in 4.17, $\langle A \rangle = \{a_1 \cdots a_n: a_1, \ldots, a_n \in A\}$. In general, one expects to consider those “terms” in $

4. The Algebras of a Theory

$IT \longrightarrow I$ by $\gamma = dT.\xi.p$. Then $pT.\gamma.i = pT.dT.\xi.p.i = pT.dT.pT.iT.\theta = pT.iT.\theta$. As $pT$ is surjective (by 4.29), $\gamma.i = iT.\theta$ as desired.

Now we return to the proof of 4.31 proper. The diagram

is commutative because $\eta$ is natural and $X\eta.\xi = \text{id}_X$. This proves that $A \subset \langle A \rangle$. It is obvious that $\langle A \rangle \subset \langle B \rangle$ whenever $A \subset B$. Since $iT.\xi: (AT, A\mu) \longrightarrow (X, \xi)$ is a T-homomorphism, $\langle A \rangle$ is a subalgebra of $(X, \xi)$ by 4.32. From the definition of “subalgebra” it is obvious that if $B$ is a subalgebra, $B = \langle B \rangle$. Therefore $\langle \langle A \rangle \rangle = \langle A \rangle$ and whenever $A$ is contained in the subalgebra $B$, $\langle A \rangle \subset \langle B \rangle = B$.

Notes for Section 4

Algebras of an algebraic theory in monoid form were defined by [Eilenberg and Moore ’65, (2.6)]. While they recognized that groups arise as $\text{Set}^T$, their main example is $AT = A \otimes \Lambda$ (where $\mathcal{K}$ is the category of modules over the commutative ring $R$ and $\Lambda$ is an $R$-algebra) whose algebras are the $\Lambda$-modules.

It was Jon Beck who first perceived that “triples” describe universal algebra in the category of sets. The atmosphere at that time is best conveyed by quoting two paragraphs from Beck’s thesis [Beck ’67, pages 72–73]. The quote is verbatim (except that our reference numbers

The Birkhoff variety theorem was proved in [Birkhoff'35, theorems 6, 9]. The ideas in 4.21–4.31 are interesting in their own right; for a different proof of 4.25 see 5.40 below. A much more general proof of 4.32 will be given in 3.4.17.

Exercises for Section 4

1. Starting from the point of view that the structure of an $(\Omega, E)$-algebra $(X, \delta)$ can be described by a function $\xi: XT \longrightarrow X$ (e.g. $x*y = (xy)\xi$ in 4.17), expand the heuristics of 4.11 into a motivation for the definition of "algebraic theory in monoid form."

2. In the proof of 4.15 we did not explicitly show that, for a fixed set $X$, the passage from $\delta$ to $\xi$ is injective. Show that this follows from 4.7.

3. A semilattice is a partially ordered set in which every pair of elements has a supremum. Let $T$ be the algebraic theory of nonempty finite subsets (cf. exercises 7, 10 of section 3). Show that $\text{Set}^T$ may be identified with the category of semilattices and functions which preserve binary suprema. [Hint: the structure map is "supremum."]

4. Prove that the double power-set theory of 3.19 is not finitary.

5. Why is "groups" not a variety in "monoids"?

6. Show that a subsemigroup of a group need not be a subgroup even if it is a group. (Hint: the units are different!)

For the following three exercises (implicit in [Birkhoff'35, page 141]) fix an algebraic theory $T$ in $\text{Set}$. A variety in $\text{Set}^T$ is a collection of $T$-algebras closed under the formation of products, subalgebras, and quotients.

7. For any collection $\mathcal{X}$ of $T$-algebras, show that the class $\text{Var}(\

then, if $A$ is finite then $AT'$ is finite. (Hint: show that $AT'$ has a universal property in $\text{Var}(\mathcal{X})$ and proceed as in 2.7.) This generalizes [Birkhoff ’35, Theorem 11]. $\mathcal{X}$ must be a “small set” in order that $P$ be definable; see the “primer on set theory” at the end of this chapter.

10. This exercise should help the reader to appreciate why isomorphic algebras are “abstractly the same.”

(a) There are four monoid structures on the two-element set $\{x, y\}$ whose multiplication tables are shown below:

$$
\begin{array}{c c c c c}
xx & xy & yx & yy \\
1 & x & y & y \\
2 & x & y & y \\
3 & y & x & x \\
4 & x & x & x
\end{array}
$$

Show that 1 and 3 are isomorphic and that 2 and 4 are isomorphic, but that no other two are isomorphic.

(b) Prove that “isomorphism” is an equivalence relation.

(c) (Cf. 2.3.1 below.) If $(Y, \gamma)$ is an $(\Omega, E)$-algebra and if $f: X \longrightarrow Y$ is a bijection, prove that there exists unique $\delta$ such that $f:(X, \delta) \longrightarrow (Y, \gamma)$ is an $\Omega$-homomorphism and then that $(X, \delta)$ is an $(\Omega, E)$-algebra and that $f$ is an isomorphism.

(d) Isomorphic structures “enjoy the same properties.” Verify this for groups with respect to the following properties: “possesses three normal subgroups”; “has no elements of finite order”; “admits a surjective homomorphism from the group of integers.”

11. Let $\mathbf{T}$ be an algebraic theory in $\mathcal{K}$. Show that the following axioms on $\xi: XT \longrightarrow X$ (suitable for theories presented in extension form as in exercise 3.12) are

as a hint, define the product of two algebraic theories in Set and prove that it is again a theory. If $T = \text{id} \times \text{id}$ (see exercise 12) show that $Set^T$ is the equationally-definable class corresponding to one binary operation and the equations $aa = a, (ab)(cd) = ad$.

14. [Jónsson and Tarski ’61]. Let $T$ be a theory in Set admitting a finite algebra with at least two elements. Let $A$ be a finite set.

(a) If $T$ corresponds to “groups,” show that there exists finite $B \subset AT$ such that $\langle B \rangle = AT$ and $A \cap B = \emptyset$.

(b) If $B \subset AT$ and $\langle B \rangle = AT$, prove that $\text{card}(A) \leqslant \text{card}(B)$. [Hint: let $(X, \xi)$ be a finite algebra with at least two elements; the map $X^A \rightarrow X^B$ sending $f$ to the restriction of $f^\#$ is injective.]

5. Infinitary Theories

In this section we restrict our attention, once again, to algebraic theories in the base category Set of sets and functions. We define the syntactic rank (the number of variables needed to write formulas) and the semantic rank (the number of variables needed by the operations on actual algebras) for an algebraic theory, and prove they are equal. Examples such as complete semilattices, complete atomic Boolean algebras, and compact Hausdorff spaces demonstrate that interesting mathematical structures arise as the algebras of infinitary theories. Bounded theories are coextensive with equationally definable classes of algebras (with perhaps infinitary operations). In general, theories are coextensive with “tractable large” equational presentations. We prove the theorem of [Gaifmann ’64] and [Hales ’64] that complete Boolean algebras do not constitute a tractable equational class.

Some useful facts about set theory which relate to this section are presented in a “primer” at the end.

Let us fix an algebraic theory $T = (T,
