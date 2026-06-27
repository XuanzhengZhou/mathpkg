---
role: proof
locale: en
of_concept: beths-definability-theorem
source_book: gtm037
source_chapter: "22"
source_section: "4"
---

First treat the case where $\pi$ is a relation symbol of rank $m$. Expand $\mathcal{L}$ to $\mathcal{L}^*$ with new constant symbols $c_0, \ldots, c_{m-1}$ and a new relation symbol $S$ of rank $m$. Let $\Theta$ be the set of all sentences $\mathbf{S} c_0 \cdots c_{m-1}$.

Let $\Gamma^*$ be the theory in $\mathcal{L}^*$ obtained from $\Gamma$ by replacing every occurrence of $\pi$ by $S$. Now by condition (i), we have:

$$\Gamma \cup \Gamma^* \models \pi c_0 \cdots c_{m-1} \leftrightarrow \mathbf{S} c_0 \cdots c_{m-1}.$$

By compactness, there is a finite conjunction $\gamma$ of sentences of $\Gamma$ and $\theta$ of sentences of $\Theta$ such that

$$\models \gamma \wedge \pi c_0 \cdots c_{m-1} \rightarrow (\theta \rightarrow \mathbf{S} c_0 \cdots c_{m-1}).$$

By the Interpolation Theorem, there exists a sentence $\xi$ in the common language (which contains all nonlogical constants except $\pi$ and $S$, plus $c_0, \ldots, c_{m-1}$) such that

$$\models \gamma \wedge \pi c_0 \cdots c_{m-1} \rightarrow \xi \quad \text{and} \quad \models \xi \rightarrow (\theta \rightarrow \mathbf{S} c_0 \cdots c_{m-1}).$$

From this it follows that $\Gamma \models \pi c_0 \cdots c_{m-1} \leftrightarrow \xi$, and hence

$$\Gamma \models \forall v_0 \cdots \forall v_{m-1} (\pi v_0 \cdots v_{m-1} \leftrightarrow \xi'),$$

where $\xi'$ is obtained from $\xi$ by replacing $c_0, \ldots, c_{m-1}$ by $v_0, \ldots, v_{m-1}$. The theory $\Delta = \{\theta \in \text{Sent}_{\mathcal{L}'} : \Gamma \models \theta\}$ together with this explicit definition axiom axiomatizes $\Gamma$, establishing the result.

The case where $\pi$ is a function symbol or constant symbol is handled similarly by first replacing it with a relation symbol representing its graph.
