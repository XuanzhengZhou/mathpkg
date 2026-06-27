---
role: proof
locale: en
of_concept: powerset-monad-algebra-complete-semilattice
source_book: gtm005
source_chapter: "VI"
source_section: "1"
---

The category of Eilenberg-Moore algebras for the powerset monad $\mathcal{P}$ is isomorphic to the category of complete join-semilattices.

An algebra $\alpha: \mathcal{P}(X) \to X$ defines a complete join by $\bigvee S = \alpha(S)$. Properties:
- $\bigvee \emptyset = \alpha(\emptyset)$ (bottom element).
- $\bigvee \{x\} = \alpha(\{x\}) = x$ (unit law: $\alpha \circ \eta_X = 1_X$).
- Complete associativity: for a family $\{S_i\}_{i \in I}$ of subsets, $\bigvee(\bigcup_i S_i) = \bigvee_i (\bigvee S_i)$, which is exactly $\alpha(\bigcup_i S_i) = \alpha(\{\alpha(S_i) : i \in I\})$, the multiplication law $\alpha \circ \mu_X = \alpha \circ \mathcal{P}(\alpha)$.

Algebra homomorphisms $f: (X, \alpha) \to (Y, \beta)$ satisfy $f \circ \alpha = \beta \circ \mathcal{P}(f)$, which means $f(\bigvee S) = \bigvee f(S)$ — precisely join-preserving maps.
