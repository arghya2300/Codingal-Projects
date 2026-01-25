import numpy as np

np.random.seed(42) 

puppies =np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p=puppies.mean()
print("mean", p)
print("standard deviation", puppies.std())
print("variance", puppies.var())

np.random.choice(puppies, size=5, replace=True)
np.random.choice(puppies, size=5, replace=True).mean()

print("\nsampling distribution with size 5:")
sample_props = []

for i in range(10000):
    sample = np.random.choice(puppies, size=5, replace=True)
    sample_props.append(sample.mean())

sample_props = np.array(sample_props)
sm = sample_props.mean()

print("Mean", sample_props.mean())
print("Standard Deviation", sample_props.std())
print("Variance", sample_props.var())



print("\nsampling distribution with size 20:")
twenty_sample_props = []

for i in range(10000):
    sample = np.random.choice(puppies, size=20, replace=True)
    twenty_sample_props.append(sample.mean())

twenty_sample_props = np.array(twenty_sample_props)
sm = twenty_sample_props.mean()

print("Mean", twenty_sample_props.mean())
print("Standard Deviation", twenty_sample_props.std())
print("Variance", twenty_sample_props.var())