package config

import (
	"fmt"

	"github.com/caarlos0/env/v11"
)

type config struct {
	Home             string `env:"HOME" envDefault:"~"`
	Port             int    `env:"PORT" envDefault:"8080"`
	Database         string `env:"DATABASE" envDefault:"cryptdb"`
	DatabaseUser     string `env:"DATABASE_USER" envDefault:"cryptdb"`
	DatabasePassword string `env:"DATABASE_PASSWORD" envDefault:"cryptdb"`
	DatabaseHost     string `env:"DATABASE_HOST" envDefault:"localhost"`
	DatabasePort     int    `env:"DATABASE_PORT" envDefault:"5432"`
	DatabaseName     string `env:"DATABASE_NAME" envDefault:"cryptdb"`

	//K8sCluster string `env:"K8S_CLUSTER" envDefault:"k8scluster"`
	//K8sClusterUser string `env:"K8S_CLUSTER_USER" envDefault:"k8scluster"`
}

func GetConfig() (*config, error) {
	cfg := &config{}
	if err := env.Parse(cfg); err != nil {
		return nil, fmt.Errorf("failed to get config: %w", err)
	}
	return cfg, nil
}
