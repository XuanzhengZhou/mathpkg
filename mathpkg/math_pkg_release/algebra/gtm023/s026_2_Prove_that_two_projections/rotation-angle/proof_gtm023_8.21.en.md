---
role: proof
locale: en
of_concept: rotation-angle
source_book: gtm023
source_chapter: "8"
source_section: "8.21"
---

Fix a non-zero vector $x$ and let $e_1 = x/|x|$. Complete to a positive orthonormal basis $e_1, e_2 = j(e_1)$. Write $\varphi e_1 = \cos \Theta \cdot e_1 + \sin \Theta \cdot e_2$ and $\varphi e_2 = -\sin \Theta \cdot e_1 + \cos \Theta \cdot e_2$ (since $\varphi$ is a proper rotation).

Computing the trace: $\operatorname{tr} \varphi = (\varphi e_1, e_1) + (\varphi e_2, e_2) = \cos \Theta + \cos \Theta = 2\cos \Theta$.

Computing $\operatorname{tr}(j \circ \varphi)$: $(j \varphi e_1, e_1) + (j \varphi e_2, e_2) = (j(\cos \Theta e_1 + \sin \Theta e_2), e_1) + (j(-\sin \Theta e_1 + \cos \Theta e_2), e_2) = \sin \Theta + \sin \Theta = 2\sin \Theta$.

Thus $\cos \Theta = \frac{1}{2}\operatorname{tr} \varphi$ and $\sin \Theta = \frac{1}{2}\operatorname{tr}(j \circ \varphi)$. The angle $\Theta$ is independent of $x$ because the trace is basis-independent.
