package main

import (
  "go.temporal.io/sdk/client"
  "go.temporal.io/sdk/worker"
  "log"
)

func main() {
  // Create Temporal client
  c, err := client.NewClient(client.Options{})
  if err != nil {
    log.Fatalln("Unable to create client", err)
  }
  defer c.Close()

  // Create worker
  w := worker.New(c, "simple-task-queue", worker.Options{})

  // Register workflow and activity
  w.RegisterWorkflow(SimpleWorkflow)
  w.RegisterActivity(SimpleActivity)

  // Start worker
  err = w.Run(worker.InterruptCh())
  if err != nil {
    log.Fatalln("Unable to start worker", err)
  }
}
