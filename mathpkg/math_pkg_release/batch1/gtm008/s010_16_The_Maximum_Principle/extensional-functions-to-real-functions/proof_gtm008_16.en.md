---
role: proof
locale: en
of_concept: extensional-functions-correspond-to-boolean-functions
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Define $f \in V^{(\mathbf{B})}$ by

$$\mathcal{D}(f) = \{\langle x, \varphi(x) \rangle \mid x \in \mathcal{D}(u)\}$$

and for $x \in \mathcal{D}(u)$,

$$f(\langle x, \varphi(x) \rangle) = 1.$$

We need to prove:

1. $\llbracket f \text{ is a function} \rrbracket = 1$,
2. $\llbracket \operatorname{dom}(f) = u \rrbracket = 1$,
3. $\llbracket \operatorname{ran}(f) \subseteq v \rrbracket = 1$ (which together give $\llbracket f: u \rightarrow v \rrbracket = 1$),
4. $(\forall x \in \mathcal{D}(u))[\llbracket f(x) = \varphi(x) \rrbracket = 1]$.

Since $u$ and $v$ are definite, the proof reduces to verifying the function condition.

Let $x \in \mathcal{D}(u)$ and $y, z \in V^{(\mathbf{B})}$. Then

$$\llbracket \langle x, y \rangle \in f \rrbracket = \sum_{x' \in \mathcal{D}(u)} \llbracket \langle x, y \rangle = \langle x', \varphi(x') \rangle \rrbracket$$
$$= \sum_{x' \in \mathcal{D}(u)} \llbracket x = x' \rrbracket \cdot \llbracket y = \varphi(x') \rrbracket$$
$$\leq \sum_{x' \in \mathcal{D}(u)} \llbracket \varphi(x) = \varphi(x') \rrbracket \cdot \llbracket y = \varphi(x') \rrbracket$$

since $\varphi$ is extensional (so $\llbracket x = x' \rrbracket \leq \llbracket \varphi(x) = \varphi(x') \rrbracket$)

$$\leq \llbracket y = \varphi(x) \rrbracket.$$

This shows that

$$\llbracket \langle x, y \rangle \in f \rrbracket \cdot \llbracket \langle x, z \rangle \in f \rrbracket \leq \llbracket y = \varphi(x) \rrbracket \cdot \llbracket z = \varphi(x) \rrbracket \leq \llbracket y = z \rrbracket,$$

which proves that $f$ is functional (property 1). From this and the definition of $f$, properties 2-4 follow: $\llbracket f: u \rightarrow v \rrbracket = 1$ and $(\forall x \in \mathcal{D}(u))[\llbracket f(x) = \varphi(x) \rrbracket = 1]$.
