---
role: proof
locale: en
of_concept: time-independence-of-force
source_book: gtm060
source_chapter: "1"
source_section: "2"
---
Suppose $\mathbf{x} = \varphi(t)$ satisfies $\ddot{\mathbf{x}} = \mathbf{F}(\mathbf{x}, \dot{\mathbf{x}}, t)$. Under a time translation $t \mapsto t + s$, the transformed motion is $\tilde{\varphi}(t) = \varphi(t + s)$. Then $\dot{\tilde{\varphi}}(t) = \dot{\varphi}(t + s)$ and $\ddot{\tilde{\varphi}}(t) = \ddot{\varphi}(t + s)$. For this to also satisfy the same equation of motion, we must have:

$$\ddot{\varphi}(t + s) = \mathbf{F}(\varphi(t + s), \dot{\varphi}(t + s), t).$$

But the original equation evaluated at $t + s$ gives:

$$\ddot{\varphi}(t + s) = \mathbf{F}(\varphi(t + s), \dot{\varphi}(t + s), t + s).$$

Comparing these, we obtain $\mathbf{F}(\mathbf{x}, \dot{\mathbf{x}}, t) = \mathbf{F}(\mathbf{x}, \dot{\mathbf{x}}, t + s)$ for all $s$, which means $\mathbf{F}$ is independent of $t$. Therefore $\mathbf{F}(\mathbf{x}, \dot{\mathbf{x}}, t) = \boldsymbol{\Phi}(\mathbf{x}, \dot{\mathbf{x}})$.
