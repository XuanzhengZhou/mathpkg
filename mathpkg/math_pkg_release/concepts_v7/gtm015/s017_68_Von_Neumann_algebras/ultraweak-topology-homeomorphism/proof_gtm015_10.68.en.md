---
role: proof
locale: en
of_concept: ultraweak-topology-homeomorphism
source_book: gtm015
source_chapter: "10"
source_section: "68"
---

# Proof of Ultraweak topology as relative weak operator topology

Proof. In the notation of (68.10), the formula (*) in (68.14) may be written $f(T) = \omega_{x,y}(\tilde{T})$. Since the relative topology on $\mathcal{L}(H)^{\sim}$ induced by the weak operator topology of $\mathcal{L}(K)$ may be described as the initial topology for the set of all such linear forms $\tilde{T} \mapsto \omega_{x,y}(\tilde{T})$, we have at once: the ultraweak topology on $\mathcal{L}(H)$ is the topology that makes the bijection $T \mapsto \tilde{T}$ of $\mathcal{L}(H)$ onto $(\mathcal{L}(H)^{\sim}, \tau)$ a homeomorphism, where $\tau$ is the relative topology on $\mathcal{L}(H)^{\sim}$ induced by the weak operator topology of $\mathcal{L}(K)$.

This follows directly from the definitions: the ultraweak topology is by definition the initial topology for the linear forms $f(T) = \sum_i (T x_i | y_i) = \omega_{x,y}(\tilde{T})$, which is precisely the pullback via $T \mapsto \tilde{T}$ of the weak operator topology on $\mathcal{L}(K)$.
