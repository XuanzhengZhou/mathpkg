---
role: proof
locale: en
of_concept: omega-consistency-implies-distinct-numerals
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

If $n \neq p$, suppose for contradiction that $\neg(\mathbf{n} = \mathbf{p}) \notin \Gamma$. Since $\Gamma$ is a theory, by completeness of $\Gamma$ with respect to its deductive closure, we would have $\mathbf{n} = \mathbf{p} \in \Gamma$. Then for the formula $\varphi(v_0)$ defined as $v_0 = \mathbf{p}$, we would have $\varphi(\mathbf{x}) \in \Gamma$ for each $x \in \omega$ (since for all $x$, $\mathbf{x} = \mathbf{p} \in \Gamma$ would follow by transitivity of equality, using $\mathbf{n} = \mathbf{p}$ and the definition of numerals). But also $\exists v_0 \neg \varphi(v_0)$ would be in $\Gamma$ since trivially $\exists v_0 (v_0 \neq \mathbf{p})$ is provable. This contradicts $\omega$-consistency of $\Gamma$. Hence $\neg(\mathbf{n} = \mathbf{p}) \in \Gamma$.
