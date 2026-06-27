---
role: proof
locale: en
of_concept: h1-as-kernel
source_book: gtm004
source_chapter: "VI"
source_section: "4"
---

# Proof of Proposition 4.2: $H_1(G, B)$ as Kernel

By definition, $H_1(G, B) = \operatorname{Tor}_1^{\mathbb{Z}G}(B, \mathbb{Z})$. To compute this, we use the standard $\mathbb{Z}G$-free presentation of the trivial module $\mathbb{Z}$:

$$0 \longrightarrow IG \xrightarrow{\iota} \mathbb{Z}G \xrightarrow{\varepsilon} \mathbb{Z} \longrightarrow 0,$$

where $\varepsilon$ is the augmentation map and $\iota$ is the inclusion. Tensoring this short exact sequence with $B$ over $\mathbb{Z}G$ yields the exact sequence

$$0 \longrightarrow \operatorname{Tor}_1^{\mathbb{Z}G}(B, \mathbb{Z}) \longrightarrow B \otimes_{\mathbb{Z}G} IG \xrightarrow{\iota_*} B \otimes_{\mathbb{Z}G} \mathbb{Z}G \longrightarrow B \otimes_{\mathbb{Z}G} \mathbb{Z} \longrightarrow 0.$$

Using the natural isomorphism $B \otimes_{\mathbb{Z}G} \mathbb{Z}G \cong B$ (given by $b \otimes x \mapsto bx$), this sequence becomes

$$0 \longrightarrow H_1(G, B) \longrightarrow B \otimes_{\mathbb{Z}G} IG \xrightarrow{\iota_*} B \longrightarrow H_0(G, B) \longrightarrow 0,$$

where $\iota_*(b \otimes (x-1)) = b x - b$ for $b \in B$, $x \in G$.

By exactness, the kernel of $\iota_*$ is precisely the image of the first map, which is $H_1(G, B)$. Therefore

$$H_1(G, B) = \ker\big(\iota_*: B \otimes_{\mathbb{Z}G} IG \longrightarrow B\big),$$

with $\iota_*(b \otimes (x-1)) = b x - b$.

**Special case: trivial $B$.** If $B$ is a trivial $G$-module, then $bx = b$ for all $x \in G$, so $\iota_*$ is the zero map. In this case $H_1(G, B) \cong B \otimes_{\mathbb{Z}G} IG$.
