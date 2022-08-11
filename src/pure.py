import haiku as hk
import jax
import jax.numpy as jnp

m = 3
n = 2

# specify the computations to be performed
class Model(hk.Module):
  def __call__(self, x):
    A = hk.get_parameter('A', shape=(m, n), init=jnp.zeros)
    b = hk.get_parameter('b', shape=(m, 1), init=jnp.zeros)

    return jax.nn.tanh(A @ x + b)
    
# haiku transforms the object-oriented model into a functional one
model = hk.without_apply_rng(hk.transform(lambda x: Model()(x)))

# construct a concrete input 
x = jnp.ones((n, 1))

# initialize the parameters
params = model.init(jax.random.PRNGKey(0), x)

# perform the forward pass
out = model.apply(params, x)