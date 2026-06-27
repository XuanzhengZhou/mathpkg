---
role: proof
locale: en
of_concept: adams-conjecture
source_book: gtm020
source_chapter: "14"
source_section: "14"
---

**Proof Sketch (Four Approaches).** To prove the Adams conjecture, it suffices to prove it for the universal bundle over $BO(n)$ and for $\psi^{p}$ where $p$ is a prime.

**Proof 1 (Quillen, Friedlander).** Quillen observed that for algebraic vector bundles $E$ with class $[E]$ in $K(X)$, the formula
$$
\psi^{p}[E] = [\mathrm{Frob}^{*} E]
$$
holds, where $\mathrm{Frob}: X \to X$ is the Frobenius endomorphism. Using the \'{e}tale homotopy theory of Artin and Mazur, the Adams conjecture for complex vector bundles reduces to a conjecture on the \'{e}tale properties of sphere bundles, which Friedlander subsequently proved. This proof covered only complex $K$-theory and did not resolve the question of $m_{2k}$ or $2m_{2k}$.

**Proof 2 (Sullivan).** Sullivan employed \'{e}tale homotopy type considerations for $BO$ as a limit of Grassmannians, which are algebraic varieties defined over any field.

**Proof 3 (Quillen).** Quillen gave a second proof by first establishing the conjecture for vector bundles with finite structure group. Using modular character theory for finite groups, one produces enough examples of virtual representations of finite groups to define maps
$$
BGL(k) \to BU \quad \text{and} \quad BO(k) \to BO
$$
where $k$ is an algebraic closure of the field of $p$ elements. These maps are homology isomorphisms over $\mathbb{Z}/d$ where $d$ is prime to $p$. The general Adams conjecture is then deduced from the finite structure group case using standard methods of algebraic topology.

**Proof 4 (Becker, Gottlieb).** Let $p: E \to B$ be a fibre bundle with fibre $F$ a compact smooth manifold, structure group $G$ a compact Lie group acting smoothly on $F$, and base $B$ a finite complex. Becker and Gottlieb construct an $S$-map $p^{\mathrm{tr}}: B \cup \{\infty\} \to E \cup \{\infty\} = E^{+}$ such that for any cohomology theory, $h^{*}(p^{\mathrm{tr}}) h^{*}(p)$ is multiplication by $e(F)$, the Euler number of $F$. For a real $2n$-dimensional vector bundle $\xi$ over $B$, there exists a map $f: X \to B$ such that $h^{*}(f)$ is a split monomorphism for any general cohomology theory, and $f^{*}(\xi) = \eta$ has structure group $N(T)$, the normalizer of the maximal torus $SO(2)^{n} \subset O(2n)$. The result follows by transfer arguments.

**Consequences.** A byproduct of the proof is a precise determination of $J(S^{m})$: the map $J: KO(S^{4m}) \to \sigma_{4m-1}$ has image a cyclic direct summand of order $m_{k}$.
