---
role: proof
locale: en
of_concept: transitive-automorphisms-of-euclidean-regions
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

The proof that transitive automorphisms exist for any region $\Omega \subseteq \mathbb{R}^r$ ($r \geq 2$) follows by adapting the construction given for the closed unit square $[0,1]^2$.

Let $\Omega$ be an open connected region in $\mathbb{R}^r$ with $r \geq 2$. Since $\Omega$ is homeomorphic to a region containing a closed $r$-dimensional cube, one can embed the unit square construction into $\Omega$: choose a topological closed disk (a homeomorphic image of $[0,1]^2$) contained in $\Omega$. Let $H_{\Omega}$ be the space of all automorphisms of $\Omega$ that restrict to the identity outside this disk, equipped with the uniform metric. This space is topologically complete.

For a countable base $\{U_i\}$ of $\Omega$, define

$$E_{ij} = \left\{ T \in H_{\Omega} : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

The same perturbation argument as for the square shows each $E_{ij}$ is dense and open in $H_{\Omega}$. The proof relies only on the availability of line segments joining points (which exist in any region of $\mathbb{R}^r$, $r \geq 2$) and the fact that recurrent and nonperiodic points form residual sets (Theorem 17.3 generalizes to any measure-preserving automorphism of a separable metric space).

By the Baire category theorem, $\bigcap_{i,j} E_{ij} \neq \emptyset$, and any $T$ in this intersection is a transitive automorphism of $\Omega$. Moreover, the set of all such transitive automorphisms is residual in $H_{\Omega}$. The method extends similarly to arbitrary regions of $\mathbb{R}^r$ for any $r \geq 2$, using the fact that $\Omega$ can be exhausted by a countable family of closed disks, each admitting the square-like construction.
