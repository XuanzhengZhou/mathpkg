---
role: proof
locale: en
of_concept: schreier-refinement-theorem-modular-lattices
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Let

$$a = a_1 \geq a_2 \geq \cdots \geq a_{s+1} = b \tag{3}$$

and

$$a = b_1 \geq b_2 \geq \cdots \geq b_{t+1} = b \tag{4}$$

be two descending chains connecting $a$ and $b$. Introduce the elements

$$a_{ik} = (a_i \cap b_k) \cup a_{i+1}, \quad k = 1, 2, \ldots, t+1,$$
$$b_{ki} = (a_i \cap b_k) \cup b_{k+1}, \quad i = 1, 2, \ldots, s+1.$$

Then we obtain refinements

$$a = a_{11} \geq a_{12} \geq \cdots \geq a_{1,t+1} = a_{21} \geq a_{22} \geq \cdots \geq a_{2,t+1} \geq \cdots \geq a_{s,t+1} = b \tag{5}$$

and

$$a = b_{11} \geq b_{12} \geq \cdots \geq b_{1,s+1} = b_{21} \geq b_{22} \geq \cdots \geq b_{2,s+1} \geq \cdots \geq b_{t,s+1} = b \tag{6}$$

of (3) and (4) respectively. By the Zassenhaus lemma for modular lattices, the intervals $I[a_{ik}, a_{i,k+1}]$ and $I[b_{ki}, b_{k,i+1}]$ are projective. The correspondence

$$I[a_{ik}, a_{i,k+1}] \to I[b_{ki}, b_{k,i+1}]$$

establishes the equivalence of the refinements, proving the theorem.
