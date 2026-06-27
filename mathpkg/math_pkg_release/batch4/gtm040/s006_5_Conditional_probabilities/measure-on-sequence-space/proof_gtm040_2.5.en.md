---
role: proof
locale: en
of_concept: measure-on-sequence-space
source_book: gtm040
source_chapter: "2"
source_section: "5. Conditional probabilities"
---

By definition of conditional probability,
$$\Pr[x_0 = c_0 \wedge \cdots \wedge x_{n-1} = c_{n-1} \wedge x_n = c_n]$$
$$= \Pr[x_n = c_n \mid x_0 = c_0 \wedge \cdots \wedge x_{n-1} = c_{n-1}] \times \Pr[x_0 = c_0 \wedge \cdots \wedge x_{n-1} = c_{n-1}].$$

Applying this identity repeatedly by induction yields
\begin{align*}
\Pr[x_0 = c_0 \wedge \cdots \wedge x_n = c_n]
&= \Pr[x_0 = c_0] \cdot \Pr[x_1 = c_1 \mid x_0 = c_0] \\
&\quad \times \Pr[x_2 = c_2 \mid x_0 = c_0 \wedge x_1 = c_1] \\
&\quad \times \Pr[x_3 = c_3 \mid x_0 = c_0 \wedge x_1 = c_1 \wedge x_2 = c_2] \\
&\quad \times \cdots \\
&\quad \times \Pr[x_n = c_n \mid x_0 = c_0 \wedge \cdots \wedge x_{n-1} = c_{n-1}].
\end{align*}

Thus the measure is completely determined by the starting probabilities and the transition probabilities as claimed.
