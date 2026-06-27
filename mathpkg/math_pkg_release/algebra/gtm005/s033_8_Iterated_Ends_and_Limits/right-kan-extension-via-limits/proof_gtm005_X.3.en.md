---
role: proof
locale: en
of_concept: right-kan-extension-via-limits
source_book: gtm005
source_chapter: "X"
source_section: "3. The Kan Extension"
---

**Proof.** For each $c \in C$, define $Rc$ as the limit of $TQ: (c \downarrow K) \to A$, with limiting cone $\lambda$. Each $g: c \to c'$ induces a functor $(g \downarrow K): (c' \downarrow K) \to (c \downarrow K)$ by $f' \mapsto f'g$, and $Rg$ is the canonical comparison map from $\lim TQ$ to $\lim TQ \circ (g \downarrow K) = \lim TQ'$. This makes $R$ a functor.

For each $n \in M$, the object $\langle 1_{Kn}, n \rangle$ lies in $(Kn \downarrow K)$, and we set $\varepsilon_n = \lambda_{1_{Kn}}: R(Kn) \to Tn$. To verify naturality of $\varepsilon$, for $h: n \to n'$ in $M$, the map $Kh: (Kn \downarrow K) \to (Kn' \downarrow K)$ sends $\langle 1_{Kn}, n \rangle$ to $\langle Kh, n' \rangle$, and the cone condition yields $\varepsilon_{n'} \circ R(Kh) = Th \circ \varepsilon_n$.

For universality, given any $S: C \to A$ and $\alpha: SK \to T$, for each $c \in C$ and each $f: c \to Km$ in $(c \downarrow K)$, the composition $\alpha_m \circ Sf: Sc \to Tm$ defines a cone from $Sc$ over $TQ$. By the universal property of the limit $Rc$, there is a unique $\sigma_c: Sc \to Rc$ such that $\lambda_f \circ \sigma_c = \alpha_m \circ Sf$ for all $f$. Naturality of $\sigma$ follows from the limit definition of $Rg$, and the construction ensures $\alpha = \varepsilon \cdot \sigma K$. Uniqueness of $\sigma$ follows because $\varepsilon \cdot \sigma K = \alpha$ determines $\sigma_{Kn}$ for all $n$, and naturality forces the rest.
