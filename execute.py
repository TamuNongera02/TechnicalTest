from temporalio.client import Client
from temporal_neo4j import MyWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(MyWorkflow.run, "Tamu Test", id="my-workflow-id", task_queue="my-task-queue")
    print(f"Workflow result: {result}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
