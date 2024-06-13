package main

import (
  "go.temporal.io/sdk/workflow"
  "time"
)

func SimpleWorkflow(ctx workflow.Context) error {
  logger := workflow.GetLogger(ctx)
  logger.Info("Tamu Technical Test")

  // Call an activity
  ao := workflow.ActivityOptions{
    StartToCloseTimeout: time.Minute,
  }
  ctx = workflow.WithActivityOptions(ctx, ao)
  var result string
  err := workflow.ExecuteActivity(ctx, SimpleActivity, "Temporal").Get(ctx, &result)
  if err != nil {
    logger.Error("Activity failed.", "Error", err)
    return err
  }

  logger.Info("Simple Workflow completed.", "Result", result)
  return nil
}
