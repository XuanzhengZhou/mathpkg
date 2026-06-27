---
role: proof
locale: en
of_concept: tautology-godel-number-recursive
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

Let $R$ be the relation of Proposition 10.21, which holds between the Godel number of a subformula and the Godel number of the containing formula. Using Lemma 10.20, a formula $\varphi$ with Godel number $m$ is a tautology iff every valuation on its subformulas makes it true.

The number $n$ is used to code the set $S$ of all subformulas of $\varphi$: each subformula's Godel number appears as a component $(n)_i$ of $n$, with the convention $(n)_{\ln(n)} = m$ (the formula itself is the last member). A valuation is coded by a number $f$ where $(f)_i$ is $1$ (false) or $2$ (true) for the subformula numbered $(n)_i$, with $\ln(f) = \ln(n)$ matching the length of the subformula list.

The conditions then encode:
- $\neg'(n)_j = (n)_i$ means the subformula at position $j$ is the negation of the subformula at position $i$;
- $(n)_j \vee'(n)_k = (n)_i$ means the subformula at position $i$ is the disjunction of those at $j$ and $k$;
- $(n)_j \wedge'(n)_k = (n)_i$ similarly for conjunction.

The final implication says: if $f$ is a valuation satisfying the truth-table constraints, then $f$ assigns true ($2$) to $\varphi$ itself (position $\ln(n)$). All quantifiers are bounded by functions of $m$, making the definition recursive.
