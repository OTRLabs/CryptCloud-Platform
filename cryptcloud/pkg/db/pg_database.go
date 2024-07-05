package db

import (
	"context"
	"cryptcloud/ent"
	"cryptcloud/pkg/config"
	"log"

	_ "github.com/lib/pq"
)

func GetDatabase(ctx context.Context) *ent.Client {

	// Load config
	config, err := config.GetConfig()
	if err != nil {
		log.Fatalf("failed to load config: %v", err)
	}

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
