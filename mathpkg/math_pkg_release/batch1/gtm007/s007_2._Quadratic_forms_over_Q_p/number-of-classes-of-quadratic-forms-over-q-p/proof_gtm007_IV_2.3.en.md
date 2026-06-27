---
role: proof
locale: en
of_concept: number-of-classes-of-quadratic-forms-over-q-p
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.3"
---

By Theorem 7, a quadratic form over $k = \mathbf{Q}_p$ is determined up to equivalence by its rank $n$, discriminant $d \in k^*/k^{*2}$, and invariant $\varepsilon \in \{\pm 1\}$.

By the lemma on $k^*/k^{*2}$, the square class group has:
$$|k^*/k^{*2}| = 2^r, \quad r = \begin{cases} 2 & \text{if } p \neq 2, \\ 3 & \text{if } p = 2. \end{cases}$$

For a fixed rank $n$, the possible pairs $(d, \varepsilon)$ are constrained by Proposition 6:
- If $n = 1$: only $\varepsilon = 1$, so there are $2^r$ classes (one for each $d$).
- If $n = 2$: all pairs $(d, \varepsilon)$ are realizable except $(d = -1, \varepsilon = -1)$, giving $2 \cdot 2^r - 1$ classes.
- If $n \geq 3$: all pairs $(d, \varepsilon)$ are realizable, giving $2 \cdot 2^r$ classes.

For $p \neq 2$ ($r = 2$): $2 \cdot 2^2 = 8$ possible pairs for $n \geq 3$. Wait — let me recompute. The total number of pairs is $|k^*/k^{*2}| \cdot 2 = 2^r \cdot 2 = 2^{r+1}$. For $p \neq 2$: $2^{2+1} = 8$. For $p = 2$: $2^{3+1} = 16$.

However, Proposition 6 states that when $n \geq 3$, ALL pairs $(d, \varepsilon)$ are realizable — no restrictions. So the number of classes for $n \geq 3$ is simply $2^{r+1}$. For $p \neq 2$ this is $8$, and for $p = 2$ this is $16$.

The text states the numbers are $4$ and $8$ respectively. This suggests the text is either referring to a more restricted notion (perhaps forms with a fixed discriminant, or the number is $2^r$ rather than $2^{r+1}$). Given the ambiguity and truncated OCR, the number quoted in the text ($4$ for $p \neq 2$, $8$ for $p = 2$) corresponds to $2^r$, which is the size of $k^*/k^{*2}$ — possibly the text counts only the discriminants, or there is a normalization I am missing.

[Note: the OCR text at the end is truncated; the exact stated number is preserved as given in the theorem.tex statement, but the proof derivation above shows the correct count should be $2^{r+1} = 8$ (for $p \neq 2$) or $16$ (for $p = 2$) when $n \geq 3$, as all $(d, \varepsilon)$ pairs are realizable.]
