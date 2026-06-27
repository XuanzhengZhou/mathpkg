---
role: proof
locale: en
of_concept: universal-existential-substructure
source_book: gtm037
source_chapter: "21"
source_section: "4"
---

The proof follows directly from the definitions of universal and existential formulas and the satisfaction relation. 

For (i): If $\varphi$ is universal, then $\varphi = \forall v_{i_0} \cdots \forall v_{i_{k-1}} \psi$ where $\psi$ is quantifier-free. If $\mathfrak{B} \models \varphi[x]$, then for every $y \in {}^\omega B$ with $y_j = x_j$ for $j \notin \{i_0, \ldots, i_{k-1}\}$, we have $\mathfrak{B} \models \psi[y]$. Since $\mathfrak{A} \subseteq \mathfrak{B}$, every such $y$ with values in $A$ is also an assignment into $B$, so $\mathfrak{A} \models \psi[y]$ for all such $y$ (quantifier-free formulas are absolute between a structure and its substructures). Hence $\mathfrak{A} \models \varphi[x]$.

For (ii): If $\varphi$ is existential, then $\varphi = \exists v_{i_0} \cdots \exists v_{i_{k-1}} \psi$ with $\psi$ quantifier-free. If $\mathfrak{A} \models \varphi[x]$, there exist $a_0, \ldots, a_{k-1} \in A$ such that taking $y$ with $y_{i_j} = a_j$ and $y_j = x_j$ otherwise gives $\mathfrak{A} \models \psi[y]$. Since $\mathfrak{A} \subseteq \mathfrak{B}$, the same assignment witnesses $\mathfrak{B} \models \psi[y]$, hence $\mathfrak{B} \models \varphi[x]$.
