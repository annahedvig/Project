from dagster import asset

@asset
def hello_world():
    print("Hello world")
    