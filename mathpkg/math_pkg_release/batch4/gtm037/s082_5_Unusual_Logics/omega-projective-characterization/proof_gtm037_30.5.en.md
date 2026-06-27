---
role: proof
locale: en
of_concept: omega-projective-characterization
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

Let $\mathcal{L}'$ be an expansion of $\mathcal{L}$ by adding a new binary relation symbol $R$ and a new ternary relation symbol $S$, and let $\mathcal{L}''$ be an $\omega$-expansion of $\mathcal{L}'$. Now we shall associate with each second-order formula $\varphi$ of $\mathcal{L}$ a formula $\varphi^*$ of $\mathcal{L}''$; we shall assume that $\mathcal{L}''$ is supplied with certain new individual variables $F_{i0}, F_{i1}$ for $i \in \omega$:

$$(\sigma = \tau)^* = \sigma = \tau;$$
$$(P\sigma_0 \cdots \sigma_{m-1})^* = P\sigma_0 \cdots \sigma_{m-1};$$
$$(F_i\sigma)^* = SF_{i0}F_{i1}\sigma;$$
$$(\neg\varphi)^* = \neg\varphi^*; \quad (\varphi \vee \psi)^* = \varphi^* \vee \psi^*; \quad (\varphi \wedge \psi)^* = \varphi^* \wedge \psi^*;$$
$$(\forall v_i\varphi)^* = \forall v_i\varphi^*;$$
$$(\forall F_i\varphi)^* = \forall F_{i0}\forall F_{i1}(RF_{i0}F_{i1} \rightarrow \varphi^*).$$

Let $\Omega$ be the theory in $\mathcal{L}''$ consisting of:
- $\Theta^* = \{\varphi^* : \varphi \in \Theta\}$,
- $\forall v_0 \mathbf{N}v_0$,
- $\forall v_0(\mathbf{N}v_0 \rightarrow \bigvee_{i<\omega} v_0 = \mathbf{c}_i)$,
- $\mathbf{c}_i \neq \mathbf{c}_j$ for $i \neq j$,
- axioms ensuring $R$ encodes a pairing function on $\mathbf{N}$,
- axioms ensuring $S$ encodes the evaluation of a function coded by $F_{i0}, F_{i1}$.

For any $\mathcal{L}$-structure $\mathfrak{A}$, let $\mathfrak{A}^*$ be the $\mathcal{L}''$-structure with universe $A \cup \omega \cup ({}^\omega A)$, where $\mathbf{N}^{\mathfrak{A}^*} = \omega$, $\mathbf{c}_i^{\mathfrak{A}^*} = i$, and $R, S$ are interpreted in the natural way.

One then shows by induction on $\varphi$ that for any $\mathcal{L}$-structure $\mathfrak{A}$ and assignment $x$,
$$\mathfrak{A} \models \varphi[x] \quad \text{iff} \quad \mathfrak{A}^* \models \varphi^*[x'].$$

This is easily shown by induction on $\varphi$. Now it follows that if $\mathfrak{A}$ is a model of $\Theta$, then $\mathfrak{A}^*$ is a model of $\Omega$. Conversely, it is easily seen that any $\omega$-model $\mathfrak{B}$ of $\Omega$ is isomorphic to $\mathfrak{A}^*$ for some $\mathcal{L}$-structure $\mathfrak{A}$, so the $\mathcal{L}$-reduct of $\mathfrak{B}$ is a model of $\Theta$.
