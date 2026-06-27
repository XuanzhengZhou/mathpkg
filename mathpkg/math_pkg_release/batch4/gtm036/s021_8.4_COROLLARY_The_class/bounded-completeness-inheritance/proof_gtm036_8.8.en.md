---
role: proof
locale: en
of_concept: bounded-completeness-inheritance
source_book: gtm036
source_chapter: "8"
source_section: "8.8"
---

If $\{f_{\gamma}, \gamma \in \Gamma\}$ is a net which is a Cauchy net relative to the uniform topology, then $\{f_{\gamma}(t), \gamma \in \Gamma\}$ is a Cauchy net in $E$ for each $t$ in $S$. If $E$ is complete, it is then possible to choose a limit $f(t)$ of $\{f_{\gamma}(t), \gamma \in \Gamma\}$ for each $t$.

The key to the proposition is the observation that, if $t$ belongs to a member $A$ of $\mathcal{A}$, then the map which carries $f$ in $B_{\mathcal{A}}(S,E)$ into $f(t)$ is a continuous linear function on $B_{\mathcal{A}}(S,E)$, with the topology $\mathcal{T}_{\mathcal{A}}$, into $E$. (That is, uniform convergence on $A$ implies convergence at each point of $A$.) Consequently, if $G$ is a subset of $B_{\mathcal{A}}(S,E)$ which is bounded (or totally bounded) relative to $\mathcal{T}_{\mathcal{A}}$, then the set of all $f(t)$ for $f$ in $G$ is also bounded (totally bounded, respectively).

It follows that if $\{f_{\gamma}, \gamma \in \Gamma\}$ is a Cauchy net in a bounded set $G$, and if $E$ has the property that closed bounded sets are complete, then $\{f_{\gamma}(t), \gamma \in \Gamma\}$ converges to a limit $f(t)$ for each $t$ in $\bigcup \{A: A \in \mathcal{A}\}$. The argument of Lemma 8.5 then demonstrates the theorem.
