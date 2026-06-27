---
role: proof
locale: en
of_concept: henkin-model-existence
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

Let $B = \{\sigma : \sigma \text{ is a term of } \mathcal{L}, \text{ and no variable occurs in } \sigma\}$. Define an equivalence relation $\equiv$ on $B$ by

$$\{(\sigma, \tau) : \sigma, \tau \in B \text{ and } \Gamma \vdash \sigma = \tau\}.$$

By the equality axioms (reflexivity, symmetry, transitivity), $\equiv$ is indeed an equivalence relation on $B$. Let $[\sigma]$ denote the equivalence class of $\sigma$ and set $A = B/{\equiv}$.

For each operation symbol $\mathbf{O}$ of rank $m$, define an $m$-ary operation $\mathbf{O}^{\mathfrak{A}}$ on $A$ by

$$\mathbf{O}^{\mathfrak{A}}([\sigma_0], \ldots, [\sigma_{m-1}]) = [\mathbf{O}\sigma_0 \cdots \sigma_{m-1}].$$

For each relation symbol $\mathbf{R}$ of rank $m$, let $\mathbf{R}^{\mathfrak{A}}$ be the collection of all $m$-tuples $([\sigma_0], \ldots, [\sigma_{m-1}])$ such that $\Gamma \vdash \mathbf{R}\sigma_0 \cdots \sigma_{m-1}$. This defines the $\mathcal{L}$-structure $\mathfrak{A}$.

We now prove the key lemma: for any sentence $\varphi$,

$$\Gamma \vdash \varphi \quad\text{iff}\quad \varphi \text{ holds in } \mathfrak{A}.$$

The proof is by induction on $\varphi$.

**Atomic case $\varphi = (\sigma = \tau)$:**

$$\Gamma \vdash \sigma = \tau \;\Longleftrightarrow\; [\sigma] = [\tau] \;\Longleftrightarrow\; \sigma^{\mathfrak{A}} = \tau^{\mathfrak{A}} \;\Longleftrightarrow\; \mathfrak{A} \models \sigma = \tau.$$

**Atomic case $\varphi = \mathbf{R}\sigma_0 \cdots \sigma_{m-1}$:** If $\Gamma \vdash \varphi$, then by definition $([\sigma_0], \ldots, [\sigma_{m-1}]) \in \mathbf{R}^{\mathfrak{A}}$, so $\mathfrak{A} \models \varphi$. Conversely, if $\mathfrak{A} \models \varphi$, then $([\sigma_0], \ldots, [\sigma_{m-1}]) \in \mathbf{R}^{\mathfrak{A}}$, so by definition there exist $\tau_0, \ldots, \tau_{m-1} \in B$ with $[\sigma_i] = [\tau_i]$ for each $i$ and $\Gamma \vdash \mathbf{R}\tau_0 \cdots \tau_{m-1}$. Using the equality axioms repeatedly, $\Gamma \vdash \mathbf{R}\sigma_0 \cdots \sigma_{m-1}$.

**Induction steps for $\neg$, $\lor$, $\land$** follow from the completeness of $\Gamma$ and the induction hypothesis: for instance, $\Gamma \vdash \neg\psi$ iff $\Gamma \not\vdash \psi$ (by completeness and consistency), iff $\mathfrak{A} \not\models \psi$ (by IH), iff $\mathfrak{A} \models \neg\psi$.

**Quantifier case:** Since $\Gamma$ is rich, by Proposition 11.10 every sentence is provably equivalent to a quantifier-free one, reducing to the cases already handled.

Thus $\mathfrak{A} \models \Gamma$, and $|A| \leq |B|$ as required.
