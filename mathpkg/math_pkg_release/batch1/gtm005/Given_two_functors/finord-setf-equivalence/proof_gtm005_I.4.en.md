---
role: proof
locale: en
of_concept: finord-setf-equivalence
source_book: gtm005
source_chapter: "I. Categories, Functors, and Natural Transformations"
source_section: "4. Natural Transformations"
---

For each finite set $X$, choose a bijection $\theta_X: X \rightarrow \# X$, where $\# X$ is the unique finite ordinal with the same cardinality as $X$. If $X$ is itself an ordinal number, choose $\theta_X$ to be the identity. This ensures $\# \circ S = I_{\text{Finord}}$ as functors.

For any function $f: X \rightarrow Y$ between finite sets, define $\# f: \# X \rightarrow \# Y$ by $\# f = \theta_Y \circ f \circ \theta_X^{-1}$. The diagram

$$
\begin{array}{ccc}
X & \xrightarrow{\theta_X} & \# X \\
{\scriptstyle f}\downarrow & & \downarrow {\scriptstyle \# f} \\
Y & \xrightarrow{\theta_Y} & \# Y
\end{array}
$$

commutes by construction. This commutativity is precisely the statement that $\theta: I_{\text{Set}_f} \rightarrow S \circ \#$ is a natural transformation. Since each component $\theta_X$ is a bijection, $\theta$ is a natural isomorphism. Therefore $I_{\text{Finord}} = \# \circ S$ and $I_{\text{Set}_f} \cong S \circ \#$, establishing that $\text{Finord}$ and $\text{Set}_f$ are equivalent categories.
