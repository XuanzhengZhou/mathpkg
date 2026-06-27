---
role: proof
locale: en
of_concept: bilinear-form-linear-transformation-isomorphism
source_book: gtm023
source_chapter: "II"
source_section: "2.33"
---

Let $x \in E$ be a fixed vector and consider the linear function $f_x$ in $E^*$ defined by

$$f_x(x^*) = \Phi(x^*, x).$$

In view of Proposition I, there is precisely one vector $\varphi x \in E$ such that

$$f_x(x^*) = \langle x^*, \varphi x \rangle.$$

The two above equations yield

$$\langle x^*, \varphi x \rangle = \Phi(x^*, x), \quad x^* \in E^*, \quad x \in E,$$

and so a mapping $\varphi: E \rightarrow E$ is defined. The linearity of $\varphi$ follows immediately from the bilinearity of $\Phi$. Suppose now that $\varphi_1$ and $\varphi_2$ are two linear transformations of $E$ such that

$$\Phi(x^*, x) = \langle x^*, \varphi_1 x \rangle \quad \text{and} \quad \Phi(x^*, x) = \langle x^*, \varphi_2 x \rangle.$$

Then $\langle x^*, \varphi_1 x - \varphi_2 x \rangle = 0$ for all $x^* \in E^*$, whence $\varphi_1 = \varphi_2$, establishing uniqueness.
