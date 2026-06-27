---
role: proof
locale: en
of_concept: affine-projective-isomorphism-restriction
source_book: gtm049
source_chapter: "3"
source_section: "3.4"
---

Let $\alpha: A \to A'$ be an affine isomorphism. The elements $P\alpha$ of $A'$ are again all parallel and have the same dimension; as such they all have the same hyperplane at infinity $M'$. We are thus forced to define $M\pi = M'$ for each subspace $M$ of $H$. It only remains to show that the one--one mapping $\pi$ so defined, and its inverse $\pi^{-1}$, preserve inclusion.

Since $\pi$ extends $\alpha$ it is clear that $\pi$ preserves inclusions among the elements of $A$. Suppose that $M, N$ are subspaces of $H$ and that $P, Q$ respectively have $M, N$ as hyperplanes at infinity. Then $M \subset N$ if, and only if, $P$ and $Q$ are parallel and $P \leq \dim Q$. By our definition, $M\pi \subset N\pi$ if, and only if, $P\alpha$ and $Q\alpha$ are parallel and $P\alpha \leq \dim Q\alpha$. Since $\alpha$ is an isomorphism it follows that $M \subset N$ if, and only if, $M\pi \subset N\pi$.

If $M$ is a subspace of $H$ and $Q$ is an element of $A$ with hyperplane at infinity $N = Q \cap H$, then $M \subset Q$ if, and only if, $M \subset N$. From this it now follows that $M \subset Q$ if, and only if, $M\pi \subset Q\pi$.

Now suppose $\mathcal{P}(V), \mathcal{P}(V')$ are defined over the same field $F$ and $\pi$ is a projectivity. Then $\pi = \mathcal{P}(f)$ where $f$ is an isomorphism of $V$ onto $V'$ taking $H$ onto $H'$. The geometries $(A, \varphi), (A', \varphi')$ are linked to geometries $\mathcal{A}(c + H), \mathcal{A}(c' + H')$ where $c, c'$ are arbitrary elements of $V, V'$ not in $H, H'$, respectively. By multiplying $f$ by a suitable non-zero scalar, if necessary, we may ensure $cf = c'$. Then the restriction of $\mathcal{A}(f)$ to $\mathcal{A}(c + H)$ gives an affinity onto $\mathcal{A}(c' + H')$.

Conversely, if $\alpha$ is an affinity, then by Theorem 5 (or the earlier result for affinities, p. 43) it is induced by a linear isomorphism $f$ of the direction spaces, which extends uniquely to a projectivity $\pi = \mathcal{P}(f)$ with $H\pi = H'$ and $\pi|_A = \alpha$. The uniqueness of $\pi$ follows from the fact that any two projectivities agreeing on $A$ must agree everywhere, since $A$ together with $H$ generates $\mathcal{P}(V)$.
