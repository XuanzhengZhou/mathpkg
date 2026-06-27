---
role: proof
locale: en
of_concept: lemma-13-1
source_book: gtm055
source_chapter: "12-13"
source_section: "Section 14_Section_14"
---

Proof. For each $x$ in $\mathcal{E}$ the mapping $\lambda \rightarrow \lambda x$ is continuous on $\mathbb{C}$. Hence $x/n \in \mathcal{E}_{\varepsilon/2}$ for all sufficiently large positive integers $n$, and it follows that the sequence of sets $\{n\mathcal{E}_{\varepsilon/2}\}_{n=1}^{\infty}$ covers $\mathcal{E}$. Since $\mathcal{R}(T) = \mathcal{F}$ the images $T(n\mathcal{E}_{\varepsilon/2}) = nT(\mathcal{E}_{\varepsilon/2})$ cover $\mathcal{F}$. Since $\mathcal{F}$ is complete, it follows by the Baire category theorem (Th. 4.8) that

In particular, $w_0$ itself belongs to $(T(\mathcal{E}_{\varepsilon/2}))^-$. Moreover, a moment’s reflection shows that by reducing $\delta$ and perturbing $w_0$ slightly we may arrange things so that $w_0$ lies in the image $T(\mathcal{E}_{\varepsilon/2})$, and we assume this done.

Now let $D$ denote the set of all differences of pairs of vectors belonging to $T(\mathcal{E}_{\varepsilon/2})$:

$$D = \{Tx' - Tx'' : |x'|, |x''| \leq \varepsilon/2\}.$$

Clearly $D^-$ contains the closure $(T(\mathcal{E}_{\varepsilon/2}) - w_0)^-$ of $T(\mathcal{E}_{\varepsilon/2}) - w_0$. But translations are homeomorphisms on $\mathcal{E}$, so $(T(\mathcal{E}_{\varepsilon/2}) - w_0)^- = (T(\mathcal{E}_{\varepsilon/2}))^- - w_0$, and therefore

$$D^- \supset (T(\mathcal{E}_{\varepsilon/2}))^- - w_0 \supset \mathcal{F}_{\delta}.$$

Finally, since $Tx' - Tx'' = T(x' - x'')$, we have $D \subset T(\mathcal{E}_{\varepsilon})$, and therefore

$$\mathcal{F}_{\delta} \subset (T(\mathcal{E}_{\varepsilon}))^-.$$
