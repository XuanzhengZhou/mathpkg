---
role: proof
locale: en
of_concept: cghaus-coreflective-in-haus
source_book: gtm005
source_chapter: "VII"
source_section: "8. Compactly Generated Spaces"
---

To each Hausdorff space $Y$, construct $KY$ with the same underlying set by declaring $A \subset Y$ closed in $KY$ if and only if $A \cap C$ is closed in $Y$ for all compact sets $C \subset Y$. All closed sets of $Y$ remain closed in $KY$, so $\varepsilon_Y: KY \to Y$ is continuous and $KY$ is Hausdorff.

For any continuous $f: X \to Y$ with $X \in \mathbf{CGHaus}$, define $f': X \to KY$ as the same set-function. For any closed $A \subset KY$ and compact $C \subset X$, the image $f(C)$ is compact in $Y$ (continuous image of compact is compact). Since $f^{-1}(A) \cap C = f|_C^{-1}(A \cap f(C))$ and $f|_C$ is continuous, $f^{-1}(A) \cap C$ is closed in $C$, hence closed in $X$. Because $X$ is compactly generated, $f^{-1}(A)$ is closed in $X$, so $f'$ is continuous. Thus $f = \varepsilon_Y \circ f'$ with $f'$ the unique such factorization (since $\varepsilon_Y$ is the identity on underlying sets). This exhibits $\varepsilon$ as universal from $K$ to $Y$, making $K$ right adjoint to the inclusion.
