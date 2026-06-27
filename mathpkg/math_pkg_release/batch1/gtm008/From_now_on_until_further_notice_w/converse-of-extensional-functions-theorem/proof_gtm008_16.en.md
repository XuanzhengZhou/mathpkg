---
role: proof
locale: en
of_concept: converse-of-extensional-functions-theorem
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Since $\llbracket f: u \to v \rrbracket = 1$ and $u$ is definite, for each $x \in \mathcal{D}(u)$ we have $\llbracket x \in u \rrbracket = 1$, so $\llbracket (\exists y \in v) \langle x, y \rangle \in f \rrbracket = 1$.

By the Maximum Principle (Theorem 16.2), there exists $y \in V^{(\mathbf{B})}$ such that $\llbracket \langle x, y \rangle \in f \rrbracket = 1$ and $\llbracket y \in v \rrbracket = 1$. Since $v$ is definite, $\llbracket y \in v \rrbracket = 1$ means $\llbracket y = y' \rrbracket = 1$ for some $y' \in \mathcal{D}(v)$ (by the characterization of definite sets). Define $\varphi(x) = y'$.

To verify extensionality of $\varphi$: if $\llbracket x = x' \rrbracket = b$, then since $f$ is a function in $V^{(\mathbf{B})}$,
$$b \leq \llbracket \langle x, \varphi(x) \rangle \in f \land \langle x', \varphi(x') \rangle \in f \land x = x' \rrbracket \leq \llbracket \varphi(x) = \varphi(x') \rrbracket.$$

Thus $\varphi$ is extensional, and $\llbracket f(x) = \varphi(x) \rrbracket = 1$ for all $x \in \mathcal{D}(u)$ by construction.
