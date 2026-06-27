---
role: proof
locale: en
of_concept: tautology-equivalent-conditions
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

(i) $\Rightarrow$ (ii). Assume that $\varphi$ is a tautology, and let $f$ satisfy the hypothesis of (ii). By recursion on formulas we define a function $h$: $\operatorname{Fmla} \to 2$ as follows:

$$h(\psi) = f(\psi) \quad \text{if } \psi \text{ is an atomic formula} \in S,$$
$$h(\psi) = 0 \quad \text{if } \psi \text{ is an atomic formula} \notin S,$$
$$h(\neg \psi) = 1 - h(\psi) \quad \text{for any formula } \psi,$$
$$h(\psi \vee \chi) = 1 \quad \text{if } h(\psi) = 1 \text{ or } h(\chi) = 1,$$
$$h(\psi \vee \chi) = 0 \quad \text{if } h(\psi) = h(\chi) = 0,$$
$$h(\psi \wedge \chi) = 1 \quad \text{if } h(\psi) = 1 \text{ and } h(\chi) = 1,$$
$$h(\psi \wedge \chi) = 0 \quad \text{otherwise}.$$

The function $h$ is well-defined by the recursion theorem for formulas (Proposition 10.18). One then verifies by induction on formulas that $h$ agrees with $f$ on all subformulas in $S$. Since $\varphi$ is a tautology, by definition any truth valuation (in particular the one induced by $h$ on atomic formulas) makes $\varphi$ true, so $h(\varphi) = 1$, and therefore $f(\varphi) = 1$.

(ii) $\Rightarrow$ (i). If condition (ii) holds, take any truth valuation $v$ assigning truth values to the atomic subformulas of $\varphi$. By extending $v$ to $S$ via the standard truth-table rules, we obtain an $f$ satisfying (a)-(c). Condition (ii) then forces $f(\varphi) = 1$, so $v$ makes $\varphi$ true. Since $v$ was arbitrary, $\varphi$ is a tautology.
