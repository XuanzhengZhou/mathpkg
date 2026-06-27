---
role: proof
locale: en
of_concept: verma-module-is-standard-cyclic
source_book: gtm009
source_chapter: "20"
source_section: "20.3"
---

**Proof.** The element $1 \otimes v^+$ generates $Z(\lambda)$ as a $\mathfrak{U}(L)$-module because every element of $Z(\lambda)$ is a finite sum of terms $u \otimes v^+$ with $u \in \mathfrak{U}(L)$, and $(u \otimes v^+) = u \cdot (1 \otimes v^+)$ by the definition of the left module action.

To see that $1 \otimes v^+$ is nonzero, recall from Corollary D of Theorem 17.3 (PBW Theorem) that $\mathfrak{U}(L)$ is a free $\mathfrak{U}(B)$-module with basis consisting of $1$ together with all monomials $y_{\beta_1}^{i_1} \cdots y_{\beta_m}^{i_m}$ where $\beta_j \in \Phi^+$ and $i_j \geq 0$ (here $y_{\beta}$ is a basis of $L_{-\beta}$). Since $D_\lambda$ is a one-dimensional $\mathfrak{U}(B)$-module, the tensor product over $\mathfrak{U}(B)$ identifies $b \otimes v^+$ with $1 \otimes b \cdot v^+$ for $b \in \mathfrak{U}(B)$. Thus $Z(\lambda)$ has basis $1 \otimes v^+$ together with the vectors $y_{\beta_1}^{i_1} \cdots y_{\beta_m}^{i_m} \otimes v^+$, all of which are linearly independent over $F$. In particular, $1 \otimes v^+ \neq 0$.

Moreover, for any $x_\alpha \in L_\alpha$ ($\alpha \succ 0$), we have
$$x_\alpha \cdot (1 \otimes v^+) = x_\alpha \otimes v^+ = 1 \otimes x_\alpha \cdot v^+ = 1 \otimes 0 = 0,$$
and for $h \in H$,
$$h \cdot (1 \otimes v^+) = h \otimes v^+ = 1 \otimes h \cdot v^+ = 1 \otimes \lambda(h) v^+ = \lambda(h)(1 \otimes v^+).$$
Thus $1 \otimes v^+$ is a maximal vector of weight $\lambda$, and $Z(\lambda) = \mathfrak{U}(L) \cdot (1 \otimes v^+)$ is standard cyclic.

For the second assertion, let $N^- = \bigoplus_{\alpha \prec 0} L_\alpha$. By the PBW decomposition, $\mathfrak{U}(L) \cong \mathfrak{U}(N^-) \otimes_F \mathfrak{U}(B)$ as vector spaces. Tensoring over $\mathfrak{U}(B)$ with the one-dimensional module $D_\lambda$ collapses the $\mathfrak{U}(B)$ factor, leaving an isomorphism $Z(\lambda) \cong \mathfrak{U}(N^-) \otimes_F D_\lambda \cong \mathfrak{U}(N^-)$ as $\mathfrak{U}(N^-)$-modules (since $D_\lambda$ is one-dimensional with trivial $N^-$-action). $\square$
