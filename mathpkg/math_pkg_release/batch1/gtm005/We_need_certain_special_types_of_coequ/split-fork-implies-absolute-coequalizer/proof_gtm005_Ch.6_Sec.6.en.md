---
role: proof
locale: en
of_concept: split-fork-implies-absolute-coequalizer
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "6. Split Coequalizers"
---

Since a split fork is defined by equations involving only composites and identities, it remains a split fork under the application of any functor $T : C \to X$. For any functor $T$, the image
$$T a \xrightarrow[T \partial_1]{T \partial_0} T b \xrightarrow{T e} T c$$
with splitting arrows $T s : T c \to T b$ and $T t : T b \to T a$ still satisfies the split fork equations:
$$T e \circ T \partial_0 = T e \circ T \partial_1, \quad T e \circ T s = 1_{T c}, \quad T \partial_0 \circ T t = 1_{T a}, \quad T \partial_1 \circ T t = T s \circ T e.$$
Now suppose $f : T b \to d$ satisfies $f \circ T \partial_0 = f \circ T \partial_1$. Define $f' = f \circ T s : T c \to d$. Then
$$f' \circ T e = f \circ T s \circ T e = f \circ T \partial_1 \circ T t = f \circ T \partial_0 \circ T t = f \circ 1_{T a} = f.$$
For uniqueness, if $g \circ T e = f$ for some $g$, then $g = g \circ 1_{T c} = g \circ T e \circ T s = f \circ T s = f'$. Hence $T e$ is a coequalizer of $T \partial_0$ and $T \partial_1$ in $X$, making $e$ an absolute coequalizer.
