---
role: proof
locale: en
of_concept: extensional-representation
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

For $v \in V^{(\mathbf{B})}$ and $d \subseteq V^{(\mathbf{B})}$ such that $\mathcal{D}(v) \subseteq d$, define $u: d \to B$ by

$$(\forall x \in d)\; u(x) = \llbracket x \in v \rrbracket.$$

First, we verify extensionality. For $x \in d$,
$$u(x) = \llbracket x \in v \rrbracket \leq \llbracket x \in u \rrbracket = \sum_{y \in d} \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket \leq \llbracket x \in v \rrbracket = u(x).$$

Thus $u(x) = \llbracket x \in u \rrbracket$, which implies for $x, y \in d$:
$$\llbracket x = y \rrbracket \cdot u(x) = \llbracket x = y \rrbracket \cdot \llbracket x \in u \rrbracket \leq \llbracket y \in u \rrbracket = u(y),$$
so $u$ is extensional.

That $\llbracket u = v \rrbracket = 1$ follows from the same computation as in Theorem 16.1, since $u$ is exactly the extension of $v$ to domain $d$ defined there.
