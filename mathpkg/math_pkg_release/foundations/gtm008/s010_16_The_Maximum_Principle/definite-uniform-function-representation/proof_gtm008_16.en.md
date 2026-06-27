---
role: proof
locale: en
of_concept: definite-uniform-function-representation
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $u, v \in V^{(\mathbf{B})}$ be definite and uniform, and suppose $\llbracket f: u \rightarrow v \rrbracket = 1$.

Since $u$ and $v$ are uniform, their domains $\mathcal{D}(u)$ and $\mathcal{D}(v)$ are complete. Since $\llbracket f: u \rightarrow v \rrbracket = 1$, we have $\llbracket (\forall x \in u)(\exists! y \in v)[\langle x, y \rangle \in f] \rrbracket = 1$.

For each $x \in \mathcal{D}(u)$, since $u$ is definite we have $\llbracket x \in u \rrbracket = 1$, and therefore

$$\llbracket (\exists! y \in v)[\langle x, y \rangle \in f] \rrbracket = 1.$$

By the Maximum Principle (Theorem 16.2) applied to the formula $\psi(y) \equiv \langle x, y \rangle \in f$, there exists $\varphi(x) \in V^{(\mathbf{B})}$ such that

$$\llbracket \langle x, \varphi(x) \rangle \in f \rrbracket = 1.$$

Moreover, since $\llbracket f: u \rightarrow v \rrbracket = 1$, we must have $\llbracket \varphi(x) \in v \rrbracket = 1$. Because $v$ is definite and uniform, this implies $\varphi(x) \in \mathcal{D}(v)$ (up to Boolean equality 1). Thus we obtain a real function $\varphi: \mathcal{D}(u) \rightarrow \mathcal{D}(v)$.

To verify $\varphi$ is extensional: for $x, x' \in \mathcal{D}(u)$,

$$\llbracket x = x' \rrbracket = \llbracket x = x' \rrbracket \cdot \llbracket \langle x, \varphi(x) \rangle \in f \rrbracket \cdot \llbracket \langle x', \varphi(x') \rangle \in f \rrbracket$$
$$\leq \llbracket \varphi(x) = \varphi(x') \rrbracket$$

since $f$ is a Boolean-valued function. This establishes extensionality.

Finally, by construction $\llbracket f(x) = \varphi(x) \rrbracket = 1$ for all $x \in \mathcal{D}(u)$, which completes the proof.
