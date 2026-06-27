---
role: proof
locale: en
of_concept: clone-monoid-bijection
source_book: gtm026
source_chapter: "3"
source_section: "3.18"
---

The inverse passage can only be achieved by the formula of 3.14. For the forward direction, the construction of $(T, \eta, \mu)$ from $(T, \eta, \circ)$ is given by 3.10 (definition of $fT$), 3.11 (definition of $g^\Delta$), 3.13 (definition of $\mu$ via $\circ$), 3.15 (naturality of $\mu$), and 3.16 (the three commutative diagrams). The inverse direction recovers $\circ$ from $\mu$ via the Kleisli composition law: $\alpha \circ \beta = \alpha.\beta^\#$ where $\beta^\# = (\beta T).(C\mu)$. The proof that these passages are mutually inverse relies on the algebraic identities established in 3.12, 3.14, 3.15, and the three diagrams of 3.16.

For the ultrafilter example in $\mathbf{Set}$: define $\langle x, X\eta \rangle = \mathrm{prin}(x) \in XT$, where $\mathrm{prin}(x)$ is the principal ultrafilter on $x$ defined by $\mathrm{prin}(x) = \{A \subset X : x \in A\}$. For $f: X \longrightarrow Y$, $fT$ is defined by $\langle \mathcal{A}, fT \rangle = \{B \subset Y : Bf^{-1} \in \mathcal{A}\}$. $X\mu: XTT \longrightarrow XT$ is defined by $\langle \bar{\mathcal{A}}, X\mu \rangle = \{A \subset X : \{\mathcal{A} \in XT : A \in \mathcal{A}\} \in \bar{\mathcal{A}}\}$. The proof that $(T, \eta, \circ)$ is an algebraic theory is left as an exercise.
