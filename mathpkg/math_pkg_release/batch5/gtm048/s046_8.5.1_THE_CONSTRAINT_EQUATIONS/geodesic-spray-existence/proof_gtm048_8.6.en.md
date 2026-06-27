---
role: proof
locale: en
of_concept: geodesic-spray-existence
source_book: gtm048
source_chapter: "8"
source_section: "8.6.1"
---

Let $G$ be the unique vector field on $TM$ characterized by the condition that for every $v \in TM$, the integral curve of $G$ through $v$ is $t \mapsto \dot{\gamma}_v(t)$, where $\gamma_v$ is the unique geodesic with initial velocity $v$. Explicitly, $G(v) = \frac{d}{dt}\big|_{t=0} \dot{\gamma}_v(t)$. By the geodesic equation $D_{\dot{\gamma}} \dot{\gamma} = 0$, we have $(\Pi^* D)_G I = 0$, so $G$ is horizontal. Moreover, $\Pi_* G(v) = \Pi_* \frac{d}{dt}|_{t=0} \dot{\gamma}_v(t) = \frac{d}{dt}|_{t=0} \gamma_v(t) = v = I(v)$, hence $\Pi_* G = I$. Uniqueness follows from the uniqueness of geodesics given initial conditions.
