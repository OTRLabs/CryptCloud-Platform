package main

import (
	"context"
	"cryptcloud/internal/config"
	"cryptcloud/internal/db"
	"cryptcloud/internal/logging"
	"errors"
	"log"
	"os"
	"os/signal"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func main() {
	if err := run(); err != nil {
		log.Fatalln(err)
	}
}

func run(err error) {
	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt)
	defer stop()

	// load config
	config, err := config.LoadConfig()
	if err != nil {
		return
	}

	// Set up database.
	if err = db.GetDatabase(ctx, config); err != nil {
		return
	}

	// Set up OpenTelemetry.
	otelShutdown, err := logging.SetupOTelSDK(ctx)
	if err != nil {
		return
	}
	// Handle shutdown properly so nothing leaks.
	defer func() {
		err = errors.Join(err, otelShutdown(context.Background()))
	}()

	// Set up router.
	chiRouter := chi.NewRouter()
	chiRouter.Use(middleware.Logger)

}
