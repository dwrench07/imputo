from pandas import *
from scipy.stats import norm


# TODO: Connect to data source with Blaze
# TODO: Get data from data source with Odo
data = norm.rvs(size=100)
# print(data)
# TODO: Check for headers
# TODO: Check for correlation
# TODO: Split into arrays
# TODO: Get data type and summary statistics
# TODO:
"""
Maximum Likelihood Estimate(s) (MLEs) for any shape parameters (if applicable),
followed by those for location and scale.
For most random variables, shape statistics will be returned, but there are exceptions (e.g. norm).

https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.stats.rv_continuous.fit.html
"""
loc, scale = norm.fit(data)
"""
This fit is computed by maximizing a log-likelihood function, 
with penalty applied for samples outside of range of the distribution. 
The returned answer is not guaranteed to be the globally optimal MLE, 
it may only be locally optimal, or the optimization may fail altogether.
"""
print("loc = {}, scale = {}".format(loc, scale))

# TODO: Run all computations with Dask
# TODO: fit() returns dict with fitted data
# TODO: Imputo.compute(fitted_object, [size, default is size in original fitted_object]).
# Nothing done until compute() is called
# TODO: Return the data

"""Imputo - 



"""


class Impute(object):
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def provider(self):
        """For each ``object`` data type in the provided dataset find the provider mapping or best matching provider.

        Example:

            {
            providers:{
                    "Last Name": ['lName', 'l_name', 'LastName', 'lastName', etc.]
                    ...
                }
            }



        :return:
        """
        providers = {"Last Name": ['lName', 'l_name', 'LastName', 'lastName']}
        # TODO:
        try:
            if provider in providers:
                return provider

            else:
                for mapping in corpus:
                # TODO: return the mean of fuzzy matches for each provider taking the highest matching mean.
                return fuzzywuzzy.process.returnOne(provider, providers)

        except Exception as e:
            print(e)

        finally:

    # TODO: Ask user to validate fields

    def fit(self):
        pass

    def plot(self):
        """Plot the top 3 distributions with the lowest MLE.

        :return:
        """
        pass

    def summary(self):
        pass

    def params(self):
        """ Returns a dict of the parameters used to create (see imputo.json).

        :return:
        """
        pass


if __name__ == '__main__':
    Impute()