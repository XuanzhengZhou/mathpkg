---
role: proof
locale: en
of_concept: extensional-functions-induce-boolean-valued-functions
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Define $f \in V^{(\mathbf{B})}$ with domain
$$\mathcal{D}(f) = \{\langle x, \varphi(x) \rangle \mid x \in \mathcal{D}(u)\}$$
and truth values given by interpreting $\langle x, \varphi(x) \rangle$ as elements of $V^{(\mathbf{B})}$.

To show $\llbracket f: u \to v \rrbracket = 1$, we must verify two things: (1) $f$ satisfies the single-valued condition in the Boolean-valued sense, and (2) the range is contained in $v$.

For (1), let $x \in \mathcal{D}(u)$ and $y, z \in V^{(\mathbf{B})}$. Then
\begin{align*}
\llbracket \langle x, y \rangle \in f \rrbracket &= \sum_{x' \in \mathcal{D}(u)} \llbracket \langle x, y \rangle = \langle x', \varphi(x') \rangle \rrbracket \\
&= \sum_{x' \in \mathcal{D}(u)} \llbracket x = x' \rrbracket \cdot \llbracket y = \varphi(x') \rrbracket \\
&\leq \sum_{x' \in \mathcal{D}(u)} \llbracket \varphi(x) = \varphi(x') \rrbracket \cdot \llbracket y = \varphi(x') \rrbracket \quad\text{(since $\varphi$ is extensional)} \\
&\leq \llbracket y = \varphi(x) \rrbracket.
\end{align*}

Hence
$$\llbracket \langle x, y \rangle \in f \rrbracket \cdot \llbracket \langle x, z \rangle \in f \rrbracket \leq \llbracket y = \varphi(x) \rrbracket \cdot \llbracket z = \varphi(x) \rrbracket \leq \llbracket y = z \rrbracket,$$
which proves the single-valued condition, hence condition (1). From (1) we obtain that $f$ is a function in $V^{(\mathbf{B})}$. Since $u$ and $v$ are definite, straightforward calculations give $\llbracket f: u \to v \rrbracket = 1$.

For (2), let $x \in \mathcal{D}(u)$. Interpreting $f(x) = \varphi(x)$ as $(\exists y)[\langle x, y \rangle \in f \land y = \varphi(x)]$, the definition of $f$ directly yields $\llbracket f(x) = \varphi(x) \rrbracket = 1$.
