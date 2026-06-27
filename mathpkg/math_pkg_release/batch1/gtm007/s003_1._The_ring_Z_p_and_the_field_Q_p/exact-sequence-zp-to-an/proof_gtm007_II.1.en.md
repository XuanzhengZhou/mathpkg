---
role: proof
locale: en
of_concept: exact-sequence-zp-to-an
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "1. The ring Z_p and the field Q_p"
---

*Proof.* It is clear that the kernel of $\varepsilon_n$ contains $p^n \mathbb{Z}_p$; conversely, if $x = (x_m)_{m \geq 1}$ belongs to $\ker(\varepsilon_n)$, one has $x_m \equiv 0 \pmod{p^n}$ for all $m \geq n$, which means that there exists a well-defined element $y_{m-n}$ of $A_{m-n}$ (where $A_k = \mathbb{Z}/p^k\mathbb{Z}$) such that its image under the isomorphism
$$A_{m-n} \xrightarrow{\sim} p^n \mathbb{Z}/p^m \mathbb{Z} \subset A_m$$
satisfies $x_m = p^n y_{m-n}$. The elements $y_i$ define an element $y$ of $\mathbb{Z}_p = \varprojlim A_i$, and one checks immediately that $p^n y = x$, which proves that $\ker(\varepsilon_n) = p^n \mathbb{Z}_p$. Hence the sequence is exact. $\square$
