---
role: proof
locale: en
of_concept: grover-search-rotation-claim
source_book: gtm053
source_chapter: "8"
source_section: "8.6"
---
(i) The operator $I_F$ reflects about the hyperplane orthogonal to $|x_0\rangle$ (inverting its sign and leaving other basis states unchanged). The operator $J = -I_\delta$ reflects about the hyperplane orthogonal to $|0\rangle$ with an additional global sign. Conjugating $J$ by $V$ gives $VJV$, which reflects about the hyperplane orthogonal to the uniform superposition $\xi$. The composition $T = VJVI_F$ of two reflections is a rotation in the plane they span, which is exactly the plane spanned by $\xi$ and $|x_0\rangle$. Both vectors lie in this plane and are invariant under the action of both $VJV$ and $I_F$.

(ii) Computing the matrix of $T$ restricted to this plane: $\xi$ and $|x_0\rangle$ are not orthogonal; their inner product is $\langle \xi | x_0 \rangle = 1/\sqrt{N}$. The angle $\varphi$ between them satisfies $\cos \varphi = 1/\sqrt{N}$. The rotation angle $\varphi_N$ of $T$ is twice the angle between the two reflection axes, giving $\cos \varphi_N = 1 - 2/N$ and $\sin \varphi_N = 2\sqrt{N-1}/N$. For large $N$, $\varphi_N \approx 2/\sqrt{N}$, so approximately $\pi\sqrt{N}/4$ iterations rotate $\xi$ to near $|x_0\rangle$.
