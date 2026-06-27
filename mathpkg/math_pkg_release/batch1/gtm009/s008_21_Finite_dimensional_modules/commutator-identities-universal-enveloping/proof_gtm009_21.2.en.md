---
role: proof
locale: en
of_concept: commutator-identities-universal-enveloping
source_book: gtm009
source_chapter: "21"
source_section: "21.2"
---

(a) $[x_j, y_i^{k+1}] = 0$ when $i \neq j$. This follows from the fact (Lemma 10.1) that $\alpha_j - \alpha_i$ is not a root when $i \neq j$. Since $x_j \in L_{\alpha_j}$ and $y_i \in L_{-\alpha_i}$, their bracket $[x_j, y_i]$ lies in $L_{\alpha_j - \alpha_i}$ (when $\alpha_j - \alpha_i$ is a root), and is zero otherwise. When $i \neq j$, $\alpha_j - \alpha_i$ is not a root, so $[x_j, y_i] = 0$. By induction, $[x_j, y_i^{k+1}] = 0$.

(b) $[h_j, y_i^{k+1}] = -(k+1)\alpha_i(h_j)y_i^{k+1}$. Use induction on $k$. The case $k = 0$ is $[h_j, y_i] = -\alpha_i(h_j)y_i$, which follows from the definition of the root space decomposition (cf. (18.1)). Assuming the formula holds for $k$, we compute:
$$[h_j, y_i^{k+1}] = [h_j, y_i]y_i^k + y_i[h_j, y_i^k] = -\alpha_i(h_j)y_i^{k+1} - k\alpha_i(h_j)y_i^{k+1} = -(k+1)\alpha_i(h_j)y_i^{k+1}.$$

(c) $[x_i, y_i^{k+1}] = -(k+1)y_i^k(k \cdot 1 - h_i)$. Again by induction on $k$. For $k = 0$: $[x_i, y_i] = h_i = -(0+1)y_i^0(0 \cdot 1 - h_i) = h_i$, which holds. For the induction step, compute:
$$[x_i, y_i^{k+1}] = [x_i, y_i]y_i^k + y_i[x_i, y_i^k] = h_i y_i^k - k y_i^{k-1}((k-1) \cdot 1 - h_i)y_i$$
$$= h_i y_i^k - k(k-1)y_i^k + k y_i^{k-1}h_i y_i.$$
Using $[h_i, y_i] = -2y_i$ (since $\alpha_i(h_i) = 2$), we have $h_i y_i = y_i h_i - 2y_i$, and iterating gives $h_i y_i^k = y_i^k h_i - 2k y_i^k$. Substituting and simplifying yields $-(k+1)y_i^k(k \cdot 1 - h_i)$, completing the induction.
