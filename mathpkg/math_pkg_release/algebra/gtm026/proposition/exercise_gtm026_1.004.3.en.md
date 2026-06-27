---
role: exercise
locale: en
chapter: "1"
section: "004"
exercise_number: 3
---

Algebraic Theories

Roughly speaking, the algebraic theory of an equational presentation $(\Omega, E)$ is its equivalence class in the various senses of 2.1

each $\mathcal{H}$-morphism $f: A \longrightarrow B$ induces $f^{\Delta}: A \longrightarrow B$ defined by

$$f^{\Delta} = A \xrightarrow{f} B \xrightarrow{B \eta} BT$$

The axioms on $T$, then, are:

(3.3) $(\alpha \circ \beta) \circ \gamma = \alpha \circ (\beta \circ \gamma)$ for all $\alpha: A \longrightarrow B$, $\beta: B \longrightarrow C$ and $\gamma: C \longrightarrow D$

$$\alpha \circ B \eta = \alpha \quad \text{for all} \quad \alpha: A \longrightarrow B$$

$$f^{\Delta} \circ \alpha = f.\alpha \quad \text{for all} \quad f: A \longrightarrow B, \quad \alpha: B \longrightarrow C$$

This defines a category, $\mathcal{K}_T$, with the same objects as $\mathcal{K}$, composition $\circ$, and identity morphisms $\eta$ (set $f = \text{id}_A$ to prove that $A \eta \circ \alpha = \alpha$). $\mathcal{K}_T$ is called the Kleisli category of $T$.

3.4 Example. Let $(\Omega, E)$ be an equational presentation and let $T, \eta, \circ$ be as in 2.1, 2.9, and 2.8. Then $(T, \eta, \circ)$ is an algebraic theory in Set and $\text{Set}_T = \text{Set}(\Omega, E)$. To prove this we must check 3.3; indeed, $f^{\Delta} \circ \alpha = f^{\Delta}.\alpha^{\#} = f.(B \eta.\alpha^{\#}) = f.\alpha$.

3.5 Example. Sets and Relations. A relation from a set $A$ to a set $B$ is a subset $\alpha$ of $A \times B$. We may write $a \alpha b$ for $(a, b) \in \alpha$. Since $a \alpha b$ if and only if $b \in a

group-multiplication map. Define $A\eta:A \longrightarrow AT$ by $A = \binom{\text{id}_A}{e}$, where $e:A \longrightarrow G$ is constantly the group unit. It is not hard to prove that $(T, \eta, \circ)$ is an algebraic theory in $\mathcal{H}$.

In the first two sections of this book we extracted the algebraic theory of a bunch of algebras. In section 4, we will learn how algebras can be defined in terms of their theory. The point of Examples 3.5, 3.6, and 3.7 is that algebraic theories can arise naturally without first knowing what the algebras are. The reader might ponder just what kind of algebras are defined by these three examples; they are all relatively famous examples of “structures.”

Our immediate goal is to reformulate algebraic theories in clone form as algebraic theories in monoid form, with considerable technical gains. We begin by fixing an arbitrary algebraic theory $T = (T, \eta, \circ)$ (in clone form) in a category $\mathcal{H}$ and studying some formal consequences of Axiom 3.3.

3.8 Triple Product Law. Given $f:A \longrightarrow B$, $\beta:B \longrightarrow C$ and $\gamma:C \longrightarrow D$, $f.\beta \circ \gamma$ is well defined. For $(f.\beta) \circ \gamma = (f^\Delta \circ \beta) \circ \gamma = f^\Delta \circ (\beta \circ \gamma) = f.(\beta \circ \gamma)$. $\square$

3.9 Compatibility of Compositions. Given $f:A \longrightarrow B$ and $g:B \longrightarrow C$, then $(f.g)^\Delta = f^\Delta \circ g^\Delta$. Proof: $(f.g)^\Delta = f.g.C\eta = f.g^\Delta = f^\Delta \circ g^\Delta$. $\square$

3.10 Proposition. If for $f:A \longrightarrow B$ we define $fT:AT \longrightarrow BT = \text{id}_{AT}
