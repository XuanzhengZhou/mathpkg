---
role: proof
locale: en
of_concept: existential-forcing-property
source_book: gtm008
source_chapter: "10"
source_section: "10"
---

We have the equivalence:
$$
p \Vdash (\exists x)\varphi(x) \leftrightarrow p \in \sum_{t \in T} \llbracket \varphi(t) \rrbracket = \left(\bigcup_{t \in T} \llbracket \varphi(t) \rrbracket\right)^{-0}
$$
$$
\leftrightarrow [p] \subseteq \left(\bigcup_{t \in T} \llbracket \varphi(t) \rrbracket\right)^{-1}.
$$

Thus $p \Vdash (\exists x)\varphi(x)$ implies that $\bigcup_{t \in T} \llbracket \varphi(t) \rrbracket$ is dense beneath $p$, and the same holds for $S' = [p] \cap \bigcup_{t \in T} \llbracket \varphi(t) \rrbracket$. Moreover, $S' \in M$ since $B \in M$.

Therefore, by Theorem 10.11,
$$
p \Vdash (\exists x)\varphi(x) \to (\exists q \in G)\left[q \leq p \land q \in \bigcup_{t \in T} \llbracket \varphi(t) \rrbracket\right],
$$
which yields $(\exists q \leq p)(\exists t \in T)(q \in G \land q \Vdash \varphi(t))$.
