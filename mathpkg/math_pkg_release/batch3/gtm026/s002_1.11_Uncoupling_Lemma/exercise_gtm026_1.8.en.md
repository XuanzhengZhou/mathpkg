---
role: exercise
locale: en
chapter: "1"
section: "1"
exercise_number: 8
---

Ianov's program schemata (see Rutledge '64 and the bibliography there) provide a "dual" concept to $\Omega$-terms. Fix an operator domain $\Omega$ with $\Omega_0 = \varnothing$. An *initialized $\Omega$-flowchart scheme* is a finite directed graph, with a distinguished "initial" node, in which every node of outdegree $n > 0$ is labelled with an element of $\Omega_n$; the nodes of outdegree $0$ are called *exits*. A partial function from $X$ to $Y$ is a function from a subset of $X$ to $Y$. An *$\Omega$-coalgebra* is a pair $(X, \delta)$ where $X$ is a set and $\delta$ assigns to $\omega \in \Omega_n$ a partial function $\delta_\omega: X \longrightarrow n \cdot X$ [where $n \cdot X = X + \cdots + X$ ($n$ times)].

(a) Regarding a flowchart scheme as an "abstract program" and an $\Omega$-coalgebra as a "machine," show that "running the program" results in a partial function $X \longrightarrow s \cdot X$.
