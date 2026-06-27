---
role: proof
locale: en
of_concept: lemma-8-65
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

The function ${}_m z - {}_m z^{(1)}$ is analyzed by cases:
$${}_m z - {}_m z^{(1)} = \begin{cases}
z - z^{(1)} & \text{if } z \leq m \\[4pt]
0 & \text{if } z^{(1)} > m \\[4pt]
m - z^{(1)} & \text{if } z > m \geq z^{(1)}.
\end{cases}$$
In the first case, $z - z^{(1)}$ clearly dominates. In the second case, $z^{(1)} > m$, so ${}_m z^{(1)} = m = {}_m z$ (since $z \geq z^{(1)} > m$), giving zero difference. In the third case, $z > m \geq z^{(1)}$, we have $m - z^{(1)} \leq z - z^{(1)}$ because $m < z$. Thus in all cases $0 \leq {}_m z - {}_m z^{(1)} \leq z - z^{(1)}$.
