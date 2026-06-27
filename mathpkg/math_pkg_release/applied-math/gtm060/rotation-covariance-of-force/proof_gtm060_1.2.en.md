---
role: proof
locale: en
of_concept: rotation-covariance-of-force
source_book: gtm060
source_chapter: "1"
source_section: "2"
---
Let $\mathbf{x}_i = \varphi_i(t)$ be a motion satisfying $\ddot{\mathbf{x}}_i = \mathbf{F}_i(\mathbf{x}, \dot{\mathbf{x}})$. Under an orthogonal transformation $G \in O(3)$, the transformed motion is $\tilde{\varphi}_i(t) = G\varphi_i(t)$. Then $\dot{\tilde{\varphi}}_i = G\dot{\varphi}_i$ and $\ddot{\tilde{\varphi}}_i = G\ddot{\varphi}_i$. For this to satisfy the same equation, we need:

$$G\ddot{\varphi}_i = \mathbf{F}_i(G\boldsymbol{\varphi}, G\dot{\boldsymbol{\varphi}}).$$

But $\ddot{\varphi}_i = \mathbf{F}_i(\boldsymbol{\varphi}, \dot{\boldsymbol{\varphi}})$, so $G\mathbf{F}_i(\boldsymbol{\varphi}, \dot{\boldsymbol{\varphi}}) = \mathbf{F}_i(G\boldsymbol{\varphi}, G\dot{\boldsymbol{\varphi}})$, which is the stated covariance condition $\mathbf{F}(G\mathbf{x}, G\dot{\mathbf{x}}) = G\mathbf{F}(\mathbf{x}, \dot{\mathbf{x}})$.
