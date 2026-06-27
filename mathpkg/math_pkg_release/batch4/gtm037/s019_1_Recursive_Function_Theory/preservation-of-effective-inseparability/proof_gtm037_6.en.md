---
role: proof
locale: en
of_concept: preservation-of-effective-inseparability
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

Let $h$ be a function given by Definition 6.21(iii) because $A$ and $B$ are effectively inseparable. For any $e, x \in \omega$, let

$$g(x, e) \simeq arphi_e^1(f(x)).$$

Thus $g$ is partial recursive; say $g = arphi_v^2$. By the $s$-$m$-$n$ theorem, there is a recursive function $k$ such that $arphi_{k(e)}^1(x) \simeq g(x, e) \simeq arphi_e^1(f(x))$ for all $e, x \in \omega$. Hence $\mathrm{Dmn}\,arphi_{k(e)}^1 = f^{-1}[\mathrm{Dmn}\,arphi_e^1]$.

Now define $f'(e, r) = h(k(e), k(r))$. To verify that $f'$ witnesses effective inseparability of $C$ and $D$, suppose $C \subseteq \mathrm{Dmn}\,arphi_e^1$, $D \subseteq \mathrm{Dmn}\,arphi_r^1$, and $\mathrm{Dmn}\,arphi_e^1 \cap \mathrm{Dmn}\,arphi_r^1 = \emptyset$. Then $A \subseteq f^{-1}[C] \subseteq f^{-1}[\mathrm{Dmn}\,arphi_e^1] = \mathrm{Dmn}\,arphi_{k(e)}^1$ and similarly $B \subseteq \mathrm{Dmn}\,arphi_{k(r)}^1$. Also $\mathrm{Dmn}\,arphi_{k(e)}^1 \cap \mathrm{Dmn}\,arphi_{k(r)}^1 = f^{-1}[\mathrm{Dmn}\,arphi_e^1 \cap \mathrm{Dmn}\,arphi_r^1] = \emptyset$. By effective inseparability of $A$ and $B$, $h(k(e), k(r)) \in \omega \sim (\mathrm{Dmn}\,arphi_{k(e)}^1 \cup \mathrm{Dmn}\,arphi_{k(r)}^1)$. It follows that $f'(e, r) 
otin \mathrm{Dmn}\,arphi_e^1 \cup \mathrm{Dmn}\,arphi_r^1$, establishing effective inseparability of $C$ and $D$.
