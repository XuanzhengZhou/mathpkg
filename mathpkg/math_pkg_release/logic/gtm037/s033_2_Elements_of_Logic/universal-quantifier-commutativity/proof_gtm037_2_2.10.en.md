---
role: proof
locale: en
of_concept: universal-quantifier-commutativity
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

\begin{align*}
&\vdash \forall \alpha \forall \beta \varphi \rightarrow \varphi &&\text{(10.62, twice)}\\
&\vdash \forall \alpha \forall \alpha \forall \beta \varphi \rightarrow \forall \alpha \varphi &&\text{(10.23(2))}\\
&\vdash \forall \alpha \forall \beta \varphi \rightarrow \forall \alpha \forall \beta \varphi &&\text{(10.63)}\\
&\vdash \forall \alpha \forall \beta \varphi \rightarrow \forall \alpha \varphi\\
&\vdash \forall \alpha \forall \beta \varphi \rightarrow \forall \beta \forall \alpha \varphi &&\text{(similarly)}
\end{align*}

The desired result now follows easily by symmetry. $\square$
