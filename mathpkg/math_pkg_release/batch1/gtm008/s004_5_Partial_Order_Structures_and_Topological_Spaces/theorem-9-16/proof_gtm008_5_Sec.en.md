---
role: proof
locale: en
of_concept: theorem-9-16
source_book: gtm008
source_chapter: "5"
source_section: "5 For each formula"
---
If

$F(\alpha) \triangleq \mu_{\gamma} \left[ \gamma \geq \alpha \land (\forall a_1, \ldots, a_n \in M_{\alpha}) \left[ \llbracket (\exists y) \varphi(a_1, \ldots, a_n, y) \rrbracket = \

Then

$$[x \in b] = \sum_{x' \in M_{\alpha}} [x = x'] [x' \in b]$$

$$= \sum_{x' \in M_{\alpha}} [x = x'] [x' \in a] [\varphi(x', a_1, \ldots, a_n)]_{M_{\alpha}}.$$

$$= \sum_{x' \in M_{\alpha}} [x = x'] [x' \in a] [\varphi(x', a_1, \ldots, a_n)]$$

$$\leq \sum_{x' \in M_{\alpha}} [x = x'] [x \in a] [\varphi(x, a_1, \ldots, a_n)]$$

$$\leq \sum_{x' \in M_{\alpha}} [x \in a] [\varphi(x, a_1, \ldots, a_n)]$$

$$= [x \in a] [\varphi(x, a_1, \ldots, a_n)]$$

$$= \sum_{x' \in M_{\alpha}} [x = x'] [x' \in a] [\varphi(x, a_1, \ldots, a_n)]$$

$$\leq \sum_{x' \in M_{\alpha}} [x = x'] [x' \in a] [\varphi(x', a_1, \ldots, a_n)].$$

Then $$[x \in b] = [x \in a] [\varphi(x, a_1, \ldots, a_n)].$$.

Remark. The problem in the proof of the Axiom of Powers is to find a kind of bound for all $b$ such that $b \subseteq a$.
