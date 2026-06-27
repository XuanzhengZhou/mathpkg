---
role: proof
locale: en
of_concept: change-of-bound-variables
source_book: gtm037
source_chapter: "10"
source_section: "Elements of Logic"
---

We proceed by induction on the number $m$ of bound occurrences of $\alpha$ in $\varphi$. If $m = 0$, the desired conclusion is trivial.

We now assume that $m > 0$, and that our result is known for all formulas with fewer than $m$ bound occurrences of $\alpha$. By Lemma 10.58, let $\forall \alpha \psi$ be a formula occurring in $\varphi$ such that $\alpha$ does not occur bound in $\psi$. Let $\gamma$ be a variable not occurring in $\varphi$ (hence not in $\psi$) with $\gamma \neq \alpha, \beta$. Then by 10.55 we have

(1) $\vdash \forall \alpha \psi \leftrightarrow \forall \gamma \text{ Subf}_{\gamma}^{\alpha} \psi$.

Now let $\chi$ be obtained from $\varphi$ by replacing an occurrence of $\forall \alpha \psi$ in $\varphi$ by $\forall \gamma \text{ Subf}_{\gamma}^{\alpha} \psi$. Then by (1) and 10.54 we have

(2) $\vdash \varphi \leftrightarrow \chi$.

Now $\beta$ does not occur in $\chi$, and $\chi$ has fewer than $m$ bound occurrences of $\alpha$. Hence by the induction assumption,

(3) $\vdash \chi \leftrightarrow \text{Subb}_{\beta}^{\alpha} \chi$.

Now clearly $\text{Subb}_{\beta}^{\alpha} \varphi$ can be obtained from $\text{Subb}_{\beta}^{\alpha} \chi$ by replacing an occurrence of $\forall \gamma \text{ Subf}_{\gamma}^{\alpha} \psi$ in $\text{Subb}_{\beta}^{\alpha} \chi$ by $\forall \beta \text{ Subf}_{\beta}^{\alpha} \psi$. Since $\gamma$ does not occur in $\psi$ and $\beta$ does not, by 10.55 we have

$$\vdash \forall \gamma \text{ Subf}_{\gamma}^{\alpha} \psi \leftrightarrow \forall \beta \text{ Subf}_{\beta}^{\alpha} \psi.$$

Hence by 10.54,

(4) $\vdash \text{Subb}_{\beta}^{\alpha} \chi \leftrightarrow \text{Subb}_{\beta}^{\alpha} \varphi$.

By (2), (3), and (4) we obtain $\vdash \varphi \leftrightarrow \text{Subb}_{\beta}^{\alpha} \varphi$.
