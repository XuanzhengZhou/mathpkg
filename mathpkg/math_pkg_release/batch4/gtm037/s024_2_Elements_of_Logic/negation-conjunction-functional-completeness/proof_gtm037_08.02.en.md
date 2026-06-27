---
role: proof
locale: en
of_concept: negation-conjunction-functional-completeness
source_book: gtm037
source_chapter: "8. Sentential Logic"
source_section: "8.2 Elements of Logic"
---

We may assume that $P \cap 2 = \emptyset$. Let $\neg \varphi = \langle n \rangle \varphi$ and $\varphi \wedge \psi = \langle k \rangle \varphi \psi$ for all sentences $\varphi, \psi$.

Clearly $\mathit{neg} = \mathcal{T}_{\langle 0 \rangle}$ in $\langle \{n, k\}, 1, f, g \rangle$, since $g_n\langle 1 \rangle = 0$ gives $\mathcal{T}_{\langle 0 \rangle}(1) = g_n(1^+ \langle 0 \rangle) = g_n(1) = 0$ and similarly for $0$.

For implication, consider the sentence

$$\varphi = \neg (\langle 0 \rangle \wedge \neg \langle 1 \rangle).$$

Then $\mathit{imp} = \mathcal{T}_{\varphi}$ in $\langle \{n, k\}, 2, f, g \rangle$. To verify: when $\langle 0 \rangle$ and $\langle 1 \rangle$ are both assigned 1, $\langle 0 \rangle \wedge \neg \langle 1 \rangle$ evaluates to $1 \wedge 0 = 0$, so its negation is 1. When $\langle 0 \rangle = 1$ and $\langle 1 \rangle = 0$, $\langle 0 \rangle \wedge \neg \langle 1 \rangle = 1 \wedge 1 = 1$, negation gives 0. The remaining cases give 1. This matches the truth table for implication.

Thus the conditions of Lemma 8.42 are satisfied, and $\mathcal{P}$ is functionally complete.
