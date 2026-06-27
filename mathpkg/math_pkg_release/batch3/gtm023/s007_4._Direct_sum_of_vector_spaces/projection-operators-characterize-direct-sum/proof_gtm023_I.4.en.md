---
role: proof
locale: en
of_concept: projection-operators-characterize-direct-sum
source_book: gtm023
source_chapter: "I"
source_section: "4. Direct sum of vector spaces"
---

**Proof.** ($\Rightarrow$) Let $x \in E$ be arbitrary. Using $\sum_i \varrho_i = \iota_E$, we have
$$x = \sum_{i=1}^{r} \varrho_i x \in \sum_{i=1}^{r} \operatorname{Im} \varrho_i,$$
so $E = \sum_{i=1}^{r} \operatorname{Im} \varrho_i$.

To prove the sum is direct, suppose
$$x \in \operatorname{Im} \varrho_i \cap \sum_{j \neq i} \operatorname{Im} \varrho_j.$$
Since $x \in \operatorname{Im} \varrho_i$, we have $x = \varrho_i y$ for some $y \in E$, and therefore
$$\varrho_i x = \varrho_i^2 y = \varrho_i y = x.$$

On the other hand, since $x \in \sum_{j \neq i} \operatorname{Im} \varrho_j$, we have $x = \sum_{j \neq i} \varrho_j y_j$ for some vectors $y_j \in E$. Then, using $\varrho_i \circ \varrho_j = 0$ for $i \neq j$,
$$\varrho_i x = \sum_{j \neq i} \varrho_i \varrho_j y_j = 0.$$

Thus $x = 0$, and the decomposition is direct: $E = \bigoplus_{i=1}^{r} \operatorname{Im} \varrho_i$.

($\Leftarrow$) Conversely, suppose $E = \bigoplus_v E_v$ with canonical projections $\pi_v: E \to E_v$ and injections $i_v: E_v \to E$. Define $\varrho_v = i_v \circ \pi_v$. Then $\varrho_v^2 = i_v \pi_v i_v \pi_v = i_v \iota_{E_v} \pi_v = i_v \pi_v = \varrho_v$, so $\varrho_v$ is a projection. For $v \neq \mu$,
$$\varrho_v \circ \varrho_\mu = i_v \pi_v i_\mu \pi_\mu = i_v \circ 0 \circ \pi_\mu = 0,$$
using $\pi_v \circ i_\mu = 0$ for $v \neq \mu$. Moreover, $\operatorname{Im} \varrho_v = E_v$, so the decomposition determined by the $\varrho_v$ coincides with the original one. $\square$
