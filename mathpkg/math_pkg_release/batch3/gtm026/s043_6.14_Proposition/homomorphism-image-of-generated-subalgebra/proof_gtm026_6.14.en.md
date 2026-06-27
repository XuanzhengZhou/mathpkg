---
role: proof
locale: en
of_concept: homomorphism-image-of-generated-subalgebra
source_book: gtm026
source_chapter: "6"
source_section: "6.14"
---

Let $i \colon A \to X$ be an inclusion map and let $(p, j)$ be the image factorization of $i \cdot f$. Consider the diagram

\[
\begin{CD}
A @>i>> (X,\xi) @>f>> (Y,\theta) \\
@VVV @VVV @VVV \\
\langle A \rangle @>>> \langle Af \rangle
\end{CD}
\]

Using 1.4.31, we have $\langle Af \rangle = \operatorname{Im}(jT \cdot \theta)$. But this is the same as $\operatorname{Im}(pT \cdot jT \cdot \theta)$ since $pT$ is surjective (1.4.29). Thus
$$\langle Af \rangle = \operatorname{Im}(iT \cdot \xi \cdot f) = \langle A \rangle f.$$
