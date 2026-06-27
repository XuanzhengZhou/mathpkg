---
role: proof
locale: en
of_concept: product-composition-rules
source_book: gtm004
source_chapter: "II"
source_section: "5"
---

# Proof of Composition Rules for Products

Let $f_i : Z \to X_i$, $g : W \to Z$, $g_i : X_i \to Y_i$, $i \in I$, and suppose the products in question exist.

**(i)** $\{f_i\} g = \{f_i g\}$.

Let $(X; p_i) = \prod_i X_i$. By definition, $\{f_i\} : Z \to X$ is the unique morphism with $p_i \{f_i\} = f_i$. Then $p_i (\{f_i\} g) = (p_i \{f_i\}) g = f_i g$. Since $\{f_i g\}$ is the unique morphism $W \to X$ with $p_i \{f_i g\} = f_i g$, we have $\{f_i\} g = \{f_i g\}$.

**(ii)** $(\prod_i g_i) \{f_i\} = \{g_i f_i\}$.

Let $(Y; q_i) = \prod_i Y_i$. By definition of the product of morphisms, $q_i (\prod_i g_i) = g_i p_i$. Then

$$q_i \left( (\prod_i g_i) \{f_i\} \right) = (q_i \prod_i g_i) \{f_i\} = g_i p_i \{f_i\} = g_i f_i.$$

Since $\{g_i f_i\}$ is the unique morphism with $q_i \{g_i f_i\} = g_i f_i$, we obtain $(\prod_i g_i) \{f_i\} = \{g_i f_i\}$.

In both cases, it suffices to verify that each side projects properly onto the $i$-component under the projection $p_i$ (or $q_i$).
