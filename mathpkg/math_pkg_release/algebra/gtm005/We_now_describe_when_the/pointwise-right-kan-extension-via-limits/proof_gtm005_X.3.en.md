---
role: proof
locale: en
of_concept: pointwise-right-kan-extension-via-limits
source_book: gtm005
source_chapter: "X"
source_section: "3. The Kan Extension"
---

First, $Rg$ is defined by the fact that the limit is a functor of $(c \downarrow K)$ and hence of $c$. Given $g: c \to c'$ and the projection $Q': (c' \downarrow K) \to A$, each $f': c' \to Km$ determines $f'g: c \to Km \in (c \downarrow K)$; the components $\lambda_{f'g}: Rc \to Tm$ form a cone from $Rc$, and since the cone $\lambda'$ is universal, there is a unique arrow $Rg$ making the relevant diagram commute for all $f'$. Formally, $f' \mapsto f'g$ defines the functor $(g \downarrow K): (c' \downarrow K) \to (c \downarrow K)$, so that $TQ' = TQ \circ (g \downarrow K)$, and $Rg$ is the canonical comparison between limits.

Now, to show $R$ is a right Kan extension, take any natural transformation $\alpha: SK \to T$. For each $c \in C$ and each $f: c \to Km$ in $(c \downarrow K)$, consider the arrow $\alpha_m \circ Sf: Sc \to Tm$. For each arrow $h: \langle f, m \rangle \to \langle f', m' \rangle$ of $(c \downarrow K)$ where $f' = Kh \circ f$, the square commutes because $\alpha$ is natural. This shows that the diagonal arrows $\alpha_m \circ Sf: Sc \to Tm$ form a cone from $Sc$. Hence there is a unique arrow $\sigma_c: Sc \to Rc$ factoring through the limiting cone.

To prove $\sigma$ natural for $g: c \to c'$, form a diagram with $Rg$, $\sigma_c$, $\sigma_{c'}$, $Sg$, and the components of the limiting cones. The right and outer squares commute by definition of $\sigma$, and the top by definition of $Rg$. Since the limiting cone is universal, the left square commutes, establishing naturality of $\sigma$.

Setting $c = Kn$ and $f = 1_{Kn}$ shows $\alpha_n = \lambda_{1_{Kn}} \circ \sigma_{Kn} = \varepsilon_n \circ \sigma_{Kn}$, hence $\alpha = \varepsilon \cdot \sigma K$. Uniqueness of $\sigma$ follows from the fact that the property $\alpha = \varepsilon \cdot \sigma K$ determines $\sigma_{Kn}$, and naturality plus the universal property of the limit forces the remaining components.
