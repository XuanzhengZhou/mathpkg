---
role: proof
locale: en
of_concept: extensional-subset-theorem
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

**1.** $v'$ is extensional because multiplying $v$ by a scalar $b$ preserves extensionality:
$$\llbracket x = y \rrbracket \cdot v'(x) = \llbracket x = y \rrbracket \cdot b \cdot v(x) \leq b \cdot v(y) = v'(y).$$

**2.** Since $v$ is extensional, $v(x) = \llbracket x \in v \rrbracket$, and therefore $v'(x) = b \cdot \llbracket x \in v \rrbracket$. Thus
\begin{align*}
\llbracket v' \subseteq u \rrbracket &= \prod_{x \in \mathcal{D}(v)} (v'(x) \Rightarrow \llbracket x \in u \rrbracket) \\
&= \prod_{x \in \mathcal{D}(v)} (b \cdot \llbracket x \in v \rrbracket \Rightarrow \llbracket x \in u \rrbracket) \\
&= \prod_{x \in \mathcal{D}(v)} \llbracket v \subseteq u \land x \in v \to x \in u \rrbracket \\
&= 1.
\end{align*}

**3.** First, $\llbracket v = v' \rrbracket = \llbracket v = v' \rrbracket \cdot \llbracket v' \subseteq u \rrbracket \leq \llbracket v \subseteq u \rrbracket = b$ by part 2. On the other hand, $\llbracket v = v' \rrbracket = \llbracket v = b \cdot v \rrbracket \geq b$ by the Exercise (properties of scaled sets). Hence $\llbracket v = v' \rrbracket = b = \llbracket v \subseteq u \rrbracket$.
