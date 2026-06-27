---
role: proof
locale: en
of_concept: universal-specification
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

Let $\beta$ be a variable not occurring in $\varphi$ or in $\sigma$, and distinct from $\alpha$. Then

$$\vdash \forall \alpha \varphi \rightarrow \text{Subf}_{\beta}^{\alpha} \varphi \quad \text{(by 10.60)}$$

(1) $\vdash \forall \beta \forall \alpha \varphi \rightarrow \forall \beta \text{Subf}_{\beta}^{\alpha} \varphi$ (using 10.23(2))

For the other direction, let $\beta$ be a variable not occurring in $\varphi$. Then by change of bound variable,

(2) $\vdash \varphi \leftrightarrow \text{Subb}_{\beta}^{\alpha} \varphi$.

Hence using 10.23(2) we obtain

(3) $\vdash \forall \alpha \text{Subb}_{\beta}^{\alpha} \varphi \rightarrow \forall \alpha \varphi$,

and by 10.23(3) we obtain

(4) $\vdash \text{Subb}_{\beta}^{\alpha} \varphi \rightarrow \forall \alpha \text{Subb}_{\beta}^{\alpha} \varphi$.

From (1)–(4) the desired conclusion easily follows. $\square$
