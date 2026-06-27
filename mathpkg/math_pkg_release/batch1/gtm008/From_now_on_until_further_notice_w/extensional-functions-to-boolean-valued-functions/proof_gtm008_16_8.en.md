---
role: proof
locale: en
of_concept: extensional-functions-to-boolean-valued-functions
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Define $f \in V^{(B)}$ with $\mathcal{D}(f) = \{\langle x, \varphi(x) \rangle^{(B)} \mid x \in \mathcal{D}(u)\}$ and appropriate values. The key step is verifying that $\llbracket f$ is a function$\rrbracket = 1$: for $x \in \mathcal{D}(u)$ and $y, z \in V^{(B)}$,

$$\llbracket \langle x, y \rangle \in f \rrbracket \cdot \llbracket \langle x, z \rangle \in f \rrbracket \leq \llbracket y = \varphi(x) \rrbracket \cdot \llbracket z = \varphi(x) \rrbracket \leq \llbracket y = z \rrbracket,$$

using the extensionality of $\varphi$. This proves that $f$ is function-like in the Boolean-valued sense. One then verifies $\llbracket f: u \rightarrow v \rrbracket = 1$ and pointwise equality.
