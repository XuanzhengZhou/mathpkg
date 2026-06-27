---
role: proof
locale: en
of_concept: lemma-10-12
source_book: gtm055
source_chapter: "10"
source_section: "Section 11_Section_11"
---

Proof. Let $f$ and $g$ be arbitrary continuous functions on $X$ such that $0 \leq f \leq \chi_U$ and $0 \leq g \leq \chi_V$, and set

$$h = (f + g) \wedge 1 \quad \text{and} \quad k = f + g - h.$$

Then it is easy to verify that $0 \leq h \leq \chi_U \cup V$ and $0 \leq k \leq \chi_U \cap V$. Since $f + g = h + k$, we have

$$\varphi_0(f) + \varphi_0(g) = \varphi_0(h) + \varphi_0(k) \leq \rho(U \cup V) + \rho(U \cap V).$$

and the lemma follows. $\square$
