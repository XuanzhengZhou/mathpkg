---
role: proof
locale: en
of_concept: lyndon-hochschild-serre-spectral-sequence
source_book: gtm004
source_chapter: "VIII"
source_section: "9"
---

# Proof of Lyndon–Hochschild–Serre Spectral Sequence

We are given a short exact sequence of groups

$$N \stackrel{1}{\hookrightarrow} K \stackrel{p}{\twoheadrightarrow} Q \tag{9.23}$$

and a $K$-module $A$. Let $\mathfrak{A}$ be the category of (left) $K$-modules, let $\mathfrak{B}$ be the category of (left) $Q$-modules, and let $\mathfrak{C}$ be the category of abelian groups. Define the functors

$$F : \mathfrak{A} \rightarrow \mathfrak{B}, \quad F(A) = A^N = \operatorname{Hom}_N(\mathbb{Z}, A),$$
$$G : \mathfrak{B} \rightarrow \mathfrak{C}, \quad G(B) = B^Q = \operatorname{Hom}_Q(\mathbb{Z}, B). \tag{9.24}$$

Then $GF(A) = (A^N)^Q \cong A^K$, and consequently

$$R^q F(A) = H^q(N, A), \quad R^p G(B) = H^p(Q, B), \quad R^q(GF)(A) = H^q(K, A).$$

**Verification of the $G$-acyclicity hypothesis.** We must verify the hypotheses of Theorem 9.3. The functors $F$ and $G$ are additive, being Hom-functors. It remains to show that if $I$ is an injective $K$-module, then $F(I) = I^N$ is $G$-acyclic; in fact, we prove the stronger statement that $I^N$ is an injective $Q$-module.

Observe that $F$ is right adjoint to the functor $\bar{F} : \mathfrak{B} \rightarrow \mathfrak{A}$ defined as follows: given a $Q$-module $B$, $\bar{F}(B)$ is the abelian group $B$ endowed with the $K$-module structure

$$x \cdot b = (px) \circ b, \quad x \in K, \; b \in B.$$

That is, $\bar{F}$ is restriction of scalars along the epimorphism $p : K \twoheadrightarrow Q$. Since $p$ is surjective, $\bar{F}$ plainly preserves monomorphisms. By Theorem IV.12.1, a functor that is right adjoint to a monomorphism-preserving functor preserves injectives. Hence $F(I) = I^N$ is an injective $Q$-module, and in particular $G$-acyclic (injective objects are acyclic for any right derived functor).

**Identification of the derived functors.** We may now apply Theorem 9.3, yielding a spectral sequence

$$E_1^{p,q} = (R^p G)(R^{q-p} F)(A) \Rightarrow R^q(GF)(A).$$

To identify $R^{q-p}F(A)$, we note that since $\mathbb{Z}K$ is a free $\mathbb{Z}N$-module (it is free on any set of coset representatives of $N$ in $K$), any $K$-injective resolution of $A$,

$$I_0 \rightarrow I_1 \rightarrow I_2 \rightarrow \cdots,$$

is also an $N$-injective resolution of $A$. Applying $\operatorname{Hom}_N(\mathbb{Z}, -)$ to this resolution yields the complex

$$\operatorname{Hom}_N(\mathbb{Z}, I_0) \rightarrow \operatorname{Hom}_N(\mathbb{Z}, I_1) \rightarrow \operatorname{Hom}_N(\mathbb{Z}, I_2) \rightarrow \cdots,$$

whose cohomology computes $H^*(N, A)$. Thus $R^{q-p}F(A) = H^{q-p}(N, A)$.

Similarly, the $Q$-module structure on $H^{q-p}(N, A)$ arises functorially from the $K$-module structure on the resolution, and applying $G = (-)^Q$ computes $H^p(Q, H^{q-p}(N, A))$. Finally $R^q(GF)(A) = H^q(K, A)$.

Therefore the Grothendieck spectral sequence specializes to

$$E_1^{p,q} = H^p(Q, H^{q-p}(N, A)) \Rightarrow H^q(K, A),$$

which converges finitely to the graded object associated with $\{H^q(K, A)\}$, suitably filtered. This establishes the Lyndon–Hochschild–Serre spectral sequence. $\square$

**Remark.** The proof also shows that the action of $Q$ on $H^m(N, A)$ is the natural one: for $x \in Q$ represented by $\tilde{x} \in K$, and a cocycle $f : N^{\otimes m} \rightarrow A$, the action is $(\tilde{x} \cdot f)(n_1, \ldots, n_m) = \tilde{x} f(\tilde{x}^{-1} n_1 \tilde{x}, \ldots, \tilde{x}^{-1} n_m \tilde{x})$, which descends to cohomology because $N$ is normal.
