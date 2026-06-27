---
role: proof
locale: en
of_concept: tarski-elementary-chain-theorem
source_book: gtm037
source_chapter: "19"
source_section: "4. Model Theory"
---

**Proof.** We proceed by induction on formulas to show that for every formula $\varphi$, every $\mathcal{A} \in K$, and every $x \in {}^\omega A$,

$$
\mathcal{A} \models \varphi[x] \iff \bigcup K \models \varphi[x].
$$

The case $\varphi$ atomic is trivial, since $\mathcal{A} \subseteq \bigcup K$ by Proposition 19.35. The induction steps for $\neg$, $\lor$, and $\land$ are obvious.

Now suppose $\mathcal{A} \in K$, $x \in {}^\omega A$, and $\mathcal{A} \models \forall v_i \varphi[x]$. To show that $\bigcup K \models \forall v_i \varphi[x]$, let $b \in \bigcup K$ be arbitrary, say $b \in \mathcal{B} \in K$. Since $K$ is directed by $\preceq$, choose $\mathcal{C} \in K$ with $\mathcal{A} \preceq \mathcal{C}$ and $\mathcal{B} \preceq \mathcal{C}$. Now $\mathcal{A} \preceq \mathcal{C}$ and $\mathcal{A} \models \forall v_i \varphi[x]$ imply $\mathcal{C} \models \forall v_i \varphi[x]$. Hence $\mathcal{C} \models \varphi[x(i/b)]$, where $x(i/b)$ denotes the assignment that agrees with $x$ except at $i$, where it takes value $b$. By the induction hypothesis applied to $\mathcal{C}$ and $\varphi$, we obtain $\bigcup K \models \varphi[x(i/b)]$. Since $b$ was arbitrary, $\bigcup K \models \forall v_i \varphi[x]$.

Conversely, suppose $\bigcup K \models \forall v_i \varphi[x]$. Let $b \in A$ be arbitrary. Since $b \in \bigcup K$, we have $\bigcup K \models \varphi[x(i/b)]$. By the induction hypothesis applied to $\mathcal{A}$ and $\varphi$, we obtain $\mathcal{A} \models \varphi[x(i/b)]$. Since $b$ was arbitrary, $\mathcal{A} \models \forall v_i \varphi[x]$.

Thus the equivalence holds for all formulas, and in particular $\mathcal{A} \preceq \bigcup K$ for each $\mathcal{A} \in K$. $\square$
