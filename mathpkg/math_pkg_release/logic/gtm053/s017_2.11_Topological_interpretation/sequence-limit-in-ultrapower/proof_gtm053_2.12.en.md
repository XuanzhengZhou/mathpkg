---
role: proof
locale: en
of_concept: sequence-limit-in-ultrapower
source_book: gtm053
source_chapter: "2"
source_section: "2.12"
---

Let $\{a_i : i \in I\}$ be an arbitrary sequence of elements of $\mathbf{A}$. Define the element $\mathbf{a} \in \mathbf{A}^I / U$ to be the equivalence class of this sequence:
$$\mathbf{a} = [(a_i)_{i \in I}]_U.$$

For any $L$-formula $\varphi(x)$ with parameters from the diagonal copy of $\mathbf{A}$, we have by Łoś's theorem:
$$\mathbf{A}^I / U \vDash \varphi(\mathbf{a}) \iff \{i \in I : \mathbf{A} \vDash \varphi(a_i)\} \in U.$$

This means that $\mathbf{a}$ satisfies a property $\varphi$ in the ultrapower exactly when $U$-almost all $a_i$ satisfy $\varphi$ in $\mathbf{A}$. In the topological interpretation of the Stone space, this is precisely the condition that the sequence $(a_i)$ converges to $\mathbf{a}$ along the ultrafilter $U$.

Thus, every sequence of elements of $\mathbf{A}$ acquires a canonical "limit" in $\mathbf{A}^I / U$ given by its own equivalence class modulo $U$. This limit-like behavior is a distinguishing feature of ultrapowers and underlies their use in constructing saturated and countably saturated models.
