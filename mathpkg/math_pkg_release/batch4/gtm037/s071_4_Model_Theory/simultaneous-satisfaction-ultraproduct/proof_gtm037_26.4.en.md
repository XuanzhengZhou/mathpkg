---
role: proof
locale: en
of_concept: simultaneous-satisfaction-ultraproduct
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Let $A = \{c_\gamma : \gamma < \rho\}$, where $\rho < n^{\partial}$. For each $\nu < \mu$, let
\[
B_\nu = \{\delta < n : \mathfrak{A} \models (\exists v_0 \varphi_\nu) [\langle a_{v_j \delta} : j < \omega \rangle]\}.
\]
By condition (ii), $B_\nu \in D$ for all $\nu < \mu$.

For each $\nu < \mu$, choose $g_\nu : n \to \rho$ such that for every $\delta \in B_\nu$,
\[
\mathfrak{A} \models \varphi_\nu [\langle a_{v_j \delta} : j < \omega \rangle_{c_{g_\nu \delta}}^{v_0}].
\]
Let $G = \{g_\nu : \nu < \mu\}$. Since $|F| > m$, by Lemma 26.38 (or 26.37) choose a nonempty $F_1 \subseteq F$ with $|F_1| \leq m$ such that $(F \setminus F_1, G, D)$ is $m$-consistent over $n$.

Fix $f \in F \setminus F_1$. Let $F' = (F \setminus F_1) \setminus \{f\}$. For each $\delta < n$, define
\[
b_\delta = c_{f\delta} \quad \text{if } f\delta < \rho,
\]
\[
b_\delta = c_0 \quad \text{otherwise}.
\]

For each $\nu < \mu$, let
\[
C_\nu = \{\delta < n : \mathfrak{A} \models \varphi_\nu [\langle a_{v_j \delta} : j < \omega \rangle_{b_\delta}^{v_0}]\}.
\]
By the $m$-consistency of $(F \setminus F_1, G, D)$, one shows that $C_\nu \in D$ for all $\nu < \mu$, completing the proof. The key point is that condition (i) (closure under conjunction) together with the $m$-consistency condition ensures that the chosen witnesses work simultaneously.
