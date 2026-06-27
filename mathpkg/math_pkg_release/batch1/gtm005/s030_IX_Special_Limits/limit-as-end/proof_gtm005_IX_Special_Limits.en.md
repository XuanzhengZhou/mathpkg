---
role: proof
locale: en
of_concept: limit-as-end
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Let $T : C \to X$ and define $S = T \circ Q : C^{\mathrm{op}} \times C \to X$, where $Q(c, c') = c'$. A cone $\tau : e \Rightarrow T$ with components $\tau_c : e \to T(c)$ satisfies the naturality condition $\tau_c = T(f) \circ \tau_b$ for each $f : b \to c$. This means the square

\[
\begin{CD}
e @>{\tau_b}>> T(b) = S(b, b) \\
@| @VV{S(1, f)}V \\
e @>>{\tau_c}> T(c) = S(b, c)
\end{CD}
\]

commutes (since $S(-, -)$ ignores the first variable, the right-hand map from $S(c,c) = T(c)$ to $S(b,c) = T(c)$ is the identity). Together with the dual condition (which is vacuous since $S$ is dummy in the first variable), this is exactly the condition for $\tau : e \xrightarrow{\bullet} S$ to be a dinatural wedge.

Conversely, any wedge $\tau : e \xrightarrow{\bullet} S$ yields a cone $\tau : e \Rightarrow T$ because the dinaturality hexagon collapses to the naturality square when $S$ is dummy in the first argument. Universality is preserved: a map factoring through $e$ for $T$-cones is the same as a map factoring for $S$-wedges. Hence the limit and the end coincide.
