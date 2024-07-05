package temporal

import (
	"log"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
)

func StartTemporal() {
	// The client and worker are heavyweight objects that should be created once per process.
	c, err := client.NewClient(client.Options{
		HostPort: client.DefaultHostPort,
	})
	if err != nil {
		log.Fatalln("unable to create Temporal client", err)
	}
	defer c.Close()

	w := worker.New(c, "cryptcloud", worker.Options{})
	//w.RegisterWorkflow(cryptflows.CryptFlows)
	//w.RegisterActivity(cryptflows.CryptFlows)

	err = w.Run(worker.InterruptCh())
	if err != nil {
		log.Fatalln("unable to start Temporal worker", err)
	}
}
