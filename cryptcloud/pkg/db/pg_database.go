package db

import (
	"context"
	"cryptcloud/ent"
	"cryptcloud/pkg/config"
	"log"

	_ "github.com/lib/pq"
)

func GetDatabase(ctx context.Context, config *config.Config) *ent.Client {
	// Create client
	ctx = context.Background()

	client, err := ent.Open("postgres", config.Database.DSN)
	if err != nil {
		log.Fatalf("failed opening connection to sqlite: %v", err)
	}
	// Run the auto migration tool.
	if err := client.Schema.Create(ctx); err != nil {
		log.Fatalf("failed creating schema resources: %v", err)
	}
	return client
}
