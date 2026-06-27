---
role: proof
locale: en
of_concept: craigs-theorem
source_book: gtm037
source_chapter: "15"
source_section: "3. Decidable and Undecidable Theories"
---

Obviously $(i) \Rightarrow (ii)$, while $(ii) \Rightarrow (iii)$ by 10.29. Now assume that $(iii)$ holds. Let $f$ be an elementary function with range $g^{+*}\Gamma$. Set

$$\Delta = \{ \varphi : \varphi \text{ is a sentence, and there is an } x \leq g^{+}\varphi \text{ such that } fx = g^{+}\psi \text{ for some sentence } \psi \text{ such that } \varphi = \psi \land \psi \land \cdots \land \psi \}.$$

Obviously $g^{+*}\Delta$ is elementary, and $\Delta \subseteq \Gamma$. Now suppose that $\psi \in \Gamma$. Choose $x$ so that $fx = g^{+}\psi$. Clearly we can find a sentence $\varphi$ of the form $\psi \land \psi \land \cdots \land \psi$ such that $g^{+}\varphi \geq x$. This follows from the simple observation that $g^{+}(\theta_0 \land \theta_1) > g^{+}\theta_i$ for $i = 0, 1$. Then $\varphi \in \Delta$, and $\varphi \vdash \psi$, so $\Delta$ axiomatizes $\Gamma$.

[Note: The proof in the source text is partially truncated. The final sentence has been reconstructed from mathematical context.]
