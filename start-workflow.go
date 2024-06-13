package main

import (
  "context"
  "go.temporal.io/sdk/client"
  "log"
)

func main() {
  // Create Temporal client
  c, err := client.NewClient(client.Options{})
  if err != nil {
    log.Fatalln("Unable to create client", err)
  }
  defer c.Close()

  // Start workflow
  options := client.StartWorkflowOptions{
    ID:        "simple_workflow",
    TaskQueue: "simple-task-queue",
  }
  we, err := c.ExecuteWorkflow(context.Background(), options, SimpleWorkflow)
  if err != nil {
    log.Fatalln("Unable to execute workflow", err)
  }

  log.Println("Started workflow", "WorkflowID", we.GetID(), "RunID", we.GetRunID())
}
