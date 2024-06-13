package main

import (
  "context"
  "go.temporal.io/sdk/activity"
)

func SimpleActivity(ctx context.Context, name string) (string, error) {
  logger := activity.GetLogger(ctx)
  logger.Info("Simple Activity", "name", name)
  return "Hello " + name, nil
}
