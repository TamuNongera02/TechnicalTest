from neo4j import GraphDatabase
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from datetime import timedelta

# Neo4j connection details for Cluster 1
NEO4J_URI_1 = "bolt://localhost:7687"
NEO4J_USER_1 = "VM1"
NEO4J_PASSWORD_1 = "password1"

# Neo4j connection details for Cluster 2 via SSH tunnel
NEO4J_URI_2 = "bolt://localhost:7687"
NEO4J_USER_2 = "VM2"
NEO4J_PASSWORD_2 = "password2"

# Create Neo4j driver instances
driver1 = GraphDatabase.driver(NEO4J_URI_1, auth=(NEO4J_USER_1, NEO4J_PASSWORD_1))
driver2 = GraphDatabase.driver(NEO4J_URI_2, auth=(NEO4J_USER_2, NEO4J_PASSWORD_2))

@activity.defn
async def create_node_activity_1(name: str) -> str:
    with driver1.session() as session:
        result = session.run("CREATE (n:Person {name: $name}) RETURN n", name=name)
        record = result.single()
        return record["n"]["name"]

@activity.defn
async def create_node_activity_2(name: str) -> str:
    with driver2.session() as session:
        result = session.run("CREATE (n:Person {name: $name}) RETURN n", name=name)
        record = result.single()
        return record["n"]["name"]

@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        result1 = await workflow.execute_activity(create_node_activity_1, name, start_to_close_timeout=timedelta(seconds=5))
        result2 = await workflow.execute_activity(create_node_activity_2, name, start_to_close_timeout=timedelta(seconds=5))
        return f"Created nodes in both clusters: {result1}, {result2}"

async def run_worker():
    client = await Client.connect("localhost:7233")
    worker = Worker(client, task_queue="my-task-queue", workflows=[MyWorkflow], activities=[create_node_activity_1, create_node_activity_2])
    await worker.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_worker())
