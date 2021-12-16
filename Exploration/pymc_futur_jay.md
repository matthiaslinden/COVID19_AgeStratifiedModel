# Overview
I have a Radeon VII GPU on my linux machine and would like to see my sampling in pymc3 make use of that resource.
The following paragraphs give an overview of how far I've come so far.

In Short:

* jax with ROCM works on AMD Radeon VII
* pymc + jax_sampler uses the GPU (slow)

## pymc3 futur
pymc3 has already started the transition to pymc (v4) moving from theano (or thano-pymc) to aesara (which is the still maintained fork of the original thano, after the original creators stopped development). aesara will allow greater flexibility at the backend of the compuational graph. For example using google's jax, which is descirbed as autograd+xla. XLA is a GPU backend originally developed for tensorflow.
One of the goals with regard to pymc is to move ot a jax-native sampler insted 

## History
In late 2020 theano-forks appeared with jax as linker (mainline-version no longer available thano-jaxlinker?).
Ideas layed out here: https://pymc-devs.medium.com/the-future-of-pymc3-or-theano-is-dead-long-live-theano-d8005f8a0e9b
pymc3 Code ran unaltered usind jax as backend.
furthermore numpyro's or tfp's NUTS implementations could be used via pymc3.sampling_jax. For example sample_tfp_nuts and sample_tfp_nuts_jit_vmap


## AMD's ROCM
In ML High-level-frontend + CUDA is widely available for Nvidia powered GPUs. AMD wokred 

I recently discovered, that compiling jax(lib) has the option to be base on ROCM.

# My tests
As jax+rocm seems to be the easy part now (Oct. 2021). How does it work together with pymc?

## pymc3 (based on v3.10.1)
* jax 0.2.11 (march 2021)
* jaxlib 0.1.73 (fairly recent)
* PyMC3 v3.10.1 (late 2020)
* tfp-nightly[jax] 0.15.0.dev211015 (latest)
* tensorflow-rocm 2.6.2
* theano (Theano-PyMC 1.0.11)

### Why those versions?
More recent v.3 versions dropped pm.sampling_jax options (tfp)
jax >= 0.2.12 dropped support for disabling omnistaging used in v.3 (might have to be changed to jax.config.disable_omnistaging(), see https://github.com/google/jax/blob/main/design_notes/omnistaging.md)

pymc3 3.10.1 is the version of multiple examples, including
https://github.com/pymc-devs/pymc/issues/4288

### What's working
* jax is using the GPU, greatly speeding up Matrix-mult (30k x 30k entries), rocm-smi shows proper Clock-increase and Mem/GPU usage. 

### What's not working
So far pm.sample doesn't seem to run on jax. pm.sampling_jax.sample_tfp_nuts etc. are all slower than 

## tfp + jax
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/954

# Further tests (TODO)
* pymc v3 > v3.10.1 with jax 0.2.11 to see if jax can be used through theano-pymc
* aesara without pymc v3/v4 to see if jax is kicking in on the gpu.
* pymc v4 with aesara


# Further reading:
* https://jax.readthedocs.io/en/latest/notebooks/XLA_in_Python.html XLA in python 
* https://discourse.pymc.io/t/theano-op-using-jax-for-lightning-fast-ode-inference/7244 jax ODE solver (got sundials to compile with required lapakc+klu, but most examples are broken.)
## jax
* https://rlouf.github.io/post/jax-random-walk-metropolis/
## webgpu
* https://doc.babylonjs.com/divingDeeper/postProcesses/defaultRenderingPipeline
* https://web.dev/gpu-compute/
* https://raphlinus.github.io/gpu/2020/02/12/gpu-resources.html
* https://gpuopen.com/learn/optimizing-gpu-occupancy-resource-usage-large-thread-groups/

# Other
* don't forget CPPFLAGS="-O3 -mavx2 if building from sratch (~20% python speedup, llvm 2-5% slower than gcc)
