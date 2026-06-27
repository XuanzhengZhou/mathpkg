---
role: proof
locale: en
of_concept: recursive-forcing-conditions
source_book: gtm008
source_chapter: "10"
source_section: "10"
---

These recursive conditions follow from the definition $p \Vdash \varphi \triangleq p \in \llbracket \varphi \rrbracket$ and the properties of Boolean truth values in $B$-valued models:

1. $\llbracket \neg \varphi \rrbracket = -\llbracket \varphi \rrbracket$, so $p \in -\llbracket \varphi \rrbracket$ iff no $q \leq p$ satisfies $q \in \llbracket \varphi \rrbracket$ (since $[p]$ is a regular open set).

2. $\llbracket \varphi_1 \land \varphi_2 \rrbracket = \llbracket \varphi_1 \rrbracket \cap \llbracket \varphi_2 \rrbracket$, so $p \in \llbracket \varphi_1 \rrbracket \cap \llbracket \varphi_2 \rrbracket$ iff $p \in \llbracket \varphi_1 \rrbracket$ and $p \in \llbracket \varphi_2 \rrbracket$.

3. $\llbracket (\forall x)\varphi(x) \rrbracket = \bigcap_{t \in T} \llbracket \varphi(t) \rrbracket$, which yields the stated equivalence.

4. For bounded quantifiers $(\forall x^{\alpha})$, the truth value involves an approximation: $\llbracket (\forall x^{\alpha})\varphi(x^{\alpha}) \rrbracket$ is the interior of the intersection, leading to the condition with $(\forall q \leq p)(\exists q' \leq q)$.

5-6. The conditions for $V(t)$ and $F(t)$ follow from the denotation operators defined in Definition 9.36 and the characterization of equality in the $B$-valued model.
