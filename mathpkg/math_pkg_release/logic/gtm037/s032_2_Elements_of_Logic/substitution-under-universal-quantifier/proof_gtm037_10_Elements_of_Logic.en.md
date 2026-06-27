---
role: proof
locale: en
of_concept: substitution-under-universal-quantifier
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

$$\vdash \alpha = \sigma \rightarrow (\varphi \rightarrow \text{Subf}_{\sigma}^{\alpha}\varphi) \quad 10.49$$
$$\vdash \varphi \rightarrow (\neg \text{Subf}_{\sigma}^{\alpha}\varphi \rightarrow \neg \alpha = \sigma) \quad \text{suitable tautology}$$
$$\vdash \forall \alpha\varphi \rightarrow (\forall \alpha \neg \text{Subf}_{\sigma}^{\alpha}\varphi \rightarrow \forall \alpha \neg \alpha = \sigma) \quad \text{using 10.23(2)}$$
$$\vdash \neg \forall \alpha \neg \alpha = \sigma \quad 10.23(4)$$
$$\vdash \forall \alpha\varphi \rightarrow \neg \forall \alpha \neg \text{Subf}_{\sigma}^{\alpha}\varphi$$
$$\vdash \neg \text{Subf}_{\sigma}^{\alpha}\varphi \rightarrow \forall \alpha \neg \text{Subf}_{\sigma}^{\alpha}\varphi \quad 10.23(3)$$
$$\vdash \forall \alpha\varphi \rightarrow \text{Subf}_{\sigma}^{\alpha}\varphi \quad \text{suitable tautology}$$
