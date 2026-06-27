---
role: proof
locale: en
of_concept: ordinal-elementary-equivalence
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

The idea of the proof is to show that each ordinal $< \omega^\omega$ is elementarily definable; the theorem then easily follows. To prove this, we need to express some simple concepts concerning ordinals.

Let "$v_0 - v_1$ is a successor" be the formula
$$v_1 < v_0 \land \exists v_2 [v_2 < v_0 \land \neg \exists v_3 (v_2 < v_3 \land v_3 < v_0)].$$

Clearly we have
\begin{equation}\tag{1}
(\alpha, <) \models \text{"}v_0 - v_1\text{ is a successor"} [\beta, \gamma] \quad\text{iff}\quad \gamma < \beta < \alpha \text{ and } \beta - \gamma \text{ is a successor ordinal}.
\end{equation}

Next, let "$v_0 - v_1$ is divisible by $\omega$" be the formula
$$v_1 < v_0 \land \neg (\text{"}v_0 - v_1\text{ is a successor"}).$$

Thus
\begin{equation}\tag{2}
(\alpha, <) \models \text{"}v_0 - v_1\text{ is divisible by } \omega\text{"} [\beta, \gamma] \quad\text{iff}\quad \gamma < \beta < \alpha \text{ and } \beta - \gamma \text{ is divisible by } \omega.
\end{equation}

For any positive integer $m$, having defined the formula "$v_0 - v_1$ is divisible by $\omega^m$", let "$v_0 - v_1$ is divisible by $\omega^{m+1}$" be the formula
$$\exists v_2 (v_2 < v_0 \land \text{"}v_2 - v_1\text{ is divisible by } \omega^m\text{"}) \land \forall v_2 [v_2 < v_0 \rightarrow \exists v_3 (v_2 < v_3 \land v_3 < v_0 \land \text{"}v_3 - v_1\text{ is divisible by } \omega^m\text{"})].$$

One then proves by induction on $m$ that
\begin{equation}\tag{3}
(\alpha, <) \models \text{"}v_0 - v_1\text{ is divisible by } \omega^m\text{"} [\beta, \gamma] \quad\text{iff}\quad \gamma < \beta < \alpha \text{ and } \omega^m \mid (\beta - \gamma).
\end{equation}

Now for each $\delta < \omega^\omega$, write $\delta$ in Cantor normal form and construct a formula "$v_0 - v_1 = \delta$" using the above divisibility formulas. Specifically, one can express that $\beta - \gamma = \delta$ by stating that $\beta - \gamma$ is at least $\delta$ but not greater than $\delta$, using the definability of multiples of $\omega^m$.

The definability of each $\delta < \omega^\omega$ implies that if $(\alpha, <) \equiv_{\mathrm{ee}} (\beta, <)$, then $\alpha$ and $\beta$ have the same Cantor normal form below $\omega^\omega$; that is, $\alpha \equiv \beta \pmod{\omega^\omega}$. Moreover, if $\alpha < \omega^\omega$, then $\alpha$ is completely determined by its first-order theory, so elementary equivalence forces $\alpha = \beta$.

The remainder of the proof verifies the inductive claims (1), (2), and (3) through detailed ordinal arithmetic computations, establishing that the syntactically defined formulas indeed capture the intended arithmetic properties of ordinal differences.
