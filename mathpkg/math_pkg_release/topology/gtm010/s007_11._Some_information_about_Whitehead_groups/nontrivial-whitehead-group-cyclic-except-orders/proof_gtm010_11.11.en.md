---
role: proof
locale: en
of_concept: nontrivial-whitehead-group-cyclic-except-orders
source_book: gtm010
source_chapter: "11"
source_section: "11"
---

Let j > 1 be a prime number less than q/2 such that j does not divide q. [It is an exercise that such a j exists provided q != 1, 2, 3, 4, 6.] Then (j, q) = 1, so there is an integer k, 0 < k < q, such that jk = +/-1 (mod q). Set k = k_hat if k_hat <= q/2 and k = q - k_hat if k_hat > q/2. Then jk = aq +/- 1.

Let U(t) = 1 + t + ... + t^{j-1}, V(t) = 1 + t + ... + t^{k-1}, Sigma(t) = 1 + t + ... + t^{q-1}. Then U(t)V(t) = (t^{jk} - 1)/(t - 1). Since jk = aq +/- 1, we can write this as 1 + B(t)Sigma(t). Thus Sigma(t) divides U(t)V(t) - 1, so uv = 1 in Z(G) where u = U(x)V(x) - a Sigma(x). If u is a unit then it is non-trivial because its support has size j+k-1 which is between 1 and q-1.
