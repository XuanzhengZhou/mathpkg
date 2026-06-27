---
role: proof
locale: en
of_concept: derivation-from-homomorphism-into-semi-direct-product
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of Homomorphisms into Semi-Direct Product Determine Derivations

**Corollary 5.4.** Every group homomorphism $h: X \to A \rtimes G$ determines a homomorphism $f = ph: X \to G$ and a derivation $d = qh: X \to A$, where $A$ is regarded as an $X$-module via $f$. In particular, if $h$ satisfies $ph = 1_X$ (so that $X$ is a subgroup of $G$ after identifying $X$ with its image under the splitting), then $d = qh: X \to A$ is a derivation with respect to the $X$-module structure induced by the inclusion $X \hookrightarrow G$.

*Proof.* This is precisely the converse direction of Proposition 5.3. Given $h: X \to A \rtimes G$, set $f = ph: X \to G$ and $d = qh: X \to A$. Then $f$ is a group homomorphism as the composition of homomorphisms. By equation (5.7), the map $q: A \rtimes G \to A$ satisfies the derivation-like property

$$q((a, x) \cdot (a', x')) = q(a, x) + (a, x) \circ q(a', x').$$

It follows exactly as in the converse part of Proposition 5.3 that for all $x, y \in X$,

$$d(xy) = d(x) + f(x) \circ d(y),$$

so $d$ is an $f$-derivation. In the special case where $ph = 1_X$, one has the diagram

\[
\begin{CD}
X @>{h}>> A \rtimes G \\
@V{1_X}VV @VV{p}V \\
X @>>> G
\end{CD}
\]

and $A$ becomes an $X$-module via the composition of the inclusion $X \hookrightarrow G$ with the $G$-module structure of $A$. The derivation $d = qh$ is then a derivation from $X$ to $A$ with respect to this $X$-module structure. $\square$
