---
role: proof
locale: en
of_concept: enumerable-bounded-subset-benign
source_book: gtm053
source_chapter: "5"
source_section: "5.2"
---
The proof consists of a series of reduction steps.

**First reduction (5.3).** In the free group $G = |\{a_1, b_1, c_1; \ldots; a_{rn}, b_{rn}, c_{rn}\}|$, consider a set of "layered" words $R = \{a_1^{x_1} b_1 c_1^{x_1} \cdots a_{rn}^{x_{rn}} b_{rn} c_{rn}^{x_{rn}}\}$ and the subgroup $H$ it generates. Each element $g' = a_{i_1}^{x_1} \cdots a_{i_r}^{x_r} \in R'$ is encoded as an element $g \in G$ by padding with appropriate variables.

**Second reduction (5.4-5.5).** Using the Diophantine representation theorem, the enumerable set $E \subset \mathbf{Z}^{l+1}$ defining $R$ is represented as the projection of an intersection $\bigcap_{s=1}^{N} E_s$, where each $E_s$ is defined by an equation of the form $x_i = c$, $x_i = x_j$, $x_k = x_j + x_i$, or $x_k = x_j \cdot x_i$. The subgroup $H$ is benign if all $\overline{H}_s$ are benign.

**Third reduction (5.6-5.8).** A finitely presented group $K$ is constructed as a multiple HNN-extension of $\overline{G}$. The $K$ uses two HNN-extensions: first with stable letters $t_i$, second with stable letters $t_{ijk}$. Finitely generated subgroups $L_s \subset K$ are constructed such that $L_s \cap \overline{G} = \overline{H}_s$ for all $s$. The verification uses Proposition 2.7(a) to show the stable letters generate a free subgroup with trivial intersection with $\overline{G}$. This proves $\overline{H}_s$ is benign for each $s$, hence $H$ is benign.
