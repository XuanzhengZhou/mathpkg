---
role: proof
locale: en
of_concept: valuative-criterion-of-properness
source_book: gtm052
source_chapter: "II"
source_section: "4"
---

($\Rightarrow$) First assume that $f$ is proper. Then $f$ is separated, so uniqueness follows from Theorem 4.3. For existence, consider the base extension $T \to Y$ and let $X_T = X \times_Y T$. From the given maps $U \to X$ and $U \to T$, we obtain a map $U \to X_T$. Let $\xi_1 \in X_T$ be the image of the unique point $t_1$ of $U$. Let $Z = \{\xi_1\}^-$. Then $Z$ is a closed subset of $X_T$. Since $f$ is proper, it is universally closed, so $f': X_T \to T$ is closed, hence $f'(Z)$ is closed in $T$. But $f'(\xi_1) = t_1$, the generic point of $T$, so $f'(Z) = T$. Hence there is a point $\xi_0 \in Z$ with $f'(\xi_0) = t_0$. We obtain a local homomorphism $R \to \mathcal{O}_{\xi_0,Z}$. The function field of $Z$ is $k(\xi_1)$, which is contained in $K$. By (I, 6.1A), $R$ is maximal for the domination relation, so $R \cong \mathcal{O}_{\xi_0,Z}$. This gives the desired morphism $T \to X_T \to X$.

($\Leftarrow$) Assume the condition holds. Taking $R$ to be any valuation ring, the condition implies both the separatedness criterion (uniqueness of lift) and the existence of lifts. It suffices to show $f$ is universally closed. Let $Y' \to Y$ be any morphism, let $X' = X \times_Y Y'$, and let $Z$ be a closed subset of $X'$. We need to show $f'(Z)$ is closed in $Y'$. Since $f$ is of finite type, so is $f'$ and the restriction $f': Z \to Y'$ is quasi-compact. By Lemma 4.5, it suffices to show $f'(Z)$ is stable under specialization. Let $z_1 \in Z$, $y_1 = f'(z_1)$, and $y_1 \rightsquigarrow y_0$ a specialization. Let $\mathcal{O}$ be the local ring of $y_0$ on $\{y_1\}^-$ with reduced structure. Then $k(y_1)$ is a subfield of $k(z_1)$. Let $K = k(z_1)$, and let $R$ be a valuation ring of $K$ dominating $\mathcal{O}$. By (4.4) we obtain morphisms $U \to Z$ and $T \to Y'$. Composing with $Z \to X' \to X$ and $Y' \to Y$, we apply the condition to obtain $T \to X$. Since $X'$ is a fiber product, this lifts to $T \to X'$. Since $Z$ is closed and the generic point of $T$ maps to $z_1 \in Z$, this factors through $T \to Z$. Let $z_0$ be the image of $t_0$; then $f'(z_0) = y_0$, so $y_0 \in f'(Z)$.
