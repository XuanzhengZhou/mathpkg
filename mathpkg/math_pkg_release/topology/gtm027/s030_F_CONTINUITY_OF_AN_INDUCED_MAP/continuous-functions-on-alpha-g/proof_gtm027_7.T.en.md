---
role: proof
locale: en
of_concept: continuous-functions-on-alpha-g
source_book: gtm027
source_chapter: "7"
source_section: "T"
---

# Proof of Isometric Isomorphism Between Continuous Functions on the Compactification and Almost Periodic Functions

The family of continuous real functions on $\alpha[G]$ is isometric (and isomorphic as an algebra) to $A$, the algebra of left almost periodic functions on $G$.

**Proof.** **(First direction:)** If $g : \alpha[G] \to \mathbb{R}$ is continuous, then $g \circ L : G \to \mathbb{R}$ is continuous. Since $\alpha[G]$ is compact, $g$ is bounded, so $g \circ L$ is bounded. Moreover, the set of left translates of $g \circ L$ corresponds under $L$ to the set of functions $R \mapsto g(R \circ L_x)$. Since $\alpha[G]$ is the closure of the left translations and $g$ is uniformly continuous (compact domain), the set of translates is totally bounded, so $g \circ L$ is left almost periodic. Thus $g \mapsto g \circ L$ maps $C(\alpha[G])$ into $A$.

**(Second direction:)** If $f \in A$, define $\tilde{f} : \alpha[G] \to \mathbb{R}$ by

$$\tilde{f}(R) = R^{-1}(f)(e),$$

where $e$ is the identity of $G$. (The inverse $R^{-1}$ exists in the group $\alpha[G]$ — here one uses that $\alpha[G]$ is a topological group.) Then $\tilde{f}$ is continuous on $\alpha[G]$ (by definition of the topology on $\alpha[G]$ and joint continuity properties) and satisfies $\tilde{f}(L_x) = L_{x^{-1}}(f)(e) = f(x)$. Thus $f = \tilde{f} \circ L$.

The map $f \mapsto \tilde{f}$ is an isometric isomorphism of Banach algebras (with supremum norm). The isometry follows from

$$\|f\| = \sup_{x \in G} |f(x)| = \sup_{x \in G} |\tilde{f}(L_x)| = \sup_{R \in \alpha[G]} |\tilde{f}(R)| = \|\tilde{f}\|,$$

since $\{L_x : x \in G\}$ is dense in $\alpha[G]$ and $\tilde{f}$ is continuous.
