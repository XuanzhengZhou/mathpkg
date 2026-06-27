---
role: proof
locale: en
of_concept: noethers-theorem
source_book: gtm060
source_chapter: "4"
source_section: "20"
---

Let $\Phi: \mathbb{R} \times \mathbb{R} \to M$ be a family of motions parameterized by the group parameter $s$, defined by $\Phi(s, t) = h^s(\gamma(t))$ where $\gamma(t)$ is a solution of the Lagrange equations. In local coordinates $\mathbf{q}$, let $q' = \frac{d}{ds}\big|_{s=0} h^s(q)$ denote the infinitesimal generator of the symmetry.

Since the system admits $h^s$, we have $L(\Phi(s, t), \dot{\Phi}(s, t)) = L(\Phi(0, t), \dot{\Phi}(0, t))$ for all $s$. Differentiating with respect to $s$ at $s = 0$ yields

$$0 = \frac{\partial L}{\partial q} q' + \frac{\partial L}{\partial \dot{q}} \dot{q}', \tag{1}$$

where the partial derivatives of $L$ are evaluated at $q = \Phi(s, t)$, $\dot{q} = \dot{\Phi}(s, t)$.

For each fixed $s$, the mapping $t \mapsto \Phi(s, t)$ satisfies Lagrange's equation:

$$\frac{\partial}{\partial t} \left[ \frac{\partial L}{\partial \dot{q}} (\Phi(s, t), \dot{\Phi}(s, t)) \right] = \frac{\partial L}{\partial q} (\Phi(s, t), \dot{\Phi}(s, t)).$$

Introduce the notation $F(s, t) = \frac{\partial L}{\partial \dot{q}}(\Phi(s, t), \dot{\Phi}(s, t))$ and substitute $\frac{\partial F}{\partial t}$ for $\frac{\partial L}{\partial q}$ in (1):

$$0 = \frac{\partial F}{\partial t} q' + \frac{\partial L}{\partial \dot{q}} \dot{q}'.$$

Writing $\dot{q}' = \frac{dq'}{dt}$, we obtain

$$0 = \left( \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) q' + \frac{\partial L}{\partial \dot{q}} \left( \frac{d}{dt} q' \right) = \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} q' \right) = \frac{dI}{dt}.$$

Thus $I = \frac{\partial L}{\partial \dot{q}} q'$ is a first integral of the motion.

Invariantly, $I$ is the rate of change of $L(v)$ when the vector $v \in TM_x$ varies inside $TM_x$ with velocity $\frac{d}{ds}\big|_{s=0} h^s x$. Hence $I(v)$ is well defined as a function on $TM$, independent of the choice of local coordinates. The same proof carries over when $M$ is a manifold.
