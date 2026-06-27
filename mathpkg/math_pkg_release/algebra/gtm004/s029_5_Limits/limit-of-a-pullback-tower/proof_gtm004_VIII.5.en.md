---
role: proof
locale: en
of_concept: limit-of-a-pullback-tower
source_book: gtm004
source_chapter: "VIII"
source_section: "5"
---

# Proof of Limit of a Pullback Tower

We are given a tower of objects and morphisms for $i \geq 1$:

$$
\begin{CD}
A_i @>{\varphi_i}>> B_i \\
@V{\alpha_i}VV @VV{\beta_i}V \\
A_{i-1} @>>{\varphi_{i-1}}> B_{i-1}
\end{CD}
\tag{5.6}
$$

where each square is a pullback. Set $A_\infty = \lim_i A_i$ and $B_\infty = \lim_i B_i$, with the canonical structure maps $\delta_i^A: A_\infty \to A_i$ and $\delta_i^B: B_\infty \to B_i$ given by the counit of the limit adjunction. Let

$$
\varphi_\infty = \lim_i \varphi_i: A_\infty \longrightarrow B_\infty,
$$

and let $\bar{\alpha}: A_\infty \to A_0$, $\bar{\beta}: B_\infty \to B_0$ be the induced limit morphisms (obtained as $\delta_0^A$ and $\delta_0^B$ composed with the counit at index $0$, or equivalently as $\alpha_1 \circ \delta_1^A$, etc.). We must prove that the induced square

$$
\begin{CD}
A_\infty @>{\varphi_\infty}>> B_\infty \\
@V{\bar{\alpha}}VV @VV{\bar{\beta}}V \\
A_0 @>>{\varphi_0}> B_0
\end{CD}
\tag{5.7}
$$

is a pullback.

*Proof.* Suppose we are given morphisms $\psi: X \to A_0$ and $\chi: X \to B_\infty$ such that

$$
\varphi_0 \circ \psi = \bar{\beta} \circ \chi.
$$

We must construct a unique morphism $\psi_\infty: X \to A_\infty$ satisfying $\bar{\alpha} \circ \psi_\infty = \psi$ and $\varphi_\infty \circ \psi_\infty = \chi$.

Set $\psi_0 = \psi: X \to A_0$, and define $\chi_1 = \delta_1^B \circ \chi: X \to B_1$, where $\delta_1^B: B_\infty \to B_1$ is the structure map of the limit $B_\infty$. We claim that

$$
\varphi_0 \circ \psi_0 = \beta_0 \circ \chi_1 \quad (\text{writing } \beta_0 = \beta_1).
$$

Indeed, using the universal property of the limit, $\bar{\beta} = \beta_1 \circ \delta_1^B = \beta_0 \circ \delta_1^B$, so

$$
\varphi_0 \circ \psi_0 = \varphi_0 \circ \psi = \bar{\beta} \circ \chi = \beta_0 \circ \delta_1^B \circ \chi = \beta_0 \circ \chi_1.
$$

Since the square for $i = 1$ in (5.6) is a pullback, there exists a unique morphism $\psi_1: X \to A_1$ such that

$$
\varphi_1 \circ \psi_1 = \chi_1, \qquad \alpha_1 \circ \psi_1 = \psi_0.
$$

Proceeding by induction, assume we have constructed $\psi_{i-1}: X \to A_{i-1}$. Define $\chi_i = \delta_i^B \circ \chi: X \to B_i$. One checks that $\varphi_{i-1} \circ \psi_{i-1} = \beta_{i-1} \circ \chi_i$, so by the pullback property of the $i$-th square, we obtain a unique $\psi_i: X \to A_i$ with

$$
\varphi_i \circ \psi_i = \chi_i, \qquad \alpha_i \circ \psi_i = \psi_{i-1}.
$$

Thus we obtain a family of morphisms $\{\psi_i: X \to A_i\}_{i \geq 0}$ satisfying $\alpha_i \circ \psi_i = \psi_{i-1}$ for all $i \geq 1$. By the universal property of the limit $A_\infty = \lim_i A_i$, there exists a unique morphism $\psi_\infty: X \to A_\infty$ such that

$$
\delta_i^A \circ \psi_\infty = \psi_i \quad \text{for all } i \geq 0.
$$

In particular, for $i = 0$, we have $\bar{\alpha} \circ \psi_\infty = \delta_0^A \circ \psi_\infty = \psi_0 = \psi$, so the first required condition holds.

For the second condition, we compute, for each $i \geq 0$,

$$
\delta_i^B \circ \varphi_\infty \circ \psi_\infty = \varphi_i \circ \delta_i^A \circ \psi_\infty = \varphi_i \circ \psi_i = \chi_i = \delta_i^B \circ \chi.
$$

Since the morphisms $\delta_i^B$ are jointly monic (by the universal property of the limit), we deduce $\varphi_\infty \circ \psi_\infty = \chi$.

Finally, the uniqueness of $\psi_\infty$ follows from the uniqueness at each inductive step: any other morphism $\psi_\infty'$ satisfying the same conditions would project to a family $\{\delta_i^A \circ \psi_\infty'\}$ that must coincide with $\{\psi_i\}$ by the uniqueness in each pullback square, hence $\psi_\infty' = \psi_\infty$ by the universal property of the limit. $\square$

**Remark.** This proof is purely categorical and uses only the existence of the relevant limits together with the universal property of pullbacks and limits. No elementwise arguments or abelian-category hypotheses are required. Together with its dual (for colimits of a co-tower of pushout squares), this result provides the essential tool for handling the limit and colimit processes in the proof of Theorem 5.3 on spectral sequences.
