from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda_python_alpha as lambda_alpha, AssetHashType,
    aws_lambda as lambda_

    # aws_sqs as sqs,
)
from constructs import Construct

class GithubReproduceCdkErrorStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        lambda_alpha.PythonFunction(
            self,
            "MyFunc",
            entry="./",
            index="function.py",
            handler="lambda_handler",
            bundling=lambda_alpha.BundlingOptions(
                asset_excludes=[".venv", "cdk.out"],
                asset_hash_type=AssetHashType.OUTPUT,
            ),
            runtime = lambda_.Runtime.PYTHON_3_10
        )