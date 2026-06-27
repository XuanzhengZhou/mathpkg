---
role: proof
locale: en
of_concept: pullback-characterization-lemma
source_book: gtm004
source_chapter: "III. Extensions of Modules"
source_section: "1. Extensions"
---

# Proof of Lemma 1.1: Pullback Characterization via Exact Sequence

Consider the square

\[
\begin{CD}
Y @>\alpha>> A \\
@V\beta VV @VV\varphi V \\
B @>>\psi> X
\end{CD}
\tag{1.2}
\]

For any $\Lambda$-module $Z$, maps $\gamma: Z \to A$ and $\delta: Z \to B$ make the diagram

\[
\begin{CD}
Z @>\gamma>> A \\
@V\delta VV @VV\varphi V \\
B @>>\psi> X
\end{CD}
\]

commutative if and only if they induce a map $\{\gamma, \delta\}: Z \to A \oplus B$ such that $\langle \varphi, -\psi \rangle \circ \{\gamma, \delta\} = 0$. The universal property of the kernel asserts the existence of a unique map $\zeta: Z \to Y$ with $\{\alpha, \beta\} \circ \zeta = \{\gamma, \delta\}$. The universal property of the pullback asserts the existence of a unique map $\zeta: Z \to Y$ with $\alpha \circ \zeta = \gamma$ and $\beta \circ \zeta = \delta$.

These two universal properties are equivalent. Therefore, the square (1.2) is a pullback diagram if and only if the sequence

\[
0 \longrightarrow Y \xrightarrow{\{\alpha,\beta\}} A \oplus B \xrightarrow{\langle\varphi, -\psi\rangle} X
\]

is exact. $\square$
