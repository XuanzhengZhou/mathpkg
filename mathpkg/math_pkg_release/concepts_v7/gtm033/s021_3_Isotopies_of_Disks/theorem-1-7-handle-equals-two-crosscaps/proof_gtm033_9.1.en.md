---
role: proof
locale: en
of_concept: handle-equals-two-crosscaps
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.7 (Handle Equals Two Crosscaps on Nonorientable Surface)

Attaching a handle to a connected nonorientable surface is the same as attaching two crosscaps. Therefore attaching a handle to a nonorientable surface of genus $p$ produces a nonorientable surface of genus $p + 2$.

**Proof.** Let $M$ be a connected nonorientable surface without boundary, and let $f: S^0 \times D^2 \hookrightarrow M$ be an embedding for handle attachment. We may suppose the image of $f$ is contained in the interior of a small disk $D \subset M$. Thus $M[f]$ is obtained by gluing together $M - \operatorname{Int} D$ and $D[f]$ along their boundaries.

If we identify $D$ with a hemisphere of $S^2$, and reinterpret $f$ as an embedding $g: S^0 \times D^2 \to S^2$, we find that

$$M[f] \approx M \# S^2[g].$$

Now $S^2[g]$ is a torus if $g$ is orientable, and a Klein bottle if $g$ is nonorientable. A Klein bottle is $S^2$ with two crosscaps attached (a nonorientable surface of genus $2$). Therefore, whether $g$ is orientable or not, $S^2[g]$ can be obtained by attaching two crosscaps. Consequently, $M[f] \approx M \# (\text{two crosscaps})$, which is $M$ with two crosscaps attached. Hence attaching a handle increases the nonorientable genus by $2$. $\square$
