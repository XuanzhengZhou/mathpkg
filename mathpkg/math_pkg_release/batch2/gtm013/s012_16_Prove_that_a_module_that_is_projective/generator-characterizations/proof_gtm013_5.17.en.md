---
role: proof
locale: en
of_concept: generator-characterizations
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** (a) $\Leftrightarrow$ (b). This follows at once from (8.11.1).

(a) $\Rightarrow$ (d). Let ${}_R G$ be a generator. Suppose

$${}_R M' \\xrightarrow{f} {}_R M \\xrightarrow{g} {}_R M''$$

is a sequence in ${}_R\\mathbf{M}$ such that

$$\\operatorname{Hom}_R(G, M') \\xrightarrow{f_*} \\operatorname{Hom}_R(G, M) \\xrightarrow{g_*} \\operatorname{Hom}_R(G, M'')$$

is exact. Then $0 = g_* f_* = \\operatorname{Hom}(G, gf)$. Thus, since (a) $\Leftrightarrow$ (b), we have $gf = 0$, i.e., $\\operatorname{Im} f \\leq \\operatorname{Ker} g$. Let $x \\in \\operatorname{Ker} g$. Then, since $G$ generates $\\operatorname{Ker} g$, there exist homomorphisms $\\beta_i: G \\to \\operatorname{Ker} g \\leq M$ and $y_i \\in G$ such that

$$x = \\sum_{i=1}^{n} \\beta_i(y_i).$$

Then, for each $i$, $g\\beta_i = 0$, so $\\beta_i \\in \\operatorname{Ker} g_* = \\operatorname{Im} f_*$. That is, for each $i$ there is an $\\alpha_i \\in \\operatorname{Hom}(G, M')$ with $\\beta_i = f_*(\\alpha_i) = f\\alpha_i$. Therefore,

$$x = \\sum_{i=1}^{n} f\\alpha_i(y_i) = f\\left(\\sum_{i=1}^{n} \\alpha_i(y_i)\\right) \\in \\operatorname{Im} f.$$
