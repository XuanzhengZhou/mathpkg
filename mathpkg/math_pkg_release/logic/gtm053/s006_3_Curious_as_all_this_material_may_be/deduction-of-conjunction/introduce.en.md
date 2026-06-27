---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma states that if two formulas $P$ and $Q$ are separately deducible from a set of formulas $\mathcal{E}$ that contains all tautologies, then their conjunction $P \wedge Q$ is also deducible from $\mathcal{E}$.

The proof simply concatenates the deductions of $P$ and $Q$ and appends a tautology $P \Rightarrow (Q \Rightarrow (P \wedge Q))$ together with two applications of modus ponens to obtain $P \wedge Q$.
