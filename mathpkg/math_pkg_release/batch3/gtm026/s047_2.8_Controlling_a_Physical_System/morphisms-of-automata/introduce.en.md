---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Definition 2.17 formalizes the category of $X$-automata in a base category $\mathcal{K}$. An $X$-automaton is a 6-tuple $(Q, \delta, I, \tau, Y, \beta)$ consisting of a state object $Q$, an $X$-dynamics $\delta: QX \to Q$, an input object $I$ with input map $\tau: I \to Q$, and an output object $Y$ with output map $\beta: Q \to Y$. Morphisms between automata are required to commute with all three structure maps. The definition further characterizes reachability and observability using an image factorization system $(E, M)$: an automaton is reachable if its reachability map $r: IX^@ \to Q$ lies in $E$, and observable if its observability map $\sigma: Q \to YX^@$ lies in $M$.
