---
role: proof
locale: en
of_concept: product-lcs-as-projective-limit
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

For each finite subset $\mathbf{H} \subset \mathbf{A}$, the finite product $E_{\mathbf{H}} = \prod_{\alpha \in \mathbf{H}} E_\alpha$ is a locally convex space. The family $\mathcal{H}$ of all non-empty finite subsets of $\mathbf{A}$ is directed by inclusion: for any $\mathbf{H}_1, \mathbf{H}_2 \in \mathcal{H}$, their union $\mathbf{H}_1 \cup \mathbf{H}_2$ is also finite and contains both.

When $\mathbf{H} \subset \Lambda$, there is a natural projection map $g_{\mathbf{H}, \Lambda}: E_\Lambda \to E_{\mathbf{H}}$ that restricts a tuple indexed by $\Lambda$ to its coordinates in $\mathbf{H}$. These maps are continuous linear maps and satisfy the compatibility condition $g_{\mathbf{H}, \mathbf{K}} = g_{\mathbf{H}, \Lambda} \circ g_{\Lambda, \mathbf{K}}$ for $\mathbf{H} \subset \Lambda \subset \mathbf{K}$.

The projective limit of this system consists of all coherent families $(x_{\mathbf{H}})_{\mathbf{H} \in \mathcal{H}}$ with $x_{\mathbf{H}} \in E_{\mathbf{H}}$ such that $g_{\mathbf{H}, \Lambda}(x_\Lambda) = x_{\mathbf{H}}$ whenever $\mathbf{H} \subset \Lambda$. Such a family is uniquely determined by a single element $x \in \prod_{\alpha \in \mathbf{A}} E_\alpha$ by restricting to finite subsets. Conversely, any such $x$ yields a coherent family. This establishes the algebraic isomorphism, and the topology of the projective limit coincides with the product topology by the universal property.
