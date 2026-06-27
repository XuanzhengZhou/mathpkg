---
role: proof
locale: en
of_concept: puppe-sequence-exactness-for-s-maps
source_book: gtm020
source_chapter: "16"
source_section: "2"
---

The first cofiber sequence $\{X, Z\} \leftarrow \{Y, Z\} \leftarrow \{C_f, Z\} \leftarrow \{SX, Z\} \leftarrow \{SY, Z\}$ is obtained as the direct limit of the usual Puppe exact sequences

$$[S^k X, Z] \leftarrow [S^k Y, Z] \leftarrow [S^k C_f, Z] \leftarrow [S^{k+1} X, Z] \leftarrow [S^{k+1} Y, Z]$$

as $k \to \infty$. Since exactness is preserved under direct limits of abelian groups, the limit sequence is exact.

For the second sequence, the exactness of $\{Z, X\} \to \{Z, Y\} \to \{Z, C_f\}$ follows from Proposition (2.4) applied to the Puppe cofibration sequence. The full sequence $\{Z, X\} \to \{Z, Y\} \to \{Z, C_f\} \to \{Z, SX\} \to \{Z, SY\}$ is then obtained by iteration: replacing $f$ with $\alpha_f: Y \to C_f$ gives exactness at $\{Z, C_f\}$, and continuing yields the long exact sequence.