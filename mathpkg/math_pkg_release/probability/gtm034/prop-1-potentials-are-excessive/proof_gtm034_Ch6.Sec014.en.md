---
role: proof
locale: en
of_concept: prop-1-potentials-are-excessive
source_book: gtm034
source_chapter: "6"
source_section: "014"
---

Proof: Part (1) follows from

$$\sum_{t \in S} Q(x,t)g(t,y) - g(x,y) = -\delta(x,y), \quad x,y \in S,$$

which shows that $g(x,y)$ is excessive as

To get (2) note that, if $Pf \leq f, Pg \leq g$, then

$$\min [f(x), g(x)] \geq \min \left[ \sum_{y \in S} P(x,y)f(y), \sum_{y \in S} P(x,y)g(y) \right]$$

$$\geq \sum_{y \in S} P(x,y) \min [f(y), g(y)].$$

Finally, suppose that $f(x)$ is a potential. If

$$f(x) = \sum_{y \in S} g(x,y)\psi(y) = g\psi(x),$$

then

$$Q_n f(x) = \sum_{y \in S} \psi(y) \left[ \sum_{k=n}^{\infty} Q_k(x,y) \right],$$

which tends to zero for each $x$ as $n \to \infty$.

A fundamental relation between the three classes of functions defined in D2 was discovered by F. Riesz ([86], p. 337). He showed that every excessive function may be written as the sum of a regular function and of a potential. This decomposition is unique, i.e., there is only one such decomposition for each excessive function. It is given explicitly by
