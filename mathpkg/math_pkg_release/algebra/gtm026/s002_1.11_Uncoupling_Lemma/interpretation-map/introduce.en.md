---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The interpretation map $r^\#: V\Omega \longrightarrow X$ formalizes the evaluation of $\Omega$-terms with variables from $V$ in an $\Omega$-algebra $(X, \delta)$ under a variable assignment $r: V \to X$. It is defined as the composition of the substitution map $r\Omega$ (which replaces each variable by its assigned value) with the total description map $\delta^@$ (which evaluates the resulting term). Using this interpretation map, one defines what it means for an $\Omega$-algebra to satisfy an $\Omega$-equation $\{e_1, e_2\}$: the equality $e_1 r^\# = e_2 r^\#$ must hold under all variable assignments. An $(\Omega, E)$-algebra is then an $\Omega$-algebra that satisfies all equations in the equational presentation $E$, and its class forms a variety in the sense of universal algebra.
