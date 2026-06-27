---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The universal natural transformation $\mu: T_0 \to T_1$ is a construction using the product category $C \times 2$ (where $2$ is the arrow category $0 \to 1$). The transformation $\mu$ maps each object $c$ to the arrow $\langle 1_c, \downarrow \rangle$ that goes from the "bottom" copy to the "top" copy. Its universal property states that any natural transformation $\tau: S \to T$ between functors $C \to D$ can be represented uniquely by a functor $F: C \times 2 \to D$ with $F \circ \mu = \tau$. This makes $C \times 2$ the "classifying object" for natural transformations.
