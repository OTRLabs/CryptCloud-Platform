package schema

import "entgo.io/ent"

// Team holds the schema definition for the Team entity.
type Team struct {
	ent.Schema
}

// Fields of the Team.
func (Team) Fields() []ent.Field {
	return nil
}

// Edges of the Team.
func (Team) Edges() []ent.Edge {
	return nil
}
