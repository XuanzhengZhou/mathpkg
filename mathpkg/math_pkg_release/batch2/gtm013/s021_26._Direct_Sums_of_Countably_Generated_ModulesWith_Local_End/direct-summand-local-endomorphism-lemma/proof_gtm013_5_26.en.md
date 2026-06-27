---
role: proof
locale: en
of_concept: direct-summand-local-endomorphism-lemma
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

Let $e$ and $e'$ be the projections of $M$ onto $K$ and $L$, and let $f$ be the projection onto $N$. Set $H = M(1 - e - e')$, so

$$K = Me, \quad L = Me', \quad H = M(1 - e - e').$$

Also, write $H \oplus H' = M(1 - f)$ for the complementary direct summand to $N = Mf$ in $M$.

Since $f\operatorname{End}(_R M)f \cong \operatorname{End}(_R N)$ is a local ring with identity $f$, and since $f = fef + fe'f$ (for $f(1 - e - e')f = 0$), we may assume that $fef$ is invertible in $f\operatorname{End}(_R M)f$. So let $s \in \operatorname{End}(_R M)$ with

$$s = fsf \quad \text{and} \quad sfef = fefs = f.$$

Then in $\operatorname{End}(_R M)$,

$$(ese)^2 = e(sfef)se = efse = ese,$$

so $ese$ is an idempotent. Hence

$$M = (\operatorname{Im} ese) \oplus (\operatorname{Ker} ese).$$

But $L \oplus H = M(1 - e) \leq \operatorname{Ker} ese$, so

$$\operatorname{Ker} ese = (\operatorname{Ker} ese) \cap (K \oplus L \oplus H) = ((\operatorname{Ker} ese) \cap K) \oplus L \oplus H.$$

Set $K' = (\operatorname{Ker} ese) \cap K$. Then

$$M = \operatorname{Im}(ese) \oplus K' \oplus L \oplus H,$$

and $p : m \mapsto mese$ defines the projection of $M$ onto $\operatorname{Im}(ese)$ along $K' \oplus L \oplus H$.

Now consider the restriction $(p \mid N) : N \to \operatorname{Im}(ese)$. Since

$$\operatorname{Im}(ese) = (Mes)ese \subseteq (Mf)ese = Nese \subseteq \operatorname{Im}(ese),$$

the image of $(p \mid N)$ is $\operatorname{Im}(ese)$. And since

$$fese = (fef)s(fe),$$

the map $(p \mid N)$ is a composite of monomorphisms. Thus $(p \mid N)$ is an isomorphism, and by (5.5),

$$M = N \oplus K' \oplus L \oplus H.$$

Setting $L' = L \oplus H$, we obtain $M = N \oplus K' \oplus L'$ with $K' \leq K$ and $L' \leq L$ as claimed.
