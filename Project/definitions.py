from dagster import Definitions
from my_script import hello_world

defs = Definitions(
    assets=[hello_world]
)