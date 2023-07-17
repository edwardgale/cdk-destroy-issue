
# CDK issue reproduction


asset_output causing `cdk destroy` to fail


1. Get repo
1. Assume AWS creds
1. `cdk deploy` (works)
1. `cdk destroy` gives:

RuntimeError: Cannot use `output` hash type when `bundling` is not specified.

